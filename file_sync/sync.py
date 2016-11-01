#!/usr/bin/env python

import os, subprocess, sys, pwd, grp, stat
import socket, requests, json, yaml, time, logging, re, argparse
import paramiko
from pprint import pprint

_api = 'https://foobar.ru/api/'
user, group = pwd.getpwuid(os.getuid()).pw_name, grp.getgrgid(pwd.getpwuid(os.getuid()).pw_gid).gr_name

def get_hosts(hostname):
    all_hosts = []
    try:
        host_groups = [group['name'] for group in json.loads(requests.get(_api + \
                'foo/{}?format=json'.format(hostname)).text)]
    except Exception as e:
        host_groups = []
        logging.warning('{}: {}'.format(e.__class__.__name__, e))
    if host_groups:
        for group in host_groups:
            all_hosts.extend([host['fqdn'] for host in json.loads(requests.get(_api + \
                    'bar/{}?format=json'.format(group)).text)])
        all_hosts = list(set(all_hosts))
        all_hosts.remove(hostname)
    return all_hosts

def get_config(*args):
    local = False
    if args and type(args) is tuple: local = args[0]
    config = {}
    config_files = filter(lambda x: re.match('config-[0-9]+.yml', x), os.listdir('./'))
    if local:
        if config_files:
            timestamp = max([re.search('config-([0-9]+).yml', x).group(1) for x in config_files])
            with open('config-{}.yml'.format(timestamp), 'r') as config_file:
                try:
                    config = yaml.load(config_file)
                except Exception as e:
                    logging.warning('{}: {}'.format(e.__class__.__name__, e))
    else:
        try:
            config = yaml.load((requests.get('https://raw.githubusercontent.com/' \
                    'asmartishin/python_scripts/master/file_sync/config.yml').text))
            list(map(os.remove, config_files))
            with open('config-{}.yml'.format(int(time.time())), 'w') as config_file:
                config_file.write(yaml.dump(config ,default_flow_style=False))
        except Exception as e:
            logging.warning('{}: {}'.format(e.__class__.__name__, e))
            if config_files:
                timestamp = max([re.search('config-([0-9]+).yml', x).group(1) for x in config_files])
                with open('config-{}.yml'.format(timestamp), 'r') as config_file:
                    try:
                        config = yaml.load(config_file)
                    except Exception as e:
                        logging.warning('{}: {}'.format(e.__class__.__name__, e))
    return config

# Here directory permission changes to the ones, that the user starting the script has,
# cause I assume that we start it under admin user, don't know if it is a good idea.
def get_local_files(config):
    local_files = []
    for directory in config['directories']:
        if not os.path.isdir(directory):
            subprocess.call('sudo mkdir -p {}'.format(directory), shell=True)
        if user != pwd.getpwuid(os.stat(directory).st_uid).pw_name or \
                group != grp.getgrgid(os.stat(directory).st_gid).gr_name:
            subprocess.call('sudo chown -R {}:{} {}'.format(user, group, directory), shell=True)
        for dirpath, dirnames, filenames in os.walk(directory):
            local_files += [os.path.join(dirpath, filename) for filename in filenames]
    return local_files

def get_host_files(hostname, config):
    remote_files = []
    ssh  = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user)
    sftp = ssh.open_sftp()
    for directory in config['directories']:
        try:
            sftp.stat(directory)
        except IOError as e:
            if e.errno == 2:
                ssh.exec_command(('sudo mkdir -p {}').format(directory))
        huser, hgroup = re.search('([A-Za-z]+)\ ([A-Za-z_ ]+)\ ' ,ssh.exec_command(('ls -ld {}').\
                format(directory))[1].read().rstrip()).group(1, 2)
        if user != huser or group != hgroup:
            ssh.exec_command('sudo chown -R {}:{} {}'.format(user, group, directory))
        remote_files.extend(ssh.exec_command(('find {} -type f | xargs readlink -f').\
                format(directory))[1].read().splitlines())
    sftp.close()
    ssh.close()
    return remote_files

def push_files(local_files_tuple, remote_files):
    print('Push: ')
    hostname = local_files_tuple[0]
    local_files = local_files_tuple[1]
    for rhost in remote_files:
        ssh  = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(rhost, username=user)
        sftp = ssh.open_sftp()
        for lfile in local_files:
            if lfile not in remote_files[rhost]:
                if lfile.split('/')[-2] not in remote_files.keys():
                    pdir, pfile =  os.path.split(lfile)
                    rdir = '{}/{}'.format(pdir, hostname)
                    rpath = '{}/{}/{}'.format(pdir, hostname, pfile)
                    ssh.exec_command('mkdir -p {}'.format(rdir))
                    print('{} --> {}:{}'.format(lfile, rhost, rpath))
                    sftp.put(lfile, rpath)
        sftp.close()
        ssh.close()
    print

def pull_files(local_files_tuple, remote_files):
    print('Pull: ')
    hostname = local_files_tuple[0]
    local_files = local_files_tuple[1]
    all_hosts = remote_files.keys()
    all_hosts.append(hostname)
    for rhost in remote_files:
        ssh  = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(rhost, username=user)
        sftp = ssh.open_sftp()
        for rfile in remote_files[rhost]:
            if rfile not in local_files:
                if rfile.split('/')[-2] not in all_hosts:
                    pdir, pfile =  os.path.split(rfile)
                    ldir = '{}/{}'.format(pdir, rhost)
                    lpath = '{}/{}/{}'.format(pdir, rhost, pfile)
                    subprocess.call('mkdir -p {}'.format(ldir), shell=True)
                    print('{} <-- {}:{}'.format(lpath, rhost, rfile))
                    sftp.get(rfile, lpath)
        sftp.close()
        ssh.close()
    print


def parse_arguments():
    parser = argparse.ArgumentParser(description='Script for syncing files on servers')
    parser.add_argument('-l', '--local', action='store_true', default=False,
                        help='Use local copy of config file')
    return parser.parse_args()

if __name__ == "__main__":
    remote_files = {}
    args = parse_arguments()
    hostname = socket.getfqdn()
    remote_hosts = get_hosts(hostname)
    config = get_config(args.local)
    if not config:
        raise RuntimeError('Could not load config. Exiting.')
    local_files_tuple = (hostname, get_local_files(config))
    for host in remote_hosts:
        try:
            remote_files[host] = get_host_files(host, config)
        except Exception as e:
            logging.warning('{}: {}'.format(e.__class__.__name__, e))
    push_files(local_files_tuple, remote_files)
    pull_files(local_files_tuple, remote_files)
