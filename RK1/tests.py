import unittest

from main import *

class TestMain(unittest.TestCase):
    Shops = [
        Shop(1, 'Достаевский'),
        Shop(2, 'Читай город'),
        Shop(3, 'Республика'),
        Shop(11, 'Фаланастер'),
        Shop(22, 'Московский дом книги'),
        Shop(33, 'Ноты'),
    ]
    Books = [
        Book(1, 'Герой нашего времен', 250, 1),
        Book(2, 'Мастер и маргарита', 350, 2),
        Book(3, 'Заводной апельсин', 450, 3),
        Book(4, 'Три товарища', 350, 3),
        Book(5, 'Портрет Дориана Грея', 250, 3),
    ]
    Books_Shops = [
        BookShop(1, 1),
        BookShop(2, 2),
        BookShop(3, 3),
        BookShop(3, 4),
        BookShop(3, 5),
        BookShop(11, 1),
        BookShop(22, 2),
        BookShop(33, 3),
        BookShop(33, 4),
        BookShop(33, 5),
    ]

    def test1(self):
        one_to_many = [(e.name_b, e.price, d.name)
                       for d in Shops
                       for e in Books
                       if e.Shop_id == d.id]
        self.assertEquals(B1(one_to_many), [('Герой нашего времен', 250, 'Достаевский'), ('Заводной апельсин', 450, 'Республика'), ('Три товарища', 350, 'Республика'), ('Портрет Дориана Грея', 250, 'Республика'), ('Мастер и маргарита', 350, 'Читай город')])

    def test2(self):
        one_to_many = [(e.name_b, e.price, d.name)
                       for d in Shops
                       for e in Books
                       if e.Shop_id == d.id]
        self.assertEquals(B2(one_to_many), [('Доставский', 1), ('Читай город', 1), ('Республика', 1)])

    def test3(self):
        many_to_many_tBook = [(d.name, ed.Shop_id, ed.Book_id)
                              for d in Shops
                              for ed in Books_Shops
                              if d.id == ed.Shop_id]
        many_to_many = [(e.name_b, e.price, Shop_name)
                        for Shop_name, Shop_id, Book_id in many_to_many_tBook
                        for e in Books if e.id == Book_id]
        self.assertEquals(B3(many_to_many), {'Мастер и маргарита': ['Читай город', 'Московский дом книги'], 'Заводной апельсин': ['Республика', 'Ноты'], 'Три товарища': ['Республика', 'Ноты'], 'Портрет Дориана Грея': ['Республика', 'Ноты']})

if __name__ == '__main__':
    unittest.main()