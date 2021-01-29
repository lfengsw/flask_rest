import json
import pymysql

def json_to_database():
    conn = pymysql.Connect(
        host='192.168.50.68',
        port = 3306,
        user='root',
        password='12345678',
        database='flask_rest',
        charset='utf8',
    )
    cursor = conn.cursor()
    with open('city.json',encoding='utf-8') as f:
        data = json.load(f)
        info = data["returnValue"]
        letters = info.keys()
        for letter in letters:
            # 在字母数据表中插入数据
            cursor.execute("insert into letters(letter)values('{}')".format(letter))
            cursor.execute("select id from letters where letter='{}'".format(letter))
            letter_id_tuple = cursor.fetchone()
            cities = info[letter]
            for city in cities:
                city_id = city["id"]
                regionName = city["regionName"]
                cityCode = city["cityCode"]
                pinYin = city["pinYin"]
                citySQL = "insert into cities(id,regionName,cityCode,pinYin,letter_id)" \
                          "values({},'{}',{},'{}',{})".format(city_id,regionName,cityCode,pinYin,letter_id_tuple[0])
                # print("***************",citySQL)
                cursor.execute(citySQL)

        conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    json_to_database()
    print("脚本执行成功！")
