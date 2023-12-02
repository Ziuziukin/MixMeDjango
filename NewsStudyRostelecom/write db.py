import sqlite3


# создаем соединение с БД
def connect_db(name_cur):
    connection = sqlite3.connect('db.sqlite3')
    cur = connection.cursor()
    x = name_cur(cur)
    connection.commit()

#создаем таблицу берндов
def create_table_brands(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS brands(
                brandid INT PRIMARY KEY,
                name_brand TEXT,
                desc_brand TEXT,
                image_brand TEXT,
                site TEXT);""")

#создаем таблицу берндов
def create_table_tastes(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS tastes(
                tasteid INT PRIMARY KEY,
                name_taste TEXT,
                taste_rus TEXT,
                desc_taste TEXT,
                image_taste TEXT,
                strength_taste INT,
                brandid INT NOT NULL,
                FOREIGN KEY (brandid) REFERENCES brands(brandid);""")

def insert_db(cur):
    cur.execute("""INSERT INTO""")

x = connect_db(create_table_brands)
