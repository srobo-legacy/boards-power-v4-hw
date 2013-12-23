#!/usr/bin/env python
import sys

start = sys.stdin.readline()
start_time, start_temp = [float(x) for x in start.strip().split(",")]

for sample in sys.stdin:
    cur_time, cur_temp = [float(x) for x in sample.strip().split(",")]
    print "%f %f" % (cur_time - start_time, cur_temp - start_temp)
