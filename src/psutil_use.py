#!/usr/bin/python
# coding:utf-8
import psutil
import platform
'''
资源获取
'''
def is_os():
    # 判断平台window，linux
    print("platform.platform()=%s" % platform.platform())
    print('platform.machine()--', platform.machine())
    print('platform.python_version()', platform.python_version())
    print('platform.system()', platform.system())
    print('platform.uname()', platform.uname()) # 所有信息

def cpu_info():
    cpu_frep = psutil.cpu_freq()
    cpu_per = psutil.cpu_percent() # cpu使用量
    cpu_status = psutil.cpu_stats()
    cpu_times = psutil.cpu_times()
    print('cpu_frep:', cpu_frep)
    print('cpu_per:', cpu_per)
    print('cpu_status:', cpu_status)
    print('cpu_times:', cpu_times)

def mem_info():
    mem = psutil.virtual_memory()
    print(
        'mem_used: %s M' % (mem.used/1024/1024),
        'mem_total:%s M '% (mem.total/1024/1024),
        'mem_free: ',mem.free
    )

def disk_info():
    pass

def main():
    is_os()
    cpu_info()
    mem_info()

if __name__ == '__main__':
    main()
