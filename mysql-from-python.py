import pymysql

# import os

# Get username
# depended on environment
# username = os.getenv('username')
username = 'nic'

# connect to database
connection = pymysql.connect(host='localhost', user=username, password='P4ss-word', db='Chinook')

try:
    # run a query
    # connection.cursor(pymysql.cursors.DictCursor) = optional to replace tupel as dictionary
    # with connection.cursor() as cursor:
    # sql = 'SELECT * FROM Genre;'
    # cursor.execute(sql)
    # result = cursor.fetchall() # get data back
    # for row in cursor:
    # print(row)

    with connection.cursor() as cursor:
        # inserting values
        # row = ("Bob", 21, "1990-02-06 23:04:56")
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 12:12:45"),
                ("Fred", 100, "1911-09-12 0.:01:01")]
        # rows = [(23, "Bob"),
        #         (24, "Jim"),
        #         (25, "Fred")]

        # rows = ["Bob", "Jim", "Fred"]

        # cursor.execute("DELETE FROM Friends where name = %s;", 'bob')  # delete using interpolation
        # cursor.executemany("DELETE FROM Friends where name = %s;", rows)  # delete many using interpolation
        # cursor.execute("INSERT INTO Friends VALUES (%s,%s,%s );", row) # single add values
        # cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';") # single update
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        #                (23, 'Bob'))  # single interpolated update
        # cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s );", rows)  # executes a list of tuples
        # cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows) # executes update a list of tuples
        # cursor.execute("DELETE FROM Friends Where name ='Bob';") # deletes from row
        names = ["Bob", "Fred"]
        lsNames = ','.join(['%s'] * len(names))
        tnames = tuple(names)

        # cursor.execute("DELETE FROM Friends WHERE name in (%s,%s);", names)
        cursor.execute(f"DELETE FROM Friends WHERE name in {tuple(names)};")  # can also use a tuple on the list

        # cursor.execute(f"DELETE FROM Friends WHERE name in ({','.join(['%s']*len(names))});", names) # Multiply the
        # number of %S by the len of the names list to get the correct amount
        connection.commit()
        # Creating the Table
        # cursor.execute("""CREATE TABLE IF NOT EXISTS
        #                 Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will display a warning if table exists
finally:
    # close the connection regarless of the above outcome
    connection.close()
