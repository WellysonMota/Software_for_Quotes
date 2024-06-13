import mysql.connector
from mysql.connector import Error

def connect_to_database(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Substitua 'your_host', 'your_username', 'your_password', e 'database_name' pelos seus dados reais
host_name = "localhost"
user_name = "root"
user_password = "Motta1993!"
db_name = "mydb"

connection = connect_to_database(host_name, user_name, user_password, db_name)