import _sqlite3
connection = _sqlite3.connect('test.db')

cursor = connection.cursor()

# sql_command = """CREATE TABLE products(
# product_id INTEGER PRIMARY KEY,
# product_name varcher(20),
# product_description varchar(50),
# customer varchar (20),
# pub_date DATE);"""



# sql_command = """INSERT INTO products VALUES(3,'Iphone 12','no commet','Erjan','2020-10-19');"""
# cursor.execute(sql_command)

cursor.execute("SELECT * FROM products WHERE product_name='Apple Watch'")
ans = cursor.fetchall()
print(ans)

connection.commit()
connection.close()