import csv
import pandas as pd
import json
import mysql.connector
from faker import Faker
import random
from random import choice
from collections import Counter
from datetime import date, timedelta


#  bảng TRUONG

# Đường dẫn tới tệp Excel nguồn dữ liệu
excel_file = "C:\\Users\\buivu\\OneDrive\\Desktop\\đồ án 2\\danh-sach-truong-thpt-o-tphcm.xlsx"

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(excel_file)

# Lấy dữ liệu từ cột MATR trong tệp Excel
matr_data = df['MATR'].astype(int).apply(lambda x: str(x).zfill(3)).tolist()
tentr_data = df['TENTR'].tolist()
dchitr_data = df['DCHITR'].tolist()

# Tạo dữ liệu cho bảng TRUONG
truong_data = []
for matr, tentr, dchitr in zip(matr_data, tentr_data, dchitr_data):
    truong_data.append([matr, tentr, dchitr])

# Ghi dữ liệu vào tệp CSV
with open('truong.csv', 'w', newline='', encoding='utf-8') as truong_file:
    writer = csv.writer(truong_file)
    writer.writerow(['MATR', 'TENTR', 'DCHITR'])
    writer.writerows(truong_data)

# bảng HS


# Tạo dữ liệu cho bảng HS
fake = Faker('vi_VN')
ho_list={ 'Trần', 'Hoàng','Trương', 'Lý', 'Vương', 'Ngô', 'Lưu', 'Thái', 'Dương', 'Từ', 'Tôn', 'Mã', 'Châu', 'Hồ', 'Quách', 'Hà', 'Cao', 'Lâm', 'La', 'Trịnh', 'Lương', 'Hàn', 'Chu', 'Triệu', 'Nguyễn', 'Lê', 'Vũ', 'Võ', 'Đường', 'Đinh', 'Đoàn', 'Trịnh', 'Đào', 'Phạm', 'Phùng', 'Mai', 'Tô', 'Phí', 'Tạ', 'Thân', 'Lâm', 'Tống', 'Hoa', 'Từ', 'Thường', 'Tiêu', 'Ngọ', 'Kim', 'Tôn Thất', 'Triệu', 'Mạc', 'Thái', 'Thạch', 'Quách', 'Đàm', 'Đồng Văn', 'Huỳnh', 'Phan', 'Đặng', 'Bùi', 'Hồ', 'Đỗ', 'Âu Dương', 'Dư', 'Nghiêm', 'Viên', 'Ma', 'Mạch', 'Lỗ', 'Tiêu', 'Thẩm', 'Trình', 'Uông', 'Ung', 'Ưng', 'Vi', 'Văn', 'Yên', 'Nhâm', 'Doãn', 'Chung', 'Cáp', 'Ái Tân Giác La', 'Thành Cát', 'Mãn', 'Nỗ Nhĩ ', 'Lã', 'Khuất', 'Khúc', 'Khâu', 'Khổng', 'Kha', 'Hứa', 'Cáp', 'Bế', 'Bầnh', 'Chiêm', 'Chế', 'Cồ', 'Cổ', 'Phó', 'Hạ', 'Hầu', 'Kiều', 'Tùy', 'Lục', 'Đồng ', 'Đổng' }
ten_list={ 'Trung', 'Quân', 'Hải', 'Đức', 'Ân', 'An', 'Thịnh', 'Linh', 'Hiếu', 'Quốc', 'Duy', 'Tuấn', 'Tân', 'Đăng', 'Nam', 'Thành', 'Việt', 'Khánh', 'Vũ', 'Phong', 'Cường', 'Tâm', 'Nhật', 'Sơn', 'Phúc', 'Thái', 'Lâm', 'Tấn', 'Ngọc', 'Đạt', 'Hiệp', 'Tài', 'Dũng', 'Hồng', 'Huy', 'Hà', 'Khải', 'Thiện', 'Nghĩa ', 'Vương', 'Tiến', 'Vinh', 'Hoàng', 'Đông ', 'Nhân', 'Khắc', 'Thanh', 'Tùng', 'Thắng', 'Hùng', 'Bình', 'Trí', 'Kiên', 'Tuệ', 'Hào', 'Thế', 'Thiên', 'Vĩ', 'Hoa', 'Dương', 'Quang', 'Sỹ', 'Lượng', 'Xuân', 'Phương', 'Tú', 'Tuyến', 'Tuyết', 'Long', 'Hưng', 'Hòa', 'Khoa', 'Khôi', 'Khang', 'Nhất', 'Nhị', 'Tam', 'Tứ', 'Ngũ', 'Lục', 'Liên', 'Kim', 'Chung', 'Nhựt', 'Ưng', 'Thắm', 'Quỳnh', 'Giang', 'Quế', 'Quy', 'Quyết', 'Thất', 'Bát', 'Cửu', 'Tây', 'Bắc', 'Tông', 'Tín', 'Kỳ', 'Thư', 'Cát', 'Tường', 'Kiều', 'Anh', 'Tuyền', 'Mĩ', 'Pháp', 'Vân', 'Văn'}
phuong_quan = {
    'Quận 1': ['Phường Tân Định','Phường Cầu Kho','Phường Cầu Ông Lãnh', 'Phường Cô Giang','Phường Nguyễn Cư Trinh', 'Phường Đa Kao', 'Phường Bến Nghé', 'Phường Bến Thành', 'Phường Nguyễn Thái Bình', 'Phường Phạm Ngũ Lão'],
    'Quận 3': ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5','Phường Võ Thị Sáu','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14'],
    'Quận 4': [ 'Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 6','Phường 8','Phường 09','Phường 10','Phường 13','Phường 14','Phường 15','Phường 16','Phường 18'],
    'Quận 5': ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14'],
    'Quận 6':['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14'],
    'Quận 7':['Phường Bình Thuận','Phường Phú Mỹ','Phường Phú Thuận','Phường Tân Hưng','Phường Tân Kiểng','Phường Tân Phong','Phường Tân Phú','Phường Tân Quy','Phường Tân Thuận Đông','Phường Tân Thuận Tây'],
    'Quận 8':['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15','Phường 16'],
    'Quận 10':['Phường 1', 'Phường 2', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15'],
    'Quận 11':['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15','Phường 16'],
    'Quận 12':['Phường An Phú Đông','Phường Đông Hưng Thuận','Phường Hiệp Thành','Phường Tân Chánh Hiệp','Phường Tân Hưng Thuận','Phường Tân Thới Hiệp','Phường Tân Thới Nhất','Phường Thạnh Lộc','Phường Thạnh Xuân','Phường Thới An','Phường Trung Mỹ Tây'],
    'Quận Tân Bình':['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15'],
    'Quận Bình Thạnh':['Phường 1', 'Phường 2', 'Phường 3','Phường 5', 'Phường 6','Phường 7','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15','Phường 17', 'Phường 19','Phường 21','Phường 22','Phường 24','Phường 25','Phường 26','Phường 27','Phường 28'],
    'Quận Bình Tân':['Phường An Lạc','Phường An Lạc A','Phường Bình Hưng Hòa','Phường Bình Hưng Hoà A','Phường Bình Hưng Hoà B','Phường Bình Trị Đông','Phường Bình Trị Đông A','Phường Bình Trị Đông B','Phường Tân Tạo','Phường Tân Tạo A'],
    'Thủ Đức':['An Khánh','An Lợi Đông','An Phú','Bình Chiểu','Bình Thọ','Bình Trưng Đông','Bình Trưng Tây','Cát Lái','Hiệp Bình Chánh','Hiệp Bình Phước','Hiệp Phú','Linh Chiểu','Linh Đông','Linh Tây','Linh Trung','Linh Xuân','Long Bình','Long Phước','Long Thạnh Mỹ','Long Trường','Phú Hữu','Phước Bình','Phước Long A','Phước Long B','Tam Bình','Tam Phú','Tăng Nhơn Phú A','Tăng Nhơn Phú B','Tân Phú','Thảo Điền','Thạnh Mỹ Lợi','Thủ Thiêm','Trường Thạnh','Trường Thọ'],
    'Quận Gò Vấp':['Phường 1', 'Phường 3', 'Phường 4','Phường 5', 'Phường 6','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 12','Phường 13','Phường 14','Phường 15','Phường 16','Phường 17'],
    'Quận Phú Nhuận':['Phường 1', 'Phường 2' ,'Phường 3', 'Phường 4','Phường 5','Phường 7','Phường 8','Phường 09','Phường 10','Phường 11','Phường 13','Phường 15','Phường 17'],
    'Quận Tân Phú':['Phường Hiệp Tân','Phường Hoà Thạnh','Phường Phú Thạnh','Phường Phú Thọ Hoà','Phường Phú Trung','Phường Sơn Kỳ','Phường Tân Qúy','Phường Tân Sơn Nhì','Phường Tân Thành','Phường Tân Thới Hoà','Phường Tây Thạnh'],
    'Huyện Bình Chánh':['Thị trấn Tân Túc','Xã An Phú Tây','Xã Bình Chánh','Xã Bình Hưng','Xã Bình Lợi','Xã Đa Phước','Xã Hưng Long','Xã Lê Minh Xuân','Xã Phạm Văn Hai','Xã Phong Phú','Xã Quy Đức','Xã Tân Kiên','Xã Tân Nhựt','Xã Tân Quý Tây','Xã Vĩnh Lộc A','Xã Vĩnh Lộc B'],
    'Huyện Hóc Môn':['Thị trấn Hóc Môn','Xã Bà Điểm','Xã Đông Thạnh','Xã Nhị Bình','Xã Tân Hiệp','Xã Tân Thới Nhì','Xã Tân Xuân','Xã Thới Tam Thôn','Xã Trung Chánh','Xã Xuân Thới Đông','Xã Xuân Thới Sơn','Xã Xuân Thới Thượng'],
    'Huyện Củ Chi':['Thị trấn Củ Chi','Xã An Nhơn Tây','Xã An Phú','Xã Bình Mỹ','Xã Hòa Phú','Xã Nhuận Đức','Xã Phạm Văn Cội','Xã Phú Hòa Đông','Xã Phú Mỹ Hưng','Xã Phước Hiệp','Xã Phước Thạnh','Xã Phước Vĩnh An','Xã Tân An Hội','Xã Tân Phú Trung','Xã Tân Thạnh Đông','Xã Tân Thạnh Tây','Xã Tân Thông Hội','Xã Thái Mỹ','Xã Trung An','Xã Trung Lập Hạ','Xã Trung Lập Thượng'],
    'Huyện Nhà Bè':['Thị trấn Nhà Bè','Xã Hiệp Phước','Xã Long Thới','Xã Nhơn Đức','Xã Phú Xuân','Xã Phước Kiển','Xã Phước Lộc'],
    'Huyện Cần Giờ':['Thị trấn Cần Thạnh','Xã An Thới Đông','Xã Bình Khánh','Xã Long Hòa','Xã Lý Nhơn','Xã Tam Thôn Hiệp','Xã Thạnh An'],
}
ho_list = list(ho_list)
ten_list = list(ten_list)
hs_data = []
birth_years = [2004, 2005, 2006]
birth_years_weights = [1, 1, 1]
cccd_numbers_male = list(range(1, 500001))  # Số căn cước công dân cho giới tính nam
cccd_numbers_female = list(range(1, 500001))  # Số căn cước công dân cho giới tính nữ
random.shuffle(cccd_numbers_male)  # Sắp xếp ngẫu nhiên
random.shuffle(cccd_numbers_female)  # Sắp xếp ngẫu nhiên
birth_year_counter = Counter()  # Đếm số lượng học sinh theo từng năm sinh
for i in range(1, 1000001):
    mahs = f"HS{i + 3:02}"
    ho = random.choice(ho_list)
    ten = random.choice(ten_list)
    if i <= 500000:
        gioi_tinh = "M"
        cccd = f"M{cccd_numbers_male[i - 1]:06}"
    else:
        gioi_tinh = "F"
        cccd = f"F{cccd_numbers_female[i - 500001]:06}"

    birth_year = random.choices(birth_years, weights=birth_years_weights)[0]
    birth_year_counter[birth_year] += 1

    min_birth_date = date(birth_year, 1, 1)
    max_birth_date = date(birth_year, 12, 31)
    random_birth_date = min_birth_date + timedelta(days=random.randint(0, 365))

    ntns = random_birth_date.strftime("%d/%m/%Y")
    quan = choice(list(phuong_quan.keys()))
    phuong = choice(phuong_quan[quan])
    dia_chi = f"{phuong}, {quan}, Thành phố Hồ Chí Minh"
    hs_data.append((mahs, ho, ten, cccd, ntns, dia_chi))

# Ghi dữ liệu vào tệp CSV
with open('hs.csv', 'w', newline='', encoding='utf-8') as hs_file:
    writer = csv.writer(hs_file)
    writer.writerow(['MAHS', 'HO', 'TEN', 'CCCD', 'NTNS', 'DCHI_HS'])
    writer.writerows(hs_data)

# PHẦN NÀY QUAN TRỌNG !!!


# Đọc thông tin xác thực từ file cấu hình
with open('config.json') as config_file:
    config = json.load(config_file)

# Ở đây vì em muốn nó mang 1 chút tính bảo mật, nên đã sử dụng 1 file cấu hình mạng để phòng khi mã nguồn có bị lộ ra thì các hacker vẫn không thể thực hiện sql injection được database gây mất mát dữ liệu
# Ý tưởng em học được qua những ngày chơi CTF và học pentest trên mạng, và vì muốn bám sát thực tế nhất có thể nên em đã thêm vào
# File cấu hình chính là file config.json, trong đó chứa thông tin như này:
# {
#  "host": "localhost",
#  "user": "root",
#  "password": "211031",
#  "database": "truonghoc1",
# }


# Thiết lập kết nối với cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)

# ĐÃ HẾT PHẦN QUAN TRỌNG


# Tạo con trỏ để thực hiện các truy vấn
cursor = conn.cursor()


# Chuyển dữ liệu từ tệp CSV vào bảng TRUONG
with open('truong.csv', 'r', encoding='utf-8') as truong_file:
    truong_data = csv.reader(truong_file)
    next(truong_data)  # Bỏ qua dòng tiêu đề
    for row in truong_data:
        matr, tentr, dchitr = row
        query = "INSERT INTO TRUONG VALUES (%s, %s, %s)"
        values = (matr, tentr, dchitr)
        cursor.execute(query, values)


# Chuyển dữ liệu từ tệp CSV vào bảng HS
with open('hs.csv', 'r', encoding='utf-8') as hs_file:
    hs_data = csv.reader(hs_file)
    next(hs_data)  # Bỏ qua dòng tiêu đề
    for row in hs_data:
        mahs, ho, ten, cccd, ntns, dia_chi = row
        query = "INSERT INTO HS VALUES (%s, %s, %s, %s, %s, %s)"
        values = (mahs, ho, ten, cccd, ntns, dia_chi)
        cursor.execute(query, values)

# bằng c
# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()




# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()

# Đóng kết nối và con trỏ
cursor.close()
conn.close()

print("đã xong câu 2")
