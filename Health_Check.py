#!/usr/bin/env python3


import shutil
import psutil

def dis(disk):
	du = shutil.disk_usage(disk)
	free = du. free / du. total * 100
	return free > 20

def cpu():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not dis('/') or not cpu():
	print('Error')
else:
	print('Everything is ok')
