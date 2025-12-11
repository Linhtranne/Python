import csv
import os
import matplotlib.pyplot as plt
rooms = []

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "data.csv")

def load_data(file_path):
    global rooms
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rooms = []
                for row in reader:
                    rooms.append({
                        "ma_phong": row["ma_phong"],
                        "loai_phong": row["loai_phong"],
                        "gia_ngay": row["gia_ngay"],
                        "so_ngay_o": row["so_ngay_o"],
                        "dich_vu_them": row["dich_vu_them"],
                        "tong_tien": row["tong_tien"],
                        "phan_hang": row["phan_hang"]
                    })
            print(f"Đã tải {len(rooms)} phòng từ {DATA_FILE}.")
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu: {e}")
    else:
        print(f"File {DATA_FILE} chưa tồn tại. Sẽ tạo mới khi lưu dữ liệu.")

def add_room():
    """
    Check-out (Thêm đơn)
    """
    global rooms

    load_data(DATA_FILE)
    
    while True:
        ma_phong = input("Nhập mã phòng: ").strip()
        if not ma_phong:
            print("Mã phòng không được để trống!")
            continue
        if any(room["ma_phong"] == ma_phong for room in rooms):
            print(f"Mã phòng '{ma_phong}' đã tồn tại! Vui lòng nhập mã khác.")
            continue
        break
    loai_phong = input("Nhập loại phòng: ").strip()
    while True:
        try:
            gia_ngay = float(input("Nhập giá ngày: "))
            if gia_ngay < 0:
                print("Giá ngày phải >= 0!")
                continue
            break
        except ValueError:
            print("Giá ngày phải là số!")
    while True:
        try:
            so_ngay_o = int(input("Nhập số ngày ở: "))
            if so_ngay_o <= 0:
                print("Số ngày ở phải > 0!")
                continue
            break
        except ValueError:
            print("Số ngày ở phải là số nguyên!")
    while True:
        try:
            dich_vu_them = float(input("Nhập tiền dịch vụ thêm: "))
            if dich_vu_them < 0:
                print("Tiền dịch vụ phải >= 0!")
                continue
            break
        except ValueError:
            print("Tiền dịch vụ phải là số!")
    tong_tien = (gia_ngay * so_ngay_o) + dich_vu_them
    if tong_tien > 10000000:
        phan_hang = "Diamond"
    elif tong_tien > 5000000:
        phan_hang = "Gold"
    else:
        phan_hang = "Silver"
    room = {
        "ma_phong": ma_phong,
        "loai_phong": loai_phong,
        "gia_ngay": gia_ngay,
        "so_ngay_o": so_ngay_o,
        "dich_vu_them": dich_vu_them,
        "tong_tien": tong_tien,
        "phan_hang": phan_hang
    }
    rooms.append(room)
    
    save_data(DATA_FILE)
    
    print(f"\n Đã thêm phòng '{ma_phong}' thành công!")
    print(f"  - Tổng tiền: {tong_tien:,.0f} VNĐ")
    print(f"  - Phân hạng: {phan_hang}")

def display_rooms():
    """
    Hiển thị danh sách phòng
    """
    global rooms
    load_data(DATA_FILE)
    if not rooms:
        print("\n Danh sách phòng trống!")
        return
    print("\n" + "="*120)
    print(f"{'MÃ PHÒNG':<12} {'LOẠI PHÒNG':<15} {'GIÁ NGÀY':>12} {'SỐ NGÀY':>10} {'DỊCH VỤ':>12} {'TỔNG TIỀN':>15} {'PHÂN HẠNG':<10}")
    print("="*120)
    for room in rooms:
        print(f"{room['ma_phong']:<12} "
              f"{room['loai_phong']:<15} "
              f"{float(room['gia_ngay']):>12,.0f} "
              f"{int(room['so_ngay_o']):>10} "
              f"{float(room['dich_vu_them']):>12,.0f} "
              f"{float(room['tong_tien']):>15,.0f} "
              f"{room['phan_hang']:<10}")
    
    print("="*120)
    print(f"Tổng số phòng: {len(rooms)}")

