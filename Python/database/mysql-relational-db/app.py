import pymysql

def get_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             database='movie',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

def get_imdb_list():
    
    connection = get_connection()
    try:
       cur=connection.cursor()
       movie_list=cur.execute("SELECT * from imdb")
       return cur.fetchall()
    finally:
       connection.close()
       
result = get_imdb_list()
for movie in result:
    print(f" movie:{movie["name"]}- year:{movie["year"]}")