import mysql.connector 
import os
import warnings 
import pandas as pd 
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

db_user = os.environ.get('MYSQL_DB_USER')
db_password = os.environ.get('MYSQL_DB_PASSWORD')
print(db_user,db_password)

print(mysql.connector.__version__)
try:
	hr_con = mysql.connector.connect(
		host = 'localhost',
		database = 'sql_hr',
		user = db_user,
		password = db_password  
	)
except:
	print('Connection is not established')
	sys.exit('Stopping the execution')

else:
	print('Connection object : ',hr_con)
	db_info = hr_con.get_server_info()

def execute(query,con):
	cursor = con.cursor() 
	cursor.execute(query)
	records = cursor.fetchall()
	if con.is_connected():
		cursor.close()
	else:
		pass 
	return records

def fetch(query,con):
	records = pd.read_sql(query,con)
	return records 

result1 = execute('select * from sql_hr.employees',hr_con)
result2 = fetch('select * from sql_hr.employees',hr_con)

print(result2)