def update_room():
    """
    Cập nhật đơn
    """
    global rooms
    load_data(DATA_FILE)
    
    if not rooms:
        print("\n Danh sách phòng trống! Không thể cập nhật.")
        return
    ma_phong = input("Nhập mã phòng cần cập nhật: ").strip()
    room = None
    for r in rooms:
        if r["ma_phong"] == ma_phong:
            room = r
            break
    
    if not room:
        print(f"\n Không tìm thấy phòng có mã '{ma_phong}'!")
        return
    print(f"\n Thông tin phòng '{ma_phong}':")
    print(f"  - Loại phòng: {room['loai_phong']}")
    print(f"  - Giá ngày: {float(room['gia_ngay']):,.0f} VNĐ")
    print(f"  - Số ngày ở: {room['so_ngay_o']}")
    print(f"  - Dịch vụ thêm: {float(room['dich_vu_them']):,.0f} VNĐ")
    print(f"  - Tổng tiền: {float(room['tong_tien']):,.0f} VNĐ")
    print(f"  - Phân hạng: {room['phan_hang']}")
    print("\n--- Cập nhật thông tin ---")
    while True:
        try:
            so_ngay_o_moi = input(f"Nhập số ngày ở mới (hiện tại: {room['so_ngay_o']}): ").strip()
            if not so_ngay_o_moi:
                so_ngay_o_moi = int(room['so_ngay_o'])
            else:
                so_ngay_o_moi = int(so_ngay_o_moi)
            
            if so_ngay_o_moi <= 0:
                print("Số ngày ở phải > 0!")
                continue
            break
        except ValueError:
            print("Số ngày ở phải là số nguyên!")
    while True:
        try:
            dich_vu_moi = input(f"Nhập tiền dịch vụ thêm mới (hiện tại: {float(room['dich_vu_them']):,.0f}): ").strip()
            if not dich_vu_moi:
                dich_vu_moi = float(room['dich_vu_them'])
            else:
                dich_vu_moi = float(dich_vu_moi)
            
            if dich_vu_moi < 0:
                print("Tiền dịch vụ phải >= 0!")
                continue
            break
        except ValueError:
            print("Tiền dịch vụ phải là số!")
    gia_ngay = float(room['gia_ngay'])
    tong_tien_moi = (gia_ngay * so_ngay_o_moi) + dich_vu_moi
    if tong_tien_moi > 10000000:
        phan_hang_moi = "Diamond"
    elif tong_tien_moi > 5000000:
        phan_hang_moi = "Gold"
    else:
        phan_hang_moi = "Silver"
    room['so_ngay_o'] = so_ngay_o_moi
    room['dich_vu_them'] = dich_vu_moi
    room['tong_tien'] = tong_tien_moi
    room['phan_hang'] = phan_hang_moi
    
    save_data(DATA_FILE)
    
    print(f"\n Đã cập nhật phòng '{ma_phong}' thành công!")
    print(f"  - Số ngày ở mới: {so_ngay_o_moi}")
    print(f"  - Dịch vụ thêm mới: {dich_vu_moi:,.0f} VNĐ")
    print(f"  - Tổng tiền mới: {tong_tien_moi:,.0f} VNĐ")
    print(f"  - Phân hạng mới: {phan_hang_moi}")

def delete_room():
    """
    Xoá đơn
    """
    global rooms
    load_data(DATA_FILE)
    
    if not rooms:
        print("\n Danh sách phòng trống! Không thể xóa.")
        return
    ma_phong = input("Nhập mã phòng cần xóa: ").strip()
    room = None
    for r in rooms:
        if r["ma_phong"] == ma_phong:
            room = r
            break
    
    if not room:
        print(f"\n Không tìm thấy phòng có mã '{ma_phong}'!")
        return
    rooms.remove(room)

    save_data(DATA_FILE)
    
    print(f"\n Đã xóa phòng '{ma_phong}' thành công!")

