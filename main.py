import sqlalchemy
import datetime
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale

with open('engine_db.txt', 'r', encoding='utf-8') as file:
    login = file.readline().strip()
    password = file.readline().strip()
    db_name = file.readline().strip()

DSN = f"postgresql://{login}:{password}@localhost:5432/{db_name}?client_encoding=utf8"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

# Наполнение таблицы (Авторы)

Murakami = Publisher(name="Харуки Мураками", id=1)
Martin = Publisher(name="Джордж Р. Р. Мартин", id=2)
Rowling = Publisher(name="Джоан Роулинг", id=3)
Atwood = Publisher(name="Маргарет Этвуд", id=4)
Ferrante = Publisher(name="Элена Ферранте", id=5)
King = Publisher(name="Стивен Кинг", id=6)
Mitchell = Publisher(name="Дэвид Митчелл", id=7)
Coelho = Publisher(name="Пауло Коэльо", id=8)
Harari = Publisher(name="Юваль Ной Харари", id=9)
Adichie = Publisher(name="Чимаманда Нгози Адичи", id=10)

session.add_all([Murakami,
                 Martin,
                 Rowling,
                 Atwood,
                 Ferrante,
                 King,
                 Mitchell,
                 Coelho])
session.commit()

# Наполнение таблицы (Книги)

Norwegian_Wood = Book(title="Норвежский лес", id_publisher=1)
Kafka_on_the_Shore = Book(title="Кафка на пляже", id_publisher=1)
IQ84 = Book(title="1Q84", id_publisher=1)

Game_of_Thrones = Book(title="Игра престолов", id_publisher=2)
Clash_of_Kings = Book(title="Битва королей", id_publisher=2)

Harry_Potter_and_the_Sorcerers_Stone = Book(title="Гарри Поттер и философский камень", id_publisher=3)
Harry_Potter_and_the_Chamber_of_Secrets = Book(title="Гарри Поттер и тайная комната", id_publisher=3)

Handmaids_Tale = Book(title="Рассказ служанки", id_publisher=4)

My_Brilliant_Friend = Book(title="Моя гениальная подруга", id_publisher=5)

It = Book(title="Оно", id_publisher=6)
The_Shining = Book(title="Сияние", id_publisher=6)

Cloud_Atlas = Book(title="Облачный атлас", id_publisher=7)

The_Alchemist = Book(title="Алхимик", id_publisher=8)

session.add_all([Norwegian_Wood,
                 Kafka_on_the_Shore,
                 IQ84,
                 Game_of_Thrones,
                 Clash_of_Kings,
                 Harry_Potter_and_the_Sorcerers_Stone,
                 Harry_Potter_and_the_Chamber_of_Secrets,
                 Handmaids_Tale,
                 My_Brilliant_Friend,
                 It,
                 The_Shining,
                 Cloud_Atlas,
                 The_Alchemist,
                ])
session.commit()

Bukvoed = Shop(name="Буквоед")
Labirint = Shop(name="Лабиринт")
Knizhny_Dom = Shop(name="Книжный дом")
Chitai_Gorod = Shop(name="Читай-город")

session.add_all([Bukvoed, Labirint, Knizhny_Dom, Chitai_Gorod])

session.commit()

Norwegian_Wood1 = Stock(id_book=1, id_shop=1, count=34)

Kafka_on_the_Shore1 = Stock(id_book=2, id_shop=2, count=21)
Kafka_on_the_Shore2 = Stock(id_book=2, id_shop=3, count=16)

IQ841 = Stock(id_book=3, id_shop=1, count=23)

Game_of_Thrones1 = Stock(id_book=4, id_shop=1, count=19)
Game_of_Thrones2 = Stock(id_book=4, id_shop=2, count=14)
Game_of_Thrones3 = Stock(id_book=4, id_shop=3, count=16)

Clash_of_Kings1 = Stock(id_book=5, id_shop=2, count=8)

