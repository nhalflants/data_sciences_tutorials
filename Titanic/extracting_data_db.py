import sqlite3
import pymysql

### SQLITE3 Database

# open connection
connection = sqlite3.connect("classroomDB.db")
# open cursor
cursor = connection.cursor()

# create_table = """
#                 CREATE TABLE classroom (
#                     student_id INTEGER PRIMARY KEY,
#                     name VARCHAR(20),
#                     gender CHAR(1),
#                     note INTEGER
#                 );"""

# cursor.execute(create_table)

# classroom_data = [(1, "Nat", "F", 70),
#                   (2, "Manu", "M", 75)]

# for student in classroom_data:
#     insert_statement = """INSERT INTO classroom
#     (student_id, name, gender, note)
#     VALUES ({0}, "{1}", "{2}", {3});""".format(student[0], student[1], student[2], student[3])

#     cursor.execute(insert_statement)

query = "SELECT * FROM classroom"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

# connection.commit()
connection.close()


### MySQL Database

cnx = {
    'host': 'localhost',
    'username': 'root',
    'password': 'root',
    'db': 'tinkle_drink_db'
}

connection = pymysql.connect(cnx['host'],cnx['username'],cnx['password'],cnx['db'],port=8888)
cursor = connection.cursor()

query = "SELECT * FROM wp_posts"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

connection.close()
