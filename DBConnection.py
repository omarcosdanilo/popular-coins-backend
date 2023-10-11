import sqlite3


class DBConnection:
    def __init__(self, db_name):
        self.__connection = sqlite3.connect(
            f"""{db_name}.db""", check_same_thread=False
        )
        self.__cursor = self.__connection.cursor()
        print("DB Init")

    def create_table(self):
        try:
            self.__cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS coins(
                id TEXT,
                name TEXT,
                symbol TEXT,
                icon TEXT,
                price TEXT,
                total_score REAL,
                number_of_reviews INTEGER
                );
                """
            )
            self.__connection.commit()
            print("coins created")
        except sqlite3.Error as error:
            print("Error occurred: ", error)

    def insert_data(self, value):
        sql = """
                INSERT INTO coins
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        try:
            self.__cursor.execute(sql, tuple(value[k] for k in value))
            self.__connection.commit()

            print(value["name"] + " Inserido")
        except sqlite3.Error as error:
            print("Error occurred: ", error)
