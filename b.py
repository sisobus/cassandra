#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
import glob
from pycassa.system_manager import *
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

sys = SystemManager('localhost:9160')
#sys.create_keyspace('employees', SIMPLE_STRATEGY, {'replication_factor': '1'})
pool = ConnectionPool('employees')
filenames = glob.glob('employees/*.csv')
for filename in filenames:
    only_name = filename.split('/')[-1].split('.')[0]
    print only_name
#sys.create_column_family('employees',only_name,super=False)
#sys.drop_column_family('employees',only_name)
    cf = ColumnFamily(pool, only_name)
    csv_file = open(filename,'rb')
    reader = csv.reader(csv_file)
    r = 1
    for row in reader:
        c = 1
        for col in row:
            cf.insert('row'+str(r), {'col'+str(c): col})
            c += 1
        r += 1
