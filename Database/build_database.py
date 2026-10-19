import sqlite3
from zipfile import ZipFile
from schema import create_tables
from fill_database import fill_tables

connection = sqlite3.connect('f1.db')

def main():
    try:
        create_tables(connection)

        print('Обновляем таблицы и вносим данные...')

        with ZipFile('source_csv.zip') as archive:
            fill_tables(connection, archive)

        connection.commit()

        print('База данных обновлена')

    except Exception as e:
        connection.rollback()
        print(f'!!! Произошла ошибка. {e} !!!')

    finally:
        connection.close()

if __name__ == '__main__':
    main()