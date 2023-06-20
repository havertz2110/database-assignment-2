import xml.etree.ElementTree as ET

def read_xml_file(xml_file_path, low_threshold, high_threshold):
    # Đọc file XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Lọc danh sách học sinh theo ngưỡng điểm trung bình
    print("Danh sách học sinh:")
    for student in root.findall(".//student"):
        name = student.find("name").text
        average_score = float(student.find("average_score").text)

        if low_threshold <= average_score <= high_threshold:
            print(f"Họ tên: {name}, Điểm TB: {average_score}")

# Ví dụ sử dụng {tên database, tên trường; năm học; xếp loại học tập} 
xml_file_path = "database1, Trường THPTT Lê Quý Đôn,2019-2020, Giỏi.xml"
low_threshold = 7.0
high_threshold = 9.0

read_xml_file(xml_file_path, low_threshold, high_threshold)
