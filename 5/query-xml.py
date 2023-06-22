
import glob
import xml.etree.ElementTree as ET
from tabulate import tabulate

def doc_file_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    nguong_diem_thap = float(input("Nhập ngưỡng điểm thấp: "))
    nguong_diem_cao = float(input("Nhập ngưỡng điểm cao: "))

    table = []
    for student in root.findall('student'):
        ho_ten = student.find('ho_ten').text
        diem_tb = float(student.find('diem_tb').text)


        if nguong_diem_thap <= diem_tb <= nguong_diem_cao:
            table.append([ho_ten,  diem_tb])

    headers = ["Họ tên",  "Điểm TB"]
    print(tabulate(table, headers, tablefmt="fancy_grid"))



def main():
    # Lấy danh sách tất cả các file XML trong thư mục hiện tại
    files = glob.glob("*.xml")

    if not files:
        print("Không tìm thấy file XML trong thư mục.")
        return

    print("Danh sách các file XML:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    file_chon = int(input("Chọn số thứ tự của file cần đọc: "))
    if 1 <= file_chon <= len(files):
        file_duoc_chon = files[file_chon-1]
        doc_file_xml(file_duoc_chon)
    else:
        print("Số thứ tự không hợp lệ.")

if __name__ == '__main__':
    main()
