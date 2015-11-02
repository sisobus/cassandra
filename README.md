# cassandra
for Ahn

## ubuntu에 Cassandra 설치하기 
### java 설치 확인
```
    $ java -version
```
### Add the DataStax Community repository to the /etc/apt/sources.list.d/cassandra.sources.list
```
    $ echo "deb http://debian.datastax.com/community stable main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
```
### Add the DataStax repository key to your aptitude trusted keys.
```
    $ curl -L http://debian.datastax.com/debian/repo_key | sudo apt-key add -
```
### apt-get 업데이트 및 설치
```
    $ sudo apt-get update
    $ sudo apt-get install dsc20=2.0.11-1 cassandra=2.0.11
```
### Because the Debian packages start the Cassandra service automatically, you must stop the server and clear the data:
Doing this removes the default cluster_name (Test Cluster) from the system table. All nodes must use the same cluster name.
```
    $ sudo service cassandra stop
    $ sudo rm -rf /var/lib/cassandra/data/system/*
    $ sudo service cassandra start
```

## virtualenv로 python 개발 환경 만들기
### 카산드라 테스트 할 디렉토리로 감
```
    $ cd /home/sisobus/cassandra
```
### virtualenv로 독립적인 파이썬 개발 환경 만들기
```
    $ virtualenv venv
    $ . venv/bin/activate
```
### pip 를 이용하여 pycassa 설치하기
```
    (venv)$ pip install pycassa
    (venv)$ pip freeze : 설치 되어있는지 확인
```

## cassandra-cli 를 이용하여 테스트 keyspace 및 column family를 추가
### cassandra-cli 실행 및 keyspace, column family 추가
```
    (venv)$ cassandra-cli
    Connected to: "Test Cluster" on 127.0.0.1/9160
    Welcome to Cassandra CLI version 2.0.11

    The CLI is deprecated and will be removed in Cassandra 3.0.  Consider migrating to cqlsh.
    CQL is fully backwards compatible with Thrift data; see http://www.datastax.com/dev/blog/thrift-to-cql3

    Type 'help;' or '?' for help.
    Type 'quit;' or 'exit;' to quit.

    [default@unknown] create keyspace testKeyspace;
    [default@unknown] use testKeyspace;
    [default@unknown] create column family testColumnFamily;
    [default@unknown] quit;
```

## pycassa로 테스트 해보기
### test python source code 작성하기
```
    (venv)$ vi a.py

    #!/usr/bin/python
    #-*- coding:utf-8 -*-
    from pycassa.pool import ConnectionPool
    from pycassa.columnfamily import ColumnFamily

    pool = ConnectionPool('MyKeyspace')
    cf = ColumnFamily(pool, 'MyCF')
    cf.insert('row_key', {'col_name': 'col_val'})
    cf.insert('row_key', {'col_name':'col_val', 'col_name2':'col_val2'})
    cf.batch_insert({'row1': {'name1': 'val1', 'name2': 'val2'},'row2': {'foo': 'bar'}})

    print cf.get('row_key')
    print cf.get('row_key', columns=['col_name', 'col_name2'])

    for i in xrange(10):
        cf.insert('row_key', {str(i): 'val'})
    print cf.get('row_key', column_start='5', column_finish='7')
    print cf.get('row_key', column_reversed=True, column_count=3)
    print cf.multiget(['row1', 'row2'])

    result = cf.get_range(start='row_key5', finish='row_key7')
    for key, columns in result:
        print key, '=>', columns
```
### 실행해보기
```
    (venv)$ python a.py
```
