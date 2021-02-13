import mysql.connector
from mysql.connector import Error
import livre


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
