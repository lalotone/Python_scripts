import psutil 
import socket

loadCpuArray = []
loadCpuFile = open("cpuLoadData.txt", 'r+')

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def sysUtils():
    minutesOn = (psutil.boot_time() / 60)
    return minutesOn

def cpuUsage():
    cpuUsg = psutil.cpu_percent(interval=1)
    loadCpuFile.write("\n" + str(cpuUsg))

def ramData():
    totalRam = bytes2human(psutil.virtual_memory().total)
    freeRam = bytes2human(psutil.virtual_memory().available)

def utilsHDD():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partitionUsage = psutil.disk_usage(partition.mountpoint)       
        mntPoint = partition.mountpoint
        totalPartition = bytes2human(partitionUsage.total)
        partitionUsage = bytes2human(partitionUsage.used)
        partitionFree = bytes2human(partitionUsage.free)
	
def netUtils():
    stats = psutil.net_if_stats()

    for nic, addrs in psutil.net_if_addrs().items():
        print nic
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])

cpuUsage()
loadCpuFile.close()
