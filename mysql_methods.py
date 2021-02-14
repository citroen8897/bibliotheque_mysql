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
