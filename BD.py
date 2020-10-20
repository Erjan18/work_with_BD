import _sqlite3
connection = _sqlite3.connect('test.db')
import pprint

cursor = connection.cursor()

# sql_command = """CREATE TABLE salary(
# staff_id INTEGER PRIMARY KEY,
# full_name VARCHAR(50),
# staff_salary INTEGER(20),
# join_date DATE);"""

cursor.execute("INSERT INTO salary VALUES(1,'Erjan',50000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(2,'Alina',60000,'2020-10-10')")
cursor.execute("INSERT INTO salary  VALUES(3,'Baistan',70000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(4,'Erlan',90000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(5,'Tima',80000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(6,'Danil',520000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(7,'Sasha',510000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(8,'Aiba',540000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(9,'Era',550000,'2020-10-10')")
cursor.execute("INSERT INTO salary VALUES(10,'Puma',250000,'2020-10-10')")

cursor.execute("SELECT * FROM staff_salary")

ans = cursor.fetchall()
pprint.pprint(ans)

connection.commit()
connection.close()