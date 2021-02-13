import re


class Livre:
    def __init__(self, id_livre, nom, author, year, triger):
        self.id_livre = id_livre

        self.nom = nom
        while not re.findall(r'\w', self.nom):
            self.nom = (input('Введите название книги: ')).title()

        self.author = author
        while re.findall(r'[^a-zA-Zа-яА-Я, \s]', self.author):
            self.author = (input('Введите автора книги: ')).title()

        self.year = year
        while not self.year.isdigit() or len(self.year) != 4:
            self.year = input('Введите год издания книги: ')

        self.triger = triger

    def __str__(self):
        return f'id книги: {self.id_livre}\n' \
               f'Название книги: {self.nom}\n' \
               f'Автор: {self.author}\n' \
               f'Год издания: {self.year}\n'
