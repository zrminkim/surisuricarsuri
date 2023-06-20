import mysql.connector
import pandas as pd

# CSV 파일 경로
csv_file_path = 'data.csv'

# CSV 파일을 데이터프레임으로 읽어오기
df = pd.read_csv(r'C:\Users\ii818\git\surinam3\DB\filtered_data_repair(통합).csv', encoding='utf-8')
rp = pd.DataFrame(columns=['maker_num', 'model_num', 'detail_num', 'cost', 'exchange', 'repair'])

print(df[:10])
# 데이터베이스 연결
conn = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    user='root',
    password='123',
    database='carsuri'
)
cursor = conn.cursor()



# maker 테이블에서 데이터 읽어오기
cursor.execute("SELECT maker_no, maker_name FROM maker")
rows = cursor.fetchall()
maker_table = pd.DataFrame(rows, columns=['maker_no', 'maker_name'])

# 데이터프레임(df)에서 maker_name과 일치하는 maker_no로 치환
rp['maker_num'] = df['maker'].map(maker_table.set_index('maker_name')['maker_no'])


# model 테이블에서 데이터 읽어오기
cursor.execute("SELECT model_no, model_name FROM model")
rows = cursor.fetchall()
model_table = pd.DataFrame(rows, columns=['model_no', 'model_name'])

# 데이터프레임(df)에서 model_name과 일치하는 model_num으로 치환
rp['model_num'] = df['model'].map(model_table.set_index('model_name')['model_no'])


# detail 테이블에서 데이터 읽어오기
cursor.execute("SELECT detail_no, detail_name FROM detail")
rows = cursor.fetchall()
model_table = pd.DataFrame(rows, columns=['detail_no', 'detail_name'])

# 데이터프레임(df)에서 model_name과 일치하는 model_num으로 치환
rp['detail_num'] = df['detail'].map(model_table.set_index('detail_name')['detail_no'])
# "rp" 데이터프레임에 "cost", "exchange", "repair" 컬럼 추가
rp['cost'] = df['cost_total']
rp['exchange'] = df['exchange']
rp['repair'] = df['repair']

rp.to_csv('detest(수리견적).csv', encoding='utf-8-sig')

# db에 저장

# "repair_cost" 테이블 생성
create_table_query = """
CREATE TABLE IF NOT EXISTS repair_cost (
    repair_cost_no INT PRIMARY KEY AUTO_INCREMENT,
    maker_num INT(11),
    model_num INT(11),
    detail_num INT(11),
    cost INT(11),
    exchange VARCHAR(255),
    repair VARCHAR(255),
    FOREIGN KEY (maker_num) REFERENCES maker (maker_no),
    FOREIGN KEY (model_num) REFERENCES model (model_no),
    FOREIGN KEY (detail_num) REFERENCES detail (detail_no)
)
"""

# repair_cost 테이블 생성
cursor.execute(create_table_query)
# "rp" 데이터프레임의 값들을 "repair_cost" 테이블에 삽입
for row in rp.itertuples(index=False):
    cursor.execute("INSERT INTO repair_cost (maker_num, model_num, detail_num, cost, exchange, repair) VALUES (%s, %s, %s, %s, %s, %s)", row)


# 변경사항 저장
conn.commit()

# 연결 종료
conn.close()