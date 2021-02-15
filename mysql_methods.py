import mysql.connector
from mysql.connector import Error
import livre
import reader


def add_livre_data_base(nom, author, year, triger):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            new_livre = "INSERT INTO livres(nom, author, year, triger) " \
                        "VALUES(%s,%s,%s,%s)"
            cursor = conn.cursor()
            cursor.execute(new_livre, (nom, author, year, triger))

            if cursor.lastrowid:
                print('успешно добавлена запись. id книги: ', cursor.lastrowid)
            else:
                print('какая-то ошибка...')

            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def delete_livre_data_base(id_livre):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            list_de_id = []
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM livres")
            row = cursor.fetchone()
            while row is not None:
                list_de_id.append(row[0])
                row = cursor.fetchone()
            if id_livre in list_de_id:
                delete_livre = f"DELETE FROM livres WHERE id = {id_livre}"
                cursor.execute(delete_livre)
                conn.commit()
                print('Книга успешно удалена из картотеки!')
            else:
                print('Книги с указанным id в картотеке нет!')

    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def get_all_livres_data_base():
    list_des_livres = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livres")
            row = cursor.fetchone()
            while row is not None:
                list_des_livres.append(livre.Livre(row[0], row[1], row[2],
                                                   row[3], row[4]))
                row = cursor.fetchone()

    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()

    return list_des_livres


def add_reader_data_base(nom, prenom, birth_jour, birth_mois, birth_an, rue,
                         maison):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            list_des_readers = []
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM readers")
            row = cursor.fetchone()
            while row is not None:
                list_des_readers.append([row[1], row[2], row[3], row[4],
                                         row[5]])
                row = cursor.fetchone()
            if [nom, prenom, birth_jour, birth_mois, birth_an] \
                    not in list_des_readers:
                new_reader = "INSERT INTO readers(nom, prenom, birth_jour, " \
                             "birth_mois, birth_an, rue, maison) " \
                             "VALUES(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(new_reader, (nom, prenom, birth_jour,
                                            birth_mois, birth_an, rue, maison))

                if cursor.lastrowid:
                    print('успешно добавлена запись. id читателя: ',
                          cursor.lastrowid)
                else:
                    print('какая-то ошибка...')
                conn.commit()
            else:
                print('Читатель с такими личными данными уже зарегистрирован!')
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def get_all_readers_data_base():
    list_des_readers = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM readers")
            row = cursor.fetchone()
            while row is not None:
                list_des_readers.append(reader.Reader(row[0], row[1], row[2],
                                                      row[3], row[4], row[5],
                                                      row[6], row[7]))
                row = cursor.fetchone()

    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()

    return list_des_readers


def select_livre(livre_id):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        current_livre = {}
        if conn.is_connected():
            list_de_id = []
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM livres")
            row = cursor.fetchone()
            while row is not None:
                list_de_id.append(row[0])
                row = cursor.fetchone()
            if livre_id in list_de_id:
                cursor.execute(f"SELECT * FROM livres WHERE id = {livre_id}")
                row = cursor.fetchone()
                while row is not None:
                    current_livre['id книги'] = row[0]
                    current_livre['название книги'] = row[1]
                    current_livre['triger'] = row[4]
                    row = cursor.fetchone()
            else:
                print('Книги с указанным id в картотеке нет!')

    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    return current_livre


def select_reader(reader_id):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        current_reader = {}
        if conn.is_connected():
            list_de_id = []
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM readers")
            row = cursor.fetchone()
            while row is not None:
                list_de_id.append(row[0])
                row = cursor.fetchone()
            if reader_id in list_de_id:
                cursor.execute(f"SELECT * FROM readers WHERE id = {reader_id}")
                row = cursor.fetchone()
                while row is not None:
                    current_reader['id читателя'] = row[0]
                    current_reader['фамилия'] = row[2]
                    current_reader['имя'] = row[1]
                    row = cursor.fetchone()
            else:
                print('Читателя с указанным id в картотеке нет!')

    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    return current_reader


def envoyer_livre(current_livre, current_reader, operation):
    id_livre = current_livre['id книги']
    nom_livre = current_livre['название книги']
    action = operation
    id_reader = current_reader['id читателя']
    prenom_reader = current_reader['фамилия']
    nom_reader = current_reader['имя']
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            print('Соединение с базой данных товаров установлено....')
            new_position = "INSERT INTO History_de_bibliotheque(" \
                           "id_livre, nom_livre, " \
                           "id_reader, prenom_reader, nom_reader, " \
                           "action) VALUES(%s,%s,%s,%s,%s,%s)"
            cursor = conn.cursor()
            cursor.execute(new_position, (id_livre, nom_livre, id_reader,
                                          prenom_reader, nom_reader, action))

            if cursor.lastrowid:
                print('успешно добавлена запись. id - >', cursor.lastrowid)
            else:
                print('какая-то ошибка...')

            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def ajouter_status_livre(livre_id, livre_status):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            new_status = f"UPDATE livres SET triger = {livre_status} " \
                         f"WHERE id = {livre_id}"
            cursor = conn.cursor()
            cursor.execute(new_status)
            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()


def control_de_envoyer_livre(id_livre):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM History_de_bibliotheque WHERE "
                           f"id_livre = {id_livre}")
            row = cursor.fetchone()
            temp_list = []
            while row is not None:
                temp_list.append({'id_reader': row[3], 'action': row[6]})
                row = cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    return temp_list
