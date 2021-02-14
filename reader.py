import re


class Reader:
    def __init__(self, id_reader, nom, prenom, bth_jour, bth_mois, bth_an,
                 rue, maison):
        self.id_reader = id_reader

        self.nom = nom
        while not self.nom.isalpha():
            self.nom = input('Введите имя: ').title()

        self.prenom = prenom
        while not self.prenom.isalpha():
            self.prenom = input('Введите фамилию: ').title()

        self.bth_jour = bth_jour
        while not self.bth_jour.isdigit() or int(self.bth_jour) not in \
                range(1, 32):
            self.bth_jour = input('Введите день рождения: ')
        self.bth_jour = int(self.bth_jour)

        self.bth_mois = bth_mois
        while not self.bth_mois.isdigit() or int(self.bth_mois) not in \
                range(1, 13):
            self.bth_mois = input('Введите месяц рождения: ')
        self.bth_mois = int(self.bth_mois)

        self.bth_an = bth_an
        while not self.bth_an.isdigit() or len(self.bth_an) != 4:
            self.bth_an = input('Введите год рождения: ')
        self.bth_an = int(self.bth_an)

        self.rue = rue
        while re.findall(r'[^a-zA-Zа-яА-Я0-9, \s]', self.rue):
            self.rue = input('Введите название улицы: ')

        self.maison = maison
        while not self.maison.isdigit():
            self.maison = input('Введите номер дома: ')
        self.maison = int(self.maison)

    def __str__(self):
        return f'id читателя: {self.id_reader}\n' \
               f'имя: {self.nom}\n' \
               f'фамилия: {self.prenom}\n'
