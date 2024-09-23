import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class Publisher(Base):
    """
    The class representing a book publisher.

    Attributes:
        id (int): The unique ID of the publisher.
        name (str): The name of the publisher, unique for each publisher.
        books (relationship): A relationship with books published by this publisher.
    """

    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=48), unique=True)
    books = relationship("Book", back_populates='publishers', cascade="all, delete-orphan")

    def __str__(self):
        return f'Publisher:\n\tid - {self.id}\n\tname - {self.name}\n'


class Book(Base):
    """
    The class representing the book.

    Attributes:
        id (int): The unique identifier of the book.
        title (str): The title of the book.
        id_publisher (int): ID of the publisher who owns the book.
        publishers (relationship): The relationship with the publisher who released this book.
        stocks (relationship): The relationship with the stocks of books in stores.
    """

    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=48), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publishers = relationship("Publisher", back_populates='books')

    stocks = relationship("Stock", back_populates='books', cascade="all, delete-orphan")


class Shop(Base):
    """
    The class representing a bookstore.

    Attributes:
        id (int): The unique identifier of the store.
        name (str): The name of the store.
        stocks (relationship): A relationship with the stocks of books available in this store.
    """

    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=48), nullable=False)

    stocks = relationship("Stock", back_populates="shops", cascade="all, delete-orphan")


class Stock(Base):
    """
    The class representing the stock of books in the store.

    Attributes:
        id (int): The unique identifier of the stock.
        id_book (int): ID of the book that is in stock.
        id_shop (int): ID of the store where the book stock is stored.
        count (int): The number of books of this type in stock.
        books (relationship): A relationship with a book that is in stock.
        shops (relationship): The relationship with the store that has this stock.
        sales (relationship): The relationship with the sales of a given stock.
    """

    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship("Book", back_populates="stocks")
    shops = relationship("Shop", back_populates="stocks")

    sales = relationship("Sale", back_populates="stocks")


class Sale(Base):
    """
    The class representing a record of a book sale.

    Attributes:
        id (int): The unique identifier of the sale.
        price (int): The sale price of the book.
        date_sale (date): The date the book was sold.
        id_stock (int): ID of the stock from which the book was sold.
        count (int): The number of books sold in this sale.
        stocks (relationship): The relationship with the inventory directory to which the sale relates.
    """

    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship("Stock", back_populates="sales")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
