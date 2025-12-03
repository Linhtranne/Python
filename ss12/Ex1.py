import csv
import os
import matplotlib.pyplot as plt
students = []
DATA_FILE = "data.csv"

def load_data():
    global students
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                students = []
                for row in reader:
                    students.append({
                        'ma_sv': row['ma_sv'],
                        'ten': row['ten'],
                        'diem_toan': float(row['diem_toan']),
                        'diem_ly': float(row['diem_ly']),
                        'diem_hoa': float(row['diem_hoa']),
                        'diem_tb': float(row['diem_tb']),
                        'xep_loai': row['xep_loai']
                    })
            print(f"Đã tải {len(students)} sinh viên từ file {DATA_FILE}")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
    else:
        print(f"File {DATA_FILE} chưa tồn tại. Sẽ tạo mới khi lưu dữ liệu.")


def calculate_average(toan, ly, hoa):
    return round((toan + ly + hoa) / 3, 2)


def classify_student(diem_tb):
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung Bình"
    else:
        return "Yếu"


def display_students():
    if not students:
        print("\nDanh sách sinh viên trống!")
        return
    
    print("\n" + "="*100)
    print(f"{'Mã SV':<10} {'Tên':<25} {'Điểm Toán':<12} {'Điểm Lý':<12} {'Điểm Hóa':<12} {'Điểm TB':<12} {'Xếp loại':<15}")
    print("="*100)
    
    for sv in students:
        print(f"{sv['ma_sv']:<10} {sv['ten']:<25} {sv['diem_toan']:<12.2f} {sv['diem_ly']:<12.2f} {sv['diem_hoa']:<12.2f} {sv['diem_tb']:<12.2f} {sv['xep_loai']:<15}")
    
    print("="*100)
    print(f"Tổng số sinh viên: {len(students)}")


def add_student():
    while True:
        ma_sv = input("Nhập Mã SV: ").strip()
        if not ma_sv:
            print("Mã SV không được để trống!")
            continue
        if any(sv['ma_sv'] == ma_sv for sv in students):
            print("Mã SV đã tồn tại! Vui lòng nhập mã khác.")
            continue
        break
    ten = input("Nhập Tên: ").strip()
    while True:
        try:
            diem_toan = float(input("Nhập Điểm Toán (0-10): "))
            if 0 <= diem_toan <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    while True:
        try:
            diem_ly = float(input("Nhập Điểm Lý (0-10): "))
            if 0 <= diem_ly <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    while True:
        try:
            diem_hoa = float(input("Nhập Điểm Hóa (0-10): "))
            if 0 <= diem_hoa <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    diem_tb = calculate_average(diem_toan, diem_ly, diem_hoa)
    xep_loai = classify_student(diem_tb)
    students.append({
        'ma_sv': ma_sv,
        'ten': ten,
        'diem_toan': diem_toan,
        'diem_ly': diem_ly,
        'diem_hoa': diem_hoa,
        'diem_tb': diem_tb,
        'xep_loai': xep_loai
    })
    
    print(f"\n✓ Đã thêm sinh viên {ma_sv} - {ten} (Điểm TB: {diem_tb}, Xếp loại: {xep_loai})")


