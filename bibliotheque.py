import livre
import mysql_methods

while True:
    user_input_1 = input('S.P.Q.R.\n'
                         '______________________________\n'
                         '1 - добавить книгу\n'
                         '2 - удалить книгу\n'
                         '3 - посмотреть полный список книг\n'
                         '4 - посмотреть список книг в наличии\n'
                         '5 - посмотреть список книг выданных читателям\n'
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