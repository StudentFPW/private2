import psycopg2

# ----------------------------------------------------------------------------------------------------------------------

# Эта строка кода устанавливает соединение с базой данных PostgreSQL со следующими параметрами:
#       `user`: имя пользователя, используемое для подключения к базе данных.

#       `пароль`: пароль, используемый для аутентификации пользователя

#       `host`: адрес сервера, на котором размещена база данных
#       (в данном случае это локальная машина с IP-адресом 127.0.0.1)

#       `port`: номер порта, используемый для подключения к базе данных
#       (в данном случае это порт по умолчанию для PostgreSQL,5432).

#       `база данных`: имя базы данных для подключения (в данном случае это база данных с именем «test_db»)

conn = psycopg2.connect(user="postgres",
                        password="skillfactory",
                        host="127.0.0.1",
                        port="5432",
                        database="test_db")

# ----------------------------------------------------------------------------------------------------------------------

# `cur = conn.cursor()` создает объект курсора, который позволяет нам выполнять команды SQL
# и получать результаты из базы данных.

cur = conn.cursor()

# ----------------------------------------------------------------------------------------------------------------------

# Эта строка кода создает новую таблицу с именем «test» в подключенной базе данных PostgreSQL с тремя столбцами:
# «id» (последовательный первичный ключ),
# «num» (целое число)
# «data» (varchar).

# cur.execute(
#     "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
# )

# ----------------------------------------------------------------------------------------------------------------------

# Эта строка кода вставляет новую строку в таблицу «test» со значениями 100 для столбца «num» и «abc'def» для столбца
# «data». Значения передаются в виде кортежа в метод execute с использованием заполнителей (%s) для предотвращения атак
# путем внедрения кода SQL.

cur.execute(
    "INSERT INTO test (num, data) VALUES (%s, %s)",
    (100, "abc'def")
)

# ----------------------------------------------------------------------------------------------------------------------

# `cur.execute("SELECT * FROM test;")` выполняет SQL-запрос для выбора всех строк и столбцов из таблицы с именем «test».

cur.execute("SELECT * FROM test;")

# ----------------------------------------------------------------------------------------------------------------------

# `cur.fetchone()` — это метод, который извлекает следующую строку набора результатов запроса и возвращает ее в виде
# кортежа. В этом конкретном коде он используется для извлечения первой строки набора результатов запроса, возвращаемого
# инструкцией SELECT, выполненной в «тестовой» таблице.

print(cur.fetchone())

# ----------------------------------------------------------------------------------------------------------------------

# `conn.commit()` фиксирует текущую транзакцию в базе данных. Это означает, что любые изменения, внесенные в базу данных
# во время текущей транзакции, будут сохранены навсегда.

conn.commit()

# ----------------------------------------------------------------------------------------------------------------------

# `cur.close()` закрывает объект курсора, что освобождает ресурсы, удерживаемые курсором, и освобождает память.

cur.close()

# ----------------------------------------------------------------------------------------------------------------------

# `conn.close()` закрывает соединение с базой данных PostgreSQL, освобождая все ресурсы, удерживаемые соединением, и
# освобождая память.

conn.close()

# ----------------------------------------------------------------------------------------------------------------------
