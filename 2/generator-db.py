import random
import csv

# Tạo dữ liệu cho bảng TRUONG
truong_data = []
for i in range(100):
    truong_data.append([f'Truong{i+1}', f'Dia chi {i+1}'])

# Tạo dữ liệu cho bảng HS
hs_data = []
for i in range(1000000):
    hs_data.append([f'HS{i+1}', f'Lop {random.randint(1, 12)}'])

# Tạo dữ liệu cho bảng HOC
hoc_data = []
for hs_row in hs_data:
    for _ in range(random.randint(1, 3)):
        hoc_data.append([hs_row[0], f'Mon hoc {random.randint(1, 10)}'])

# Ghi dữ liệu vào các tệp CSV
with open('truong.csv', 'w', newline='') as truong_file:
    writer = csv.writer(truong_file)
    writer.writerow(['Ten truong', 'Dia chi'])
    writer.writerows(truong_data)

with open('hs.csv', 'w', newline='') as hs_file:
    writer = csv.writer(hs_file)
    writer.writerow(['Ten HS', 'Lop'])
    writer.writerows(hs_data)

with open('hoc.csv', 'w', newline='') as hoc_file:
    writer = csv.writer(hoc_file)
    writer.writerow(['Ten HS', 'Mon hoc'])
    writer.writerows(hoc_data)
