#!/usr/bin/env python
import paramiko, time, argparse, os, pwd, re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

user = pwd.getpwuid(os.getuid()).pw_name

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script for syncing local and remote files')
    parser.add_argument('-l', '--local', type=str, required=False,
            help='Local folder')
    parser.add_argument('-r', '--remote', type=str, required=True,
            help='Remote host:/folder')
    return parser.parse_args()

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            push_file(event.src_path, rhost, rdir)

def push_file(lpath, rhost, rdir):
    if rdir[-1] == '/':
        rpath = rdir + os.path.basename(lpath)
    else:
        rpath = rdir + '/' + os.path.basename(lpath)
    ssh  = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(rhost, username=user)
    sftp = ssh.open_sftp()
    sftp.put(os.path.basename(lpath), rpath)
    sftp.close()
    ssh.close()

if __name__ == '__main__':
    local_files = []
    local_times = {}
    args = parse_arguments()
    rhost, rdir = re.search('([a-zA-z0-9\.\-\_]+):/{0,1}(/{1}.+)', args.remote).group(1,2)
    if args.local:
        ldir = args.local
    else:
        ldir = os.getcwd()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path = ldir, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
