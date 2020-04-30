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
	with connection.cursor() as cursor:
		sql = 'SELECT * FROM Artist;'
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)
finally:
	# close the connection regarless of the above outcome
	connection.close()
