import pymysql
conn = pymysql.Connect(
    host='192.168.50.68',
    port=3306,
    user='root',
    password='12345678',
    database='tpp',
    charset='utf8',
)

