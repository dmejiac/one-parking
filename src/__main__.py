from .models.estacionamiento import Estacionamiento
from .models.vehiculo import Vehiculo
from .models.solicitud import Solicitud
from .funciones.menu import mostrar_menu
import datetime
import os
import sqlite3


def main():
    """
    Inicio de la aplicación.
    """
    #estacionamiento = Estacionamiento()

    mostrar_menu()

    try:
        conn = sqlite3.connect("db_dev.db")
        cursor = conn.cursor()

        print('Fue creada la base de datos')
        print('Esta conectado a la base de datos')
    
        sql = 'SELECT sqlite_version();'
        cursor.execute(sql)
        resultado = cursor.fetchall()

        print()
        print('Versión SQLite:', resultado)

        cursor.close()

    except sqlite3.Error as error:
        print('Se ha producido un error:', error)


    finally:
        if conn:
            conn.close()
            print('\nLa conexión se ha cerrado de forma satisfactoria.')

if __name__ == '__main__':
    main()