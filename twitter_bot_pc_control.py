#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import subprocess
import psutil
import re

api = TwitterAPI('', '',  '', '')

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

def temp_get():
	#take the CPU temperature (Linux Only)
	cpu_raw_temp = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])
	cpu_temp_float = float(cpu_raw_temp)
	cpu_temp = cpu_temp_float/1000
	return cpu_temp
def cpu_usage():
	#cpu percent usage
	cpu_per = psutil.cpu_percent(interval=1)
	return cpu_per	
def ram_usage():
	mem = psutil.virtual_memory()
	ram_free = mem.available		
	ram_free = bytes2human(ram_free)
	return ram_free
def hdd_usage():
	hdd_usage = psutil.disk_usage('/')
	hdd_free = hdd_usage.free
	hdd_free_Mb = hdd_free / 1000000
	hdd_free_Gb = hdd_free_Mb / 1024 
	return hdd_free_Gb

cpu_temp = temp_get()
cpu_per = cpu_usage()
ram_free = ram_usage()
hdd_free = hdd_usage()

#print ("Temperature: "+str(cpu_temp)+" ºC")
#print ("Cpu usage: "+str(cpu_per)+" %")
#print ("Free ram: "+str(ram_free))
#print ("Free hdd: "+str(hdd_free)+" Gb")

r = api.request('statuses/update', {'status':'Hellcat temperature: '+str(cpu_temp)+' C ,Cpu usage: '+str(cpu_per)+'% ,free ram: '+str(ram_free)+', HDD free: '+str(hdd_free)+' Gb'})
