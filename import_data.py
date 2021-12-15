import pandas as pd

data = pd.read_csv ('PoinsBlona.csv')   
df = pd.DataFrame(data)

import pyodbc

cursor = conn.cursor()

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO measurements (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
conn.commit()