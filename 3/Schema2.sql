import mysql.connector
import xml.etree.ElementTree as ET
import time
from tabulate import tabulate

def query_database():
    # Người dùng nhập thông tin
    input_str = input("Nhập tên cơ sở dữ liệu, tên lĩnh vực, năm học, xếp hạng học tập (cách nhau bằng dấu phẩy): ")

    # Tách chuỗi nhập vào thành các phần tử riêng biệt
    inputs = input_str.split(",")

    # Gán giá trị cho các biến tương ứng
    database_name = inputs[0].strip()
    ten_truong = inputs[1].strip()
    nam_hoc = inputs[2].strip()
    xep_loai = inputs[3].strip()

    # Thiết lập kết nối với cơ sở dữ liệu MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="211031",
        database="truonghoc1"
    )

    # Tạo con trỏ để thực hiện các truy vấn
    cursor = conn.cursor()

    # Đo thời gian thực hiện truy vấn
    start_time = time.time()

    # Truy vấn dữ liệu từ cơ sở dữ liệu
    query = f"""
            SELECT hs.ho, hs.ten, hs.ntns, hoc.diemtb, hoc.xeploai, hoc.kqua
    	    FROM truong
    	    JOIN hoc ON truong.matr = hoc.matr
    	    JOIN hs ON hoc.mahs = hs.mahs
    	    WHERE truong.tentr = '{ten_truong}' AND hoc.namhoc = '{nam_hoc}' AND hoc.xeploai = '{xep_loai}';
        """

    cursor.execute(query)
    results = cursor.fetchall()

    # Tính thời gian truy vấn
    end_time = time.time()
    query_time = end_time - start_time


    table = []

    for row in results:
        full_name = f"{row[0]} {row[1]}"
        table.append([full_name, row[2], row[3], row[4], row[5]])

    headers = ["Họ tên", "NTNS", "Điểm TB", "Xếp loại", "Kết quả"]

    print(tabulate(table, headers, tablefmt="fancy_grid"))
    print(f"Thời gian truy vấn: {query_time} giây")
    #truonghoc1,THPT Lê Quý Đôn,2019-2020,Giỏi
    # Tạo và xuất file XML
    xml_root = ET.Element("students")
    for row in results:
        full_name = f"{row[0]} {row[1]}"
        student_element = ET.SubElement(xml_root, "student")
        ET.SubElement(student_element, "ho_ten").text = full_name
        ET.SubElement(student_element, "ntns").text = row[2]
        ET.SubElement(student_element, "diem_tb").text = str(row[3])
        ET.SubElement(student_element, "xep_loai").text = row[4]
        ET.SubElement(student_element, "ket_qua").text = row[5]

    xml_tree = ET.ElementTree(xml_root)
    xml_filename = f"{database_name}-{ten_truong}-{nam_hoc}-{xep_loai}.xml"
    xml_tree.write(xml_filename)

    # Đóng kết nối cơ sở dữ liệu
    conn.close()


# Sử dụng hàm truy vấn cơ sở dữ liệu
query_database()
