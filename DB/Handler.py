import sqlite3


class dbHandler:
    def __init__(self,dbPath):
        self.path=dbPath
        self.conn = None

    def getPath(self):
        return self.path

    def connect(self):
        try:
            conn = sqlite3.connect(self.path)
            self.conn = conn#.cursor()
            return self.conn
        except Exception as e:
            print('connection error: ', e)
            return -1

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Done and disconnected from database")

    def select(self, query, values=None):
        cur = self.conn.cursor()
        if values == None:
            cur.execute(query)
        else:
            cur.executemany(query, values)
        self.conn.commit()
        rs = cur.fetchall()
        self.disconnect()
        return rs





