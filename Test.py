import mysql.connector
mycon = mysql.connector.connect(user='root', password='10Dec1964',
                                database='ocsl',
                                host='localhost',
                                auth_plugin='mysql_native_password')
mycursor = mycon.cursor()
mycursor.execute("select * from student where college != 'abc'")
for db in mycursor:
    print(db)