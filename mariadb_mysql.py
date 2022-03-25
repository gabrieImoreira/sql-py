import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user ='@USER',
        password='@PASSWORD',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield connection
    finally:
        print('\n--- Closed connection ---')
        connection.close()

with connect() as connection:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        connection.commit()

with connect() as connection:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        data = [
            ('Muriel', 'Lopes', 19, 89),
            ('Yan', 'BigHouse', 22, 59),
            ('Fabio', 'Morgante', 31, 109),
        ]
        cursor.executemany(sql, data)
        connection.commit()

with connect() as connection:
    with connection.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql, (6,))
        connection.commit()

with connect() as connection:
    with connection.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id = %s'
        cursor.execute(sql, ('João',1))
        connection.commit()

with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        result = cursor.fetchall()

        for linha in result:
            print(linha)