def save_data(file_path):
    """
    Lưu vào file CSV
    """
    global rooms
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["ma_phong", "loai_phong", "gia_ngay", "so_ngay_o", "dich_vu_them", "tong_tien", "phan_hang"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for room in rooms:
                writer.writerow(room)
        print(f"\n Đã lưu {len(rooms)} phòng vào {file_path}.")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu: {e}")

def search_room():
    """
    Tìm kiếm phòng
    """
    global rooms
    load_data(DATA_FILE)
    
    if not rooms:
        print("\n Danh sách phòng trống! Không thể tìm kiếm.")
        return
    keyword = input("Nhập từ khóa tìm kiếm (theo Mã phòng): ").strip().lower()
    results = [room for room in rooms if keyword in room["ma_phong"].lower()]
    if not results:
        print(f"\n Không tìm thấy phòng nào với từ khóa '{keyword}'!")
        return
    print(f"\n Kết quả tìm kiếm cho từ khóa '{keyword}':")
    print(f"{'MÃ PHÒNG':<12} {'LOẠI PHÒNG':<15} {'GIÁ NGÀY':>12} {'SỐ NGÀY':>10} {'DỊCH VỤ':>12} {'TỔNG TIỀN':>15} {'PHÂN HẠNG':<10}")
    for room in results:
        print(f"{room['ma_phong']:<12} "
              f"{room['loai_phong']:<15} "
              f"{float(room['gia_ngay']):>12,.0f} "
              f"{int(room['so_ngay_o']):>10} "
              f"{float(room['dich_vu_them']):>12,.0f} "
              f"{float(room['tong_tien']):>15,.0f} "
              f"{room['phan_hang']:<10}")
    print(f"Tổng số phòng tìm thấy: {len(results)}")

def sort_rooms():
    """
    Sắp xếp danh sách phòng
    """
    global rooms
    load_data(DATA_FILE)
    
    if not rooms:
        print("\n Danh sách phòng trống! Không thể sắp xếp.")
        return
    
    rooms.sort(key=lambda room: float(room['tong_tien']), reverse=True)
    save_data(DATA_FILE)
    
    print("\n Đã sắp xếp danh sách phòng theo Tổng tiền giảm dần!")
    print("\n" + "="*120)
    print(f"{'MÃ PHÒNG':<12} {'LOẠI PHÒNG':<15} {'GIÁ NGÀY':>12} {'SỐ NGÀY':>10} {'DỊCH VỤ':>12} {'TỔNG TIỀN':>15} {'PHÂN HẠNG':<10}")
    print("="*120)
    
    for room in rooms:
        print(f"{room['ma_phong']:<12} "
              f"{room['loai_phong']:<15} "
              f"{float(room['gia_ngay']):>12,.0f} "
              f"{int(room['so_ngay_o']):>10} "
              f"{float(room['dich_vu_them']):>12,.0f} "
              f"{float(room['tong_tien']):>15,.0f} "
              f"{room['phan_hang']:<10}")
    
    print("="*120)
    print(f"Tổng số phòng: {len(rooms)}")

def statistics():
    """
    Thống kê doanh thu
    """
    global rooms
    
    if not rooms:
        print("\nDanh sách phòng trống! Không thể thống kê.")
        return
    hang_counts = {"Diamond": 0, "Gold": 0, "Silver": 0}
    tong_doanh_thu = {"Diamond": 0, "Gold": 0, "Silver": 0}
    
    for room in rooms:
        phan_hang = room['phan_hang']
        if phan_hang in hang_counts:
            hang_counts[phan_hang] += 1
            tong_doanh_thu[phan_hang] += float(room['tong_tien'])

    print("\n" + "="*80)
    print("THỐNG KÊ DOANH THU THEO PHÂN HẠNG KHÁCH HÀNG")
    print("="*80)
    print(f"{'PHÂN HẠNG':<15} {'SỐ LƯỢNG ĐƠN':>15} {'TỔNG DOANH THU':>20} {'TRUNG BÌNH':>20}")
    print("-"*80)
    
    tong_don = 0
    tong_dt = 0
    
    for hang in ["Diamond", "Gold", "Silver"]:
        so_luong = hang_counts[hang]
        doanh_thu = tong_doanh_thu[hang]
        tb = doanh_thu / so_luong if so_luong > 0 else 0
        
        print(f"{hang:<15} {so_luong:>15} {doanh_thu:>20,.0f} {tb:>20,.0f}")
        tong_don += so_luong
        tong_dt += doanh_thu
    
    print("-"*80)
    print(f"{'TỔNG CỘNG':<15} {tong_don:>15} {tong_dt:>20,.0f} {tong_dt/tong_don if tong_don > 0 else 0:>20,.0f}")
    print("="*80)
def plot_chart():
    """
    Vẽ biểu đồ thống kê
    """
    global rooms
    
    if not rooms:
        print("\n Danh sách phòng trống! Không thể vẽ biểu đồ.")
        return
    hang_counts = {"Diamond": 0, "Gold": 0, "Silver": 0}
    
    for room in rooms:
        phan_hang = room['phan_hang']
        if phan_hang in hang_counts:
            hang_counts[phan_hang] += 1

    color_map = {
        "Diamond": "#00CED1", 
        "Gold": "#FFD700", 
        "Silver": "#C0C0C0"
    }
    
    labels = []
    sizes = []
    colors = []
    explode = []
    
    for hang in ["Diamond", "Gold", "Silver"]:
        if hang_counts[hang] > 0:
            labels.append(f"{hang}\n({hang_counts[hang]} đơn)")
            sizes.append(hang_counts[hang])
            colors.append(color_map[hang])
            explode.append(0.05) 
    
    if not sizes:
        print("\n Không có dữ liệu để vẽ biểu đồ!")
        return
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, 
            colors=colors, explode=explode, shadow=True)
    plt.title('Thống kê số lượng đơn theo phân hạng khách hàng', 
              fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
    print("\n Đã hiển thị biểu đồ thống kê!")

def show_menu():
    """
    Hiển thị menu chức năng chính.
    """
    print("\n" + "="*60)
    print(" "*15 + "HỆ THỐNG QUẢN LÝ PHÒNG KHÁCH SẠN")
    print("="*60)
    print("1. Hiển thị danh sách phòng")
    print("2. Thêm mới phòng")
    print("3. Cập nhật thông tin phòng")
    print("4. Xoá phòng")
    print("5. Tìm kiếm phòng")
    print("6. Sắp xếp danh sách phòng")
    print("7. Thống kê doanh thu")
    print("8. Vẽ biểu đồ thống kê")
    print("9. Lưu vào file CSV")
    print("0. Thoát")
    print("="*60)

def main():
    """
    Hàm chính điều khiển chương trình.
    """
    global rooms
    load_data(DATA_FILE)
    
    while True:
        show_menu()
        choice = input("\nNhập lựa chọn của bạn (0-9): ").strip()
        
        if choice == '1':
            display_rooms()
        elif choice == '2':
            add_room()
        elif choice == '3':
            update_room()
        elif choice == '4':
            delete_room()
        elif choice == '5':
            search_room()
        elif choice == '6':
            sort_rooms()
        elif choice == '7':
            statistics()
        elif choice == '8':
            plot_chart()
        elif choice == '9':
            save_data(DATA_FILE)
        elif choice == '0':
            if rooms:
                print("\n Đang lưu dữ liệu...")
                save_data(DATA_FILE)
            print("="*60)
            break
        else:
            print("\n Lựa chọn không hợp lệ! Vui lòng chọn từ 0-9.")
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()

