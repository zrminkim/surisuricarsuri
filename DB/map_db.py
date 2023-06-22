import mysql.connector
import pandas as pd
import csv

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    user='root',
    password='123',
    database='carsuri'
)
cursor = conn.cursor()
cursor = conn.cursor()

# CSV 파일 경로
csv_file = "../DB/map.csv"

# map_table 생성
create_maker_table = '''
CREATE TABLE IF NOT EXISTS map (
    map_no INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    addr VARCHAR(255),
    latitude DOUBLE,
    longitude DOUBLE,
    tel VARCHAR(13)
)
'''
cursor.execute(create_maker_table)


# CSV 파일 읽기
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    
    # 첫 번째 줄은 헤더로 처리
    header = next(reader)
    
    # 각 행에 대해 SQL 쿼리 실행
    for row in reader:
        name = row[0]
        addr = row[1]
        latitude_str = row[2]
        longitude_str = row[3]
        tel = row[4]
        
        # 빈 문자열인 경우에는 None으로 처리
        latitude = float(latitude_str) if latitude_str else None
        longitude = float(longitude_str) if longitude_str else None
        
        # SQL 쿼리 실행
        sql = "INSERT INTO map (name, addr, latitude, longitude, tel) VALUES (%s, %s, %s, %s, %s)"
        values = (name, addr, latitude, longitude, tel)
        cursor.execute(sql, values)

        
# 변경사항 커밋
conn.commit()

# 연결 닫기
cursor.close()
conn.close()