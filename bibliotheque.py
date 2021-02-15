import livre
import reader
import mysql_methods

while True:
    user_input_1 = input('S.P.Q.R.\n'
                         '______________________________\n'
                         '1 - добавить книгу\n'
                         '2 - удалить книгу\n'
                         '3 - посмотреть полный список книг\n'
                         '4 - посмотреть список книг в наличии\n'
                         '5 - посмотреть список книг выданных читателям\n'
                         '6 - сортировка книг в картотеке\n'
                         '7 - выдать книгу читателю\n'
                         '8 - принять книгу от читателя\n'
                         '9 - добавить читателя\n'
                         '10 - посмотреть список читателей\n'
                         '11 - посмотреть карточку читателя\n'
                         '12 - посмотреть карточку книги\n'
                         '0 - выход из программы\n'
                         '______________________________\n'
                         'Ваш выбор: ')

    if user_input_1 == '1':
        new_livre = livre.Livre(0, '', '!', '', 1)
        mysql_methods.add_livre_data_base(new_livre.nom,
                                          new_livre.author,
                                          new_livre.year,
                                          new_livre.triger)

    elif user_input_1 == '2':
        user_input_2 = input('Введите id книги для удаления: ')
        while not user_input_2.isdigit():
            user_input_2 = input('Введите id книги для удаления: ')
        mysql_methods.delete_livre_data_base(int(user_input_2))

    elif user_input_1 == '3':
        print('\n______________________________\n'
              'Полная картотека книг:\n')
        for element in mysql_methods.get_all_livres_data_base():
            print(element)
        print('______________________________')

    elif user_input_1 == '4':
        print('\n______________________________\n'
              'Список книг в наличии:\n')
        for element in mysql_methods.get_all_livres_data_base():
            if element.triger == 1:
                print(element)
        print('______________________________')

    elif user_input_1 == '5':
        print('\n______________________________\n'
              'Список книг, выданных читателям:\n')
        for element in mysql_methods.get_all_livres_data_base():
            if element.triger == 0:
                print(element)
        print('______________________________')

    elif user_input_1 == '6':
        user_input_3 = input(
            'Сортировка по названию книги - нажмите 1\n'
            'Сортировка по автору книги - нажмите 2\n'
            'Сортировка по году издания книги - нажмите 3\n'
        )
        if user_input_3 == '1':
            print('\n______________________________\n'
                  'Список книг, отсортированных по названию книги:\n')
            for element in sorted(mysql_methods.get_all_livres_data_base(),
                                  key=lambda element: element.nom):
                print(element)
            print('______________________________')
        elif user_input_3 == '2':
            print('\n______________________________\n'
                  'Список книг, отсортированных по автору книги:\n')
            for element in sorted(mysql_methods.get_all_livres_data_base(),
                                  key=lambda element: element.author):
                print(element)
            print('______________________________')
        elif user_input_3 == '3':
            print('\n______________________________\n'
                  'Список книг, отсортированных по году издания книги:\n')
            for element in sorted(mysql_methods.get_all_livres_data_base(),
                                  key=lambda element: element.year):
                print(element)
            print('______________________________')

    elif user_input_1 == '7':
        user_input_4 = input('Введите id книги: ')
        while not user_input_4.isdigit():
            user_input_4 = input('Введите id книги: ')
        user_input_5 = input('Введите id читателя: ')
        while not user_input_5.isdigit():
            user_input_5 = input('Введите id читателя: ')

        current_livre = mysql_methods.select_livre(int(user_input_4))
        current_reader = mysql_methods.select_reader(int(user_input_5))
        if current_livre and current_reader:
            if current_livre['triger'] == 1:
                mysql_methods.ajouter_status_livre(int(user_input_4), 0)
                mysql_methods.envoyer_livre(current_livre, current_reader,
                                            'выдача книги')
            else:
                print('Книга уже выдана другому читателю!')

    elif user_input_1 == '8':
        user_input_4 = input('Введите id книги: ')
        while not user_input_4.isdigit():
            user_input_4 = input('Введите id книги: ')
        user_input_5 = input('Введите id читателя: ')
        while not user_input_5.isdigit():
            user_input_5 = input('Введите id читателя: ')

        current_livre = mysql_methods.select_livre(int(user_input_4))
        current_reader = mysql_methods.select_reader(int(user_input_5))
        if current_livre and current_reader:
            if current_livre['triger'] == 0:
                verification = \
                    mysql_methods.control_de_envoyer_livre(int(user_input_4))
                if verification[-1]['id_reader'] == int(user_input_5):
                    mysql_methods.ajouter_status_livre(int(user_input_4), 1)
                    mysql_methods.envoyer_livre(current_livre, current_reader,
                                                'прием книги')
                else:
                    print('У указанного читателя нет данной книги!')
            else:
                print('Книга находится в библиотеке!')

    elif user_input_1 == '9':
        new_reader = reader.Reader(0, '', '', '', '', '', '!', '')
        mysql_methods.add_reader_data_base(new_reader.nom,
                                           new_reader.prenom,
                                           new_reader.bth_jour,
                                           new_reader.bth_mois,
                                           new_reader.bth_an,
                                           new_reader.rue,
                                           new_reader.maison)

    elif user_input_1 == '10':
        print('\n______________________________\n'
              'Полная картотека читателей:\n')
        for element in mysql_methods.get_all_readers_data_base():
            print(element)
        print('______________________________')

    elif user_input_1 == '11':
        user_input_6 = input('Введите id читателя: ')
        while not user_input_6.isdigit():
            user_input_6 = input('Введите id читателя: ')
        current_reader = mysql_methods.get_info_de_reader(int(user_input_6))
        if current_reader:
            print('\n______________________________\n'
                  'КАРТОЧКА ЧИТАТЕЛЯ:\n')
            print(f'__//__ОСНОВНАЯ ИНФОРМАЦИЯ__//__\n'
                  f'id читателя: {current_reader["id читателя"]}\n'
                  f'фамилия: {current_reader["фамилия"]}\n'
                  f'имя: {current_reader["имя"]}\n'
                  f'улица: {current_reader["улица"]}\n'
                  f'№ дома: {current_reader["№ дома"]}\n\n'
                  f'__//__ИСТОРИЯ ОПЕРАЦИЙ__//__\n')
            for element in current_reader['история операций']:
                print(f'id операции: {element[0]}\n'
                      f'id книги: {element[1]}\n'
                      f'название книги: {element[2]}\n'
                      f'тип операции: {element[3]}\n'
                      f'дата/время: {element[4]}\n')

    elif user_input_1 == '12':
        user_input_6 = input('Введите id книги: ')
        while not user_input_6.isdigit():
            user_input_6 = input('Введите id читателя: ')
        current_livre = mysql_methods.get_info_de_livre(int(user_input_6))
        if current_livre:
            if current_livre["triger"] == 0:
                current_status = 'у читателя'
            else:
                current_status = 'в наличии'
            print('\n______________________________\n'
                  'КАРТОЧКА КНИГИ:\n')
            print(f'__//__ОСНОВНАЯ ИНФОРМАЦИЯ__//__\n'
                  f'id книги: {current_livre["id книги"]}\n'
                  f'название: {current_livre["название книги"]}\n'
                  f'автор: {current_livre["автор"]}\n'
                  f'год издания: {current_livre["год издания"]}\n'
                  f'статус: {current_status}\n\n'
                  f'__//__ИСТОРИЯ ОПЕРАЦИЙ__//__\n')
            for element in current_livre['история операций']:
                print(f'id операции: {element[0]}\n'
                      f'id читателя: {element[1]}\n'
                      f'фамилия читателя: {element[2]}\n'
                      f'имя читателя: {element[3]}\n'
                      f'тип операции: {element[4]}\n'
                      f'дата/время: {element[5]}\n')

    elif user_input_1 == '0':
        input('Нажмите Enter для выхода')
        break