Harry_Potter_and_the_Sorcerers_Stone1 = Stock(id_book=6, id_shop=1, count=19)
Harry_Potter_and_the_Sorcerers_Stone2 = Stock(id_book=6, id_shop=3, count=21)

Harry_Potter_and_the_Chamber_of_Secrets1 = Stock(id_book=7, id_shop=1, count=38)
Harry_Potter_and_the_Chamber_of_Secrets2 = Stock(id_book=7, id_shop=2, count=9)
Harry_Potter_and_the_Chamber_of_Secrets3 = Stock(id_book=7, id_shop=3, count=17)

Handmaids_Tale1 = Stock(id_book=8, id_shop=2, count=10)

My_Brilliant_Friend1 = Stock(id_book=9, id_shop=3, count=11)

It1 = Stock(id_book=10, id_shop=1, count=15)
It2 = Stock(id_book=10, id_shop=2, count=13)
The_Shining1 = Stock(id_book=11, id_shop=1, count=20)
The_Shining2 = Stock(id_book=11, id_shop=2, count=7)
The_Shining3 = Stock(id_book=11, id_shop=3, count=18)

Cloud_Atlas1 = Stock(id_book=12, id_shop=1, count=12)
Cloud_Atlas2 = Stock(id_book=12, id_shop=2, count=15)

The_Alchemist1 = Stock(id_book=13, id_shop=3, count=14)

session.add_all([
    Norwegian_Wood1,
    Kafka_on_the_Shore1,
    Kafka_on_the_Shore2,
    IQ841, Game_of_Thrones1,
    Game_of_Thrones2,
    Game_of_Thrones3,
    Clash_of_Kings1,
    Harry_Potter_and_the_Sorcerers_Stone1,
    Harry_Potter_and_the_Sorcerers_Stone2, Harry_Potter_and_the_Chamber_of_Secrets1,
    Harry_Potter_and_the_Chamber_of_Secrets2,
    Harry_Potter_and_the_Chamber_of_Secrets3,
    Handmaids_Tale1,
    My_Brilliant_Friend1,
    It1,
    It2,
    The_Shining1,
    The_Shining2,
    The_Shining3,
    Cloud_Atlas1,
    Cloud_Atlas2,
    The_Alchemist1,
])

session.commit()

sale1 = Sale(price=999, date_sale=datetime.datetime(2024, 9, 20), id_stock=1, count=1)
sale2 = Sale(price=1099, date_sale=datetime.datetime(2024, 7, 24), id_stock=4, count=2)
sale3 = Sale(price=1299, date_sale=datetime.datetime(2020, 5, 17), id_stock=5, count=1)
sale4 = Sale(price=899, date_sale=datetime.datetime(2022, 2, 8), id_stock=7, count=3)
sale5 = Sale(price=1199, date_sale=datetime.datetime(2021, 1, 21), id_stock=9, count=1)
sale6 = Sale(price=1399, date_sale=datetime.datetime(2023, 12, 3), id_stock=10, count=8)
sale7 = Sale(price=899, date_sale=datetime.datetime(2018, 6, 5), id_stock=11, count=5)
sale8 = Sale(price=799, date_sale=datetime.datetime(2022, 7, 27), id_stock=13, count=2)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8])
session.commit()


def get_shop(res_):
    query = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
             .select_from(Publisher).join(Book, Book.id_publisher == Publisher.id)
             .join(Stock, Book.id == Stock.id_book)
             .join(Shop, Stock.id_shop == Shop.id)
             .join(Sale, Stock.id == Sale.id_stock))

    if res_.isdigit():
        query = query.filter(Publisher.id == int(res_))
    else:
        query = query.filter(Publisher.name.ilike(f'%{res_.strip()}%'))
    results = query.all()
    print('Информация о продажах книг в книжных магазинах: ')
    for title, name, price, date_sale in results:
        print(f'{title} | {name} | {price} | {date_sale}')


if __name__ == "__main__":
    res_ = input('Введите id или имя автора: ')
    get_shop(res_)

session.close()
