import sqlite3
import xml.etree.ElementTree as ET
import time

def query_database(database_name, field_name, school_year, academic_rank):
    # Tạo kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Đo thời gian thực hiện truy vấn
    start_time = time.time()

    # Truy vấn dữ liệu từ cơ sở dữ liệu
    query = f"SELECT * FROM students WHERE field = '{field_name}' AND year = '{school_year}' AND rank = '{academic_rank}'"
    cursor.execute(query)
    results = cursor.fetchall()

    # Tính thời gian truy vấn
    end_time = time.time()
    query_time = end_time - start_time

    # In danh sách học sinh và đoạn thời gian truy vấn
    print("Danh sách học sinh:")
    for row in results:
        print(f"Họ tên: {row[0]}, NTNS: {row[1]}, Điểm TB: {row[2]}, Xếp loại: {row[3]}, Kết quả: {row[4]}")
    print(f"Thời gian truy vấn: {query_time} giây")

    # Tạo và xuất file XML
    xml_root = ET.Element("students")
    for row in results:
        student_element = ET.SubElement(xml_root, "student")
        ET.SubElement(student_element, "name").text = row[0]
        ET.SubElement(student_element, "dob").text = row[1]
        ET.SubElement(student_element, "average_score").text = str(row[2])
        ET.SubElement(student_element, "academic_rank").text = row[3]
        ET.SubElement(student_element, "result").text = row[4]
    
    xml_tree = ET.ElementTree(xml_root)
    xml_filename = f"{database_name}-{field_name}-{school_year}-{academic_rank}.xml"
    xml_tree.write(xml_filename)

    # Đóng kết nối cơ sở dữ liệu
    conn.close()

# Ví dụ sử dụng
database_name1 = "database1.db"
database_name2 = "database2.db"
field_name = "Computer Science"
school_year = "2023"
academic_rank = "Excellent"

# Truy vấn cơ sở dữ liệu 1
query_database(database_name1, field_name, school_year, academic_rank)

# Truy vấn cơ sở dữ liệu 2
query_database(database_name2, field_name, school_year, academic_rank)
