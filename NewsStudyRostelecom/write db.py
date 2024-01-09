import sqlite3
import xlrd


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

#загрузка данных в таблицу брендов
def loads_brands():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Путь к файлу Excel
    file_path = 'temp_db/brand_name.xls'

    # Откройте файл Excel
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    # Прочитайте и залейте данные
    for row in range(1, sheet.nrows):  # Пропустите заголовок
        id = sheet.cell_value(row, 0)
        brand_name = sheet.cell_value(row, 1)
        site_brand = sheet.cell_value(row, 2)
        brand_author_id = sheet.cell_value(row, 3)
        brand_image = sheet.cell_value(row, 4)
        desc_brand = sheet.cell_value(row, 5)

        # Выполните INSERT-запрос
        cursor.execute("INSERT INTO main_brands (id, brand_name, site_brand, brand_author_id, brand_image, desc_brand) VALUES (?, ?, ?, ?, ?, ?)", (id, brand_name, site_brand, brand_author_id, brand_image, desc_brand))

    conn.commit()
    conn.close()


# загрузка данных в таблицу вкусов
def loads_tastes():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Путь к файлу Excel
    file_path = 'temp_db/taste.xls'

    # Откройте файл Excel
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    # Прочитайте и залейте данные
    for row in range(1, sheet.nrows):  # Пропустите заголовок
        id = sheet.cell_value(row, 0)
        name_taste = sheet.cell_value(row, 1)
        taste_rus = sheet.cell_value(row, 2)
        desc_taste = sheet.cell_value(row, 3)
        strength_taste = sheet.cell_value(row, 4)
        brand_id_id = sheet.cell_value(row, 5)
        taste_image = sheet.cell_value(row, 6)

        # Выполните INSERT-запрос
        cursor.execute(
            "INSERT INTO main_tastes (id, name_taste, taste_rus, desc_taste, strength_taste, brand_id_id, taste_image) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id, name_taste, taste_rus, desc_taste, strength_taste, brand_id_id, taste_image))

    conn.commit()
    conn.close()

# x = connect_db(create_table_brands)

#x = loads_tastes()