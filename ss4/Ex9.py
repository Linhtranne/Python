product_list = []


def menu():
    print("1. Thêm sản phẩm mới")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Tìm kiếm sản phẩm theo mã sản phẩm")
    print("4. Cập nhật thông tin sản phẩm")
    print("5. Xóa sản phẩm theo mã sản phẩm")
    print("0. Thoát chương trình")


def add_product():
    product_code = input("Nhập mã sản phẩm: ")
    for product in product_list:
        if product[0] == product_code:
            print(f"Lỗi: Mã sản phẩm '{product_code}' đã tồn tại!")
            return

    product_name = input("Nhập tên sản phẩm: ")
    quantity = int(input("Nhập số lượng: "))
    price = float(input("Nhập giá: "))
    product = (product_code, product_name, quantity, price)
    product_list.append(product)
    print(f"✓ Đã thêm sản phẩm '{product_name}' thành công!")


def display_list():
    if not product_list:
        print("Danh sách sản phẩm trống!")
        return

    print(f"{'Mã SP':<10} {'Tên sản phẩm':<25} "
          f"{'Số lượng':<12} {'Giá':<15}")
    print("-" * 70)
    for product in product_list:
        print(f"{product[0]:<10} {product[1]:<25} "
              f"{product[2]:<12} {product[3]:<15,.0f} VNĐ")


def search_product():
    product_code = input("Nhập mã sản phẩm cần tìm: ")

    for product in product_list:
        if product[0] == product_code:
            print("\nThông tin sản phẩm:")
            print(f"Mã sản phẩm: {product[0]}")
            print(f"Tên sản phẩm: {product[1]}")
            print(f"Số lượng: {product[2]}")
            print(f"Giá: {product[3]:,.0f} VNĐ")
            return

    print(f"Không tìm thấy sản phẩm có mã '{product_code}'!")


def update_product():
    product_code = input("Nhập mã sản phẩm cần cập nhật: ")

    for i in range(len(product_list)):
        if product_list[i][0] == product_code:
            print(f"Thông tin hiện tại: {product_list[i]}")
            product_name = input("Nhập tên sản phẩm mới: ")
            quantity = int(input("Nhập số lượng mới: "))
            price = float(input("Nhập giá mới: "))
            product_list[i] = (product_code, product_name, quantity, price)
            print("✓ Đã cập nhật sản phẩm thành công!")
            return

    print(f"Không tìm thấy sản phẩm có mã '{product_code}'!")


def delete_product():
    product_code = input("Nhập mã sản phẩm cần xóa: ")

    for i in range(len(product_list)):
        if product_list[i][0] == product_code:
            product_name = product_list[i][1]
            product_list.pop(i)
            print(f"✓ Đã xóa sản phẩm '{product_name}' thành công!")
            return

    print(f"Không tìm thấy sản phẩm có mã '{product_code}'!")


while True:
    menu()
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        display_list()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "0":
        print("\nCảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("\nVui lòng nhập lại!")
