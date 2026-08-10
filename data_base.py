import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self.conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
            charset="utf8",
            connect_timeout=30
        )

    def register(self, qry):
        con = self.conn
        cursor = con.cursor()
        cursor.execute(qry)
        con.commit()
        return "null"

    def show(self, qry):
        con = self.conn
        cursor = con.cursor()
        cursor.execute(qry)
        data = cursor.fetchall()
        return data

    def delete(self, qry):
        con = self.conn
        cursor = con.cursor()
        cursor.execute(qry)
        con.commit()
        con.close()
        return "null"