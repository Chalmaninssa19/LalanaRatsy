import psycopg2

class Connection :
    def __init__(self):
        self.conn = None
        self.cur = None
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="lalanaratsy",
                user="postgres",
                password="postgres")
            return self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
    
    # def get_data(self):
    #     try:
    #         query = "SELECT * FROM DETAILSROUTE;"
    #         self.cur.execute(query)
    #         data = self.cur.fetchall()
    #         for i in data :
    #             print(i)
    #         # i=0
    #         # while i < data.length() :
    #         #     print(data[i])
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)