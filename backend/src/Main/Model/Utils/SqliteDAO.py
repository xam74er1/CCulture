import sqlite3
from sqlite3 import Error, Connection

from backend.src.Main.Model.Utils.Config import Config


class DAOConnextion :
    connextion : Connection = None

    def __init__(self):
        DAOConnextion.connextion = DAOConnextion.create_connection(Config.SQLITE_DATABASE_FILE)

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn : Connection = None
        try:
            print("Ouverture d'une bdd at "+db_file)
            conn = sqlite3.connect(db_file, check_same_thread=False)
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def select(string):
        if DAOConnextion.connextion == None:
            tmp = DAOConnextion()

        cur = DAOConnextion.connextion.cursor()
        cur.execute(string)
        return cur.fetchall()

    @staticmethod
    def select_random_country():
        return DAOConnextion.select("Select * from Country ORDER BY RANDOM() LIMIT 1;")


