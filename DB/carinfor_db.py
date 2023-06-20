import mysql.connector
import pandas as pd

# CSV 파일을 데이터프레임으로 읽어오기
data = pd.read_csv(r'C:\Users\ii818\git\surinam3\DB\카정리.csv', encoding='utf-8')

print(data[:10])

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    user='root',
    password='123',
    database='carsuri'
)
cursor = conn.cursor()

# maker_table 생성
create_maker_table = '''
CREATE TABLE IF NOT EXISTS maker (
    maker_no INT PRIMARY KEY AUTO_INCREMENT,
    maker_name VARCHAR(255) UNIQUE
)
'''
cursor.execute(create_maker_table)

# model_table 생성
create_model_table = '''
CREATE TABLE IF NOT EXISTS model (
    model_no INT PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(255) UNIQUE,
    maker_num INT,
    FOREIGN KEY (maker_num) REFERENCES maker(maker_no)
)
'''
cursor.execute(create_model_table)

# detail_table 생성
create_detail_table = '''
CREATE TABLE IF NOT EXISTS detail (
    detail_no INT PRIMARY KEY AUTO_INCREMENT,
    detail_name VARCHAR(255),
    model_num INT,
    FOREIGN KEY (model_num) REFERENCES model(model_no)
)
'''
cursor.execute(create_detail_table)

# 데이터 저장
for index, row in data.iterrows():
    maker_name = row['maker']
    model_name = row['model']
    detail_name = row['detail']

    # maker_table에 데이터 삽입
    insert_maker_query = f"INSERT IGNORE INTO maker (maker_name) VALUES ('{maker_name}')"
    cursor.execute(insert_maker_query)

    # 삽입된 데이터의 maker_no 가져오기
    get_maker_id_query = f"SELECT maker_no FROM maker WHERE maker_name = '{maker_name}'"
    cursor.execute(get_maker_id_query)
    maker_id = cursor.fetchone()[0]

    # model_table에 데이터 삽입
    insert_model_query = f"INSERT IGNORE INTO model (model_name, maker_num) VALUES ('{model_name}', {maker_id})"
    cursor.execute(insert_model_query)

    # 삽입된 데이터의 model_no 가져오기
    get_model_id_query = f"SELECT model_no FROM model WHERE model_name = '{model_name}'"
    cursor.execute(get_model_id_query)
    model_id = cursor.fetchone()[0]

    # detail_table에 데이터 삽입
    insert_detail_query = f"INSERT INTO detail (detail_name, model_num) VALUES ('{detail_name}', {model_id})"
    cursor.execute(insert_detail_query)

# 변경사항 저장
conn.commit()

# 연결 종료
conn.close()