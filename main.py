import mysql.connector

connection = mysql.connector.connect(
    user = 'root', 
    database = 'new_schema', 
    password = 'PanoramaIsland1535649*')

 

connection.close()