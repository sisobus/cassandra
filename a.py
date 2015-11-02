#!/usr/bin/python
#-*- coding:utf-8 -*-
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('MyKeyspace')
cf = ColumnFamily(pool, 'MyCF')
#cf.insert('row_key', {'col_name': 'col_val'})
#cf.insert('row_key', {'col_name':'col_val', 'col_name2':'col_val2'})
#cf.batch_insert({'row1': {'name1': 'val1', 'name2': 'val2'},'row2': {'foo': 'bar'}})

print cf.get('row_key')
print cf.get('row_key', columns=['col_name', 'col_name2'])

#for i in xrange(10):
#    cf.insert('row_key', {str(i): 'val'})
print cf.get('row_key', column_start='5', column_finish='7')
print cf.get('row_key', column_reversed=True, column_count=3)
print cf.multiget(['row1', 'row2'])

result = cf.get_range(start='row_key5', finish='row_key7')
for key, columns in result:
    print key, '=>', columns