def update_student():
    ma_sv = input("Nhập Mã SV cần cập nhật: ").strip()
    sv = None
    for s in students:
        if s['ma_sv'] == ma_sv:
            sv = s
            break
    
    if not sv:
        print(f"Không tìm thấy sinh viên có Mã SV: {ma_sv}")
        return
    
    print(f"\nThông tin hiện tại: {sv['ten']} - Toán: {sv['diem_toan']}, Lý: {sv['diem_ly']}, Hóa: {sv['diem_hoa']}")
    while True:
        try:
            diem_toan = float(input("Nhập Điểm Toán mới (0-10): "))
            if 0 <= diem_toan <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    while True:
        try:
            diem_ly = float(input("Nhập Điểm Lý mới (0-10): "))
            if 0 <= diem_ly <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    while True:
        try:
            diem_hoa = float(input("Nhập Điểm Hóa mới (0-10): "))
            if 0 <= diem_hoa <= 10:
                break
            print("Điểm phải trong khoảng 0-10!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    sv['diem_toan'] = diem_toan
    sv['diem_ly'] = diem_ly
    sv['diem_hoa'] = diem_hoa
    sv['diem_tb'] = calculate_average(diem_toan, diem_ly, diem_hoa)
    sv['xep_loai'] = classify_student(sv['diem_tb'])
    
    print(f"\n✓ Đã cập nhật sinh viên {ma_sv} (Điểm TB mới: {sv['diem_tb']}, Xếp loại: {sv['xep_loai']})")


def delete_student():
    ma_sv = input("Nhập Mã SV cần xóa: ").strip()
    sv = None
    for s in students:
        if s['ma_sv'] == ma_sv:
            sv = s
            break
    
    if not sv:
        print(f"Không tìm thấy sinh viên có Mã SV: {ma_sv}")
        return

    confirm = input(f"Bạn có chắc muốn xóa sinh viên {sv['ten']} (Mã: {ma_sv})? (y/n): ").strip().lower()
    
    if confirm == 'y':
        students.remove(sv)
        print(f"\n✓ Đã xóa sinh viên {ma_sv}")
    else:
        print("Hủy xóa sinh viên")


def search_student():
    print("1. Tìm theo Mã SV")
    print("2. Tìm theo Tên")
    
    choice = input("Chọn cách tìm kiếm (1/2): ").strip()
    
    if choice == '1':
        ma_sv = input("Nhập Mã SV: ").strip()
        results = [sv for sv in students if sv['ma_sv'] == ma_sv]
    elif choice == '2':
        ten = input("Nhập Tên (hoặc một phần tên): ").strip().lower()
        results = [sv for sv in students if ten in sv['ten'].lower()]
    else:
        print("Lựa chọn không hợp lệ!")
        return
    
    if results:
        print(f"\nTìm thấy {len(results)} sinh viên:")
        print("="*100)
        print(f"{'Mã SV':<10} {'Tên':<25} {'Điểm Toán':<12} {'Điểm Lý':<12} {'Điểm Hóa':<12} {'Điểm TB':<12} {'Xếp loại':<15}")
        print("="*100)
        for sv in results:
            print(f"{sv['ma_sv']:<10} {sv['ten']:<25} {sv['diem_toan']:<12.2f} {sv['diem_ly']:<12.2f} {sv['diem_hoa']:<12.2f} {sv['diem_tb']:<12.2f} {sv['xep_loai']:<15}")
        print("="*100)
    else:
        print("Không tìm thấy sinh viên nào!")


def sort_students():
    if not students:
        print("\nDanh sách sinh viên trống!")
        return
    print("1. Sắp xếp theo Điểm TB (giảm dần)")
    print("2. Sắp xếp theo Tên (A-Z)")
    
    choice = input("Chọn cách sắp xếp (1/2): ").strip()
    
    if choice == '1':
        students.sort(key=lambda x: x['diem_tb'], reverse=True)
        print("\n✓ Đã sắp xếp theo Điểm TB giảm dần")
    elif choice == '2':
        students.sort(key=lambda x: x['ten'])
        print("\n✓ Đã sắp xếp theo Tên (A-Z)")
    else:
        print("Lựa chọn không hợp lệ!")
        return
    
    display_students()


def statistics():
    if not students:
        print("\nDanh sách sinh viên trống!")
        return
    count = {'Giỏi': 0, 'Khá': 0, 'Trung Bình': 0, 'Yếu': 0}
    
    for sv in students:
        count[sv['xep_loai']] += 1
    print(f"Giỏi (>= 8.0):          {count['Giỏi']} sinh viên ({count['Giỏi']/len(students)*100:.1f}%)")
    print(f"Khá (6.5 - 7.9):        {count['Khá']} sinh viên ({count['Khá']/len(students)*100:.1f}%)")
    print(f"Trung Bình (5.0 - 6.4): {count['Trung Bình']} sinh viên ({count['Trung Bình']/len(students)*100:.1f}%)")
    print(f"Yếu (< 5.0):            {count['Yếu']} sinh viên ({count['Yếu']/len(students)*100:.1f}%)")
    print(f"Tổng số sinh viên: {len(students)}")


def plot_chart():
    if not students:
        print("\nDanh sách sinh viên trống!")
        return

    count = {'Giỏi': 0, 'Khá': 0, 'Trung Bình': 0, 'Yếu': 0}
    
    for sv in students:
        count[sv['xep_loai']] += 1
    
    labels = [k for k, v in count.items() if v > 0]
    sizes = [v for v in count.values() if v > 0]
    colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.pie(sizes, labels=labels, colors=colors[:len(labels)], autopct='%1.1f%%',
            startangle=90, textprops={'fontsize': 11})
    ax1.set_title('Tỷ lệ xếp loại học lực (Pie Chart)', fontsize=13, fontweight='bold')
    
    ax2.bar(labels, sizes, color=colors[:len(labels)], edgecolor='black', linewidth=1.5)
    ax2.set_title('Số lượng sinh viên theo xếp loại (Bar Chart)', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Xếp loại', fontsize=11)
    ax2.set_ylabel('Số lượng sinh viên', fontsize=11)
    ax2.grid(True, alpha=0.3, axis='y')
    
    for i, v in enumerate(sizes):
        ax2.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Đã hiển thị biểu đồ thống kê")


def save_to_csv():
    try:
        with open(DATA_FILE, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['ma_sv', 'ten', 'diem_toan', 'diem_ly', 'diem_hoa', 'diem_tb', 'xep_loai']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for sv in students:
                writer.writerow(sv)
        
        print(f"\n✓ Đã lưu {len(students)} sinh viên vào file {DATA_FILE}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")


def menu():
    """Hiển thị menu"""
    print("\n" + "="*50)
    print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("="*50)
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Xoá sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách sinh viên")
    print("7. Thống kê điểm TB")
    print("8. Vẽ biểu đồ thống kê điểm TB")
    print("9. Lưu vào file CSV")
    print("10. Thoát")
    print("="*50)


def main():
    """Hàm main chạy chương trình"""
    load_data()
    
    while True:
        menu()
        choice = input("Chọn chức năng (1-10): ").strip()
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            statistics()
        elif choice == '8':
            plot_chart()
        elif choice == '9':
            save_to_csv()
        elif choice == '10':
            # Tự động lưu trước khi thoát
            save_to_csv()
            print("\n✓ Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-10.")


if __name__ == "__main__":
    main()
