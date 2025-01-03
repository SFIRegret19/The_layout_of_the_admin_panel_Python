import sqlite3
# import texts
# from config import priceSu, priceB, priceP, priceSh
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Пицца', f'{texts.Pizza_text}', f'{priceP}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Суши', f'{texts.Sushi_text}', f'{priceSu}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Бургер', f'{texts.Burger_text}', f'{priceB}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Шаурма', f'{texts.Shaurma_text}', f'{priceSh}'))

def get_all_products():
    initiate_db()
    cursor.execute(" CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")
    cursor.execute("SELECT title, description, price FROM Products")
    all_products = cursor.fetchall()
    return all_products

if __name__ == "__main__":
    connection.commit()
    connection.close()