import random
import csv
import pandas as pd
import json
import mysql.connector

# Tạo dữ liệu cho bảng TRUONG


# Đường dẫn tới tệp Excel nguồn dữ liệu
excel_file = "C:\\Users\\buivu\\OneDrive\\Desktop\\đồ án 2\\danh-sach-truong-thpt-o-tphcm.xlsx"

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(excel_file)

# Lấy dữ liệu từ cột MATR trong tệp Excel
matr_data = df['MATR'].tolist()
tentr_data= df['TENTR'].tolist()
dchitr_data= df['DCHITR'].tolist()

# Tạo dữ liệu cho bảng TRUONG
truong_data = []
for matr, tentr, dchitr in zip(matr_data, tentr_data, dchitr_data):
    truong_data.append([matr, tentr, dchitr])

# Ghi dữ liệu vào tệp CSV
with open('truong.csv', 'w', newline='', encoding='utf-8') as truong_file:
    writer = csv.writer(truong_file)
    writer.writerow(['MATR', 'TENTR', 'DCHITR'])
    writer.writerows(truong_data)


# Sửa xong bảng TRUONG



# Tạo dữ liệu cho bảng HS
hs_data = []
for i in range(1000000):
    hs_data.append([f'HS{i+1}', f'Lop {random.randint(1, 12)}'])



# Ghi dữ liệu vào các tệp CSV

with open('hs.csv', 'w', newline='') as hs_file:
    writer = csv.writer(hs_file)
    writer.writerow(['Ten HS', 'Lop'])
    writer.writerows(hs_data)



# Tạo dữ liệu cho bảng HOC
hoc_data = []
for hs_row in hs_data:
    for _ in range(random.randint(1, 3)):
        hoc_data.append([hs_row[0], f'Mon hoc {random.randint(1, 10)}'])



# Ghi dữ liệu vào các tệp CSV

with open('hoc.csv', 'w', newline='') as hoc_file:
    writer = csv.writer(hoc_file)
    writer.writerow(['Ten HS', 'Mon hoc'])
    writer.writerows(hoc_data)




# Đọc thông tin xác thực từ file cấu hình
with open('config.json') as config_file:
    config = json.load(config_file)



# Thiết lập kết nối với cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)



# Tạo con trỏ để thực hiện các truy vấn
cursor = conn.cursor()



# Chuyển dữ liệu từ tệp CSV vào bảng TRUONG
with open('truong.csv', 'r') as truong_file:
    truong_data = csv.reader(truong_file)
    next(truong_data)  # Bỏ qua dòng tiêu đề
    cursor.executemany('INSERT INTO TRUONG (matr, tentr, dchitr) VALUES (%s, %s, %s)', truong_data)



# Chuyển dữ liệu từ tệp CSV vào bảng HS
with open('hs.csv', 'r') as hs_file:
    hs_data = csv.reader(hs_file)
    next(hs_data)  # Bỏ qua dòng tiêu đề
    cursor.executemany('INSERT INTO HS (mahs, ho, ten, cccd, ntns, dchi_hs) VALUES (%s, %s ,%s ,%s ,%s , %s)', hs_data)



# Chuyển dữ liệu từ tệp CSV vào bảng HOC
with open('hoc.csv', 'r') as hoc_file:
    hoc_data = csv.reader(hoc_file)
    next(hoc_data)  # Bỏ qua dòng tiêu đề
    cursor.executemany('INSERT INTO HOC (matr, mahs, namhoc, diemtb, xeploai, ketqua) VALUES (%s, %s ,%s ,%s ,%s , %s)', hoc_data)




# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()




# Đóng kết nối và con trỏ
cursor.close()
conn.close()
