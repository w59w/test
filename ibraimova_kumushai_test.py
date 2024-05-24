import sqlite3

conn = sqlite3.connect('exam.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100)
    )
''')

def display_stores():
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из "
          "программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def display_products(store_id):
    cursor.execute("SELECT products.title, categories.title, products.unit_price, products.stock_quantity "
                   "FROM products INNER JOIN categories ON products.category_code = categories.code "
                   "WHERE products.store_id = ?", (store_id,))
    products = cursor.fetchall()
    for product in products:
        print("Название продукта:", product[0])
        print("Категория:", product[1])
        print("Цена:", product[2])
        print("Количество на складе:", product[3])
        print()

while True:
    display_stores()
    store_id = input("Введите id магазина (0 для выхода): ")
    if store_id == '0':
        break
    else:
        try:
            store_id = int(store_id)
            cursor.execute("SELECT * FROM store WHERE store_id = ?", (store_id,))
            store = cursor.fetchone()
            if store:
                display_products(store_id)
            else:
                print("Магазин с указанным id не найден.")
        except ValueError:
            print("Введите целое число.")

conn.close()
