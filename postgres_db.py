import psycopg2 as psy
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2, depth=4)

conn = psy.connect(database="red30",
                   user="postgres",
                   password="postgres",
                   host="localhost",
                   port="5432")

cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Sales 
    (ORDER_NUM INT PRIMARY KEY,
        ORDER_TYPE TEXT,
        CUST_NAME TEXT,
        PROD_NUMBER TEXT,
        PROD_NAME TEXT,
        QUANTITY INT,
        PRICE REAL,
        DISCOUNT REAL,
        ORDER_TOTAL REAL
    );
    """
)

conn.commit()

# Insert an entry
cursor.execute(
    """INSERT INTO Sales
    (ORDER_NUM,
    ORDER_TYPE,
    CUST_NAME,
    PROD_NUMBER,
    PROD_NAME,
    QUANTITY,
    PRICE,
    DISCOUNT,
    ORDER_TOTAL) VALUES
    (1105910, 'Retail', 'Syman Mapstone', 'EB521',
    'Understanding Artificial Intelligence', 3, 19.5, 0, 58.5)
    """
)

conn.commit()

# Query a specific entry
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL FROM Sales WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
for row in rows:
    print("CUST_NAME=", row[0])
    print("ORDER_TOTAL=", row[1])

# Query some entries
# cursor.execute("SELECT * FROM sales LIMIT 10")
# pp.pprint(cursor.fetchall())

conn.close()
