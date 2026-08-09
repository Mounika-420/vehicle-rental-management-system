import pymysql

class data_base:
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="Root@12345",
            database="vehicle_rental",
            charset="utf8"
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