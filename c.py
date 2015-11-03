#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
import glob
from pycassa.system_manager import *
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('employees')
filenames = glob.glob('employees/*.csv')
for filename in filenames:
    only_name = filename.split('/')[-1].split('.')[0]
    print only_name
    cf = ColumnFamily(pool, only_name)
    print cf.multiget(['row1','row2'])
    break
