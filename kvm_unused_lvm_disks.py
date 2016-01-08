#!/usr/bin/env python

import subprocess
import os
import sys

euid = os.getuid()
if euid != 0:
    print "Running sudo..."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)

def disks_hash(disk_list):
    disks_hash = {}
    for i in range(len(disk_list)):
        disks_hash[disk_list[i].split('/').pop()] = disk_list[i]
    return disks_hash

def vm_list_disks():
    vm_info = []
    vm_list = []
    vm_disks_info = []
    vm_disks_list = []
    proc = subprocess.Popen(['virsh', 'list', '--all'], stdout = subprocess.PIPE)
    out = proc.stdout.read()
    for i in out.split('\n'):
        if i:
            vm_info.append(i.split())
        else:
            pass
    vm_info = vm_info[2:]
    for i in vm_info:
        vm_list.append(i[1])
    for vm in vm_list:
        proc = subprocess.Popen(['virsh', 'domblklist', vm], stdout = subprocess.PIPE)
        out = proc.stdout.read()
        vm_disks_info.append(out.split())
    for vd in vm_disks_info:
        i = 4
        while i < len(vd):
            vm_disks_list.append(vd[i])
            i += 2
    return vm_disks_list

def lvm_list_disks(FOLDERS):
    lvm_info = []
    lvm_disks_list= []
    proc = subprocess.Popen('lvdisplay', stdout = subprocess.PIPE)
    out = proc.stdout.read()
    for i in out.split('---\n'):
        if i:
            lvm_info.append(i.split())
        else:
            pass
    lvm_info = lvm_info[1:]
    for i in lvm_info:
        for j in FOLDERS:
            if (j in i[2]):
                lvm_disks_list.append(i[2])
            else:
                pass
    return lvm_disks_list

def compare_disks(vm_list_disks, lvm_disks_list):
    lvm_unmatched_disks = []
    for i in lvm_disks_list:
        if i in vm_list_disks:
            pass
        else:
            lvm_unmatched_disks.append(i)
    return lvm_unmatched_disks

def print_out(lvm_unmatched_disks):
    print('\nUnused LVM disks:')
    for i in lvm_unmatched_disks:
        print(i)

if __name__ == '__main__':
    FOLDERS = ['shared', 'office', 'virtual', 'dev']
    print_out(compare_disks(vm_list_disks(), lvm_list_disks(FOLDERS)))
    print('')
    print(disks_hash(lvm_list_disks(FOLDERS)))
