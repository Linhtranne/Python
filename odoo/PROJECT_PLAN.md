# 📋 DỰ ÁN QUẢN LÝ TECH ZONE - ODOO MODULE

## 🎯 TỔNG QUAN DỰ ÁN

**Tên Module:** `device_repair`  
**Mục đích:** Hệ thống quản lý sửa chữa thiết bị điện tử (điện thoại, laptop, tablet...)  
**Tổng điểm:** 100 điểm  
**Phụ thuộc:** `base`, `product`, `mail`

---

## 📁 CẤU TRÚC THƯ MỤC MODULE

```
device_repair/
├── __init__.py                    # File khởi tạo module (Import models)
├── __manifest__.py                # Khai báo module (Tên: Device Repair, Depends: base, product, mail)
├── models/                        # Chứa code Python (Database structure & Logic)
│   ├── __init__.py                # Import các file .py bên dưới
│   ├── device.py                 # Model RepairDevice (Gốc), Logic bảo hành, Computed fields
│   ├── device_brand.py            # Model RepairBrand, RepairModel (Hãng, Dòng máy)
│   ├── repair_order.py            # Model RepairOrder (Header) & RepairLine (Chi tiết) - Core Logic
│   ├── repair_history.py          # Model RepairHistory, RepairDiagnosis (Lịch sử lỗi)
│   ├── repair_appointment.py      # Model RepairAppointment (Lịch hẹn)
│   ├── res_partner.py             # Kế thừa res.partner (Thêm ds thiết bị sở hữu)
│   └── product.py                 # Kế thừa product.template (Thêm field is_repair_part)
├── views/                         # Chứa code XML (Giao diện người dùng)
│   ├── device_views.xml           # Form, Tree, Kanban, Search view của Thiết bị
│   ├── repair_order_views.xml     # View Phiếu sửa chữa (Form, Tree, Graph, Pivot)
│   ├── repair_appointment_views.xml # View Lịch hẹn (Calendar, Tree)
│   ├── repair_history_views.xml   # View Lịch sử lỗi (thường nhúng vào Form Device)
│   ├── res_partner_views.xml      # Kế thừa View Partner (Thêm tab "Thiết bị")
│   ├── product_views.xml          # Kế thừa View Product (Thêm checkbox Linh kiện)
│   └── menus.xml                  # Định nghĩa Menu cha (Sửa chữa), Menu con (Thiết bị, Báo cáo...)
├── security/                      # Chứa phân quyền
│   ├── repair_security.xml        # Định nghĩa Groups (Technician/Manager) và Record Rules
│   └── ir.model.access.csv        # Phân quyền CRUD (Đọc/Ghi/Xóa) cho từng Model
├── data/                          # Chứa dữ liệu hệ thống & Demo
│   ├── ir_sequence_data.xml       # Định nghĩa quy tắc sinh Mã Phiếu (REP/001) và Mã Máy (DEV/001)
│   └── demo_data.xml              # Dữ liệu mẫu (iPhone 13, Galaxy S24, Khách hàng mẫu)
└── static/                        # Chứa tài nguyên tĩnh
    └── description/               # Chứa thông tin hiển thị trên Apps store
        └── icon.png               # Icon module
```

---

## 🗄️ CẤU TRÚC DỮ LIỆU (MODELS)

### 1. Master Data Models

| STT | Model (Technical Name) | Class (Python) | File | Mô tả | Key Fields | Relations |
|-----|----------------------|----------------|------|-------|------------|-----------|
| 1 | `repair.device` | `RepairDevice` | `models/device.py` | Thiết bị (Gốc). Đối tượng trung tâm cần quản lý (Điện thoại, Laptop...) | `name` (Serial/IMEI - Unique), `model_name` (Char), `purchase_date` (Date), `warranty_status` (Computed), `image` (Binary) | `owner_id` (M2O res.partner), `brand_id` (M2O repair.brand), `history_ids` (O2M) |
| 2 | `repair.brand` | `RepairBrand` | `models/device_brand.py` | Hãng sản xuất. Quản lý thương hiệu (Apple, Samsung, Dell...) | `name` (Char), `icon` (Binary) | `model_ids` (O2M repair.model) |
| 3 | `repair.model` | `RepairModel` | `models/device_brand.py` | Dòng máy (Model). Chi tiết dòng máy (iPhone 13, Galaxy S24...) | `name` (Char), `release_year` (Integer) | `brand_id` (M2O repair.brand), `device_ids` (O2M repair.device) |
| 4 | `res.partner` (Inherit) | `ResPartner` | `models/res_partner.py` | Khách hàng. Kế thừa để quản lý chủ sở hữu thiết bị | `device_count` (Computed - Đếm số thiết bị) | `device_ids` (O2M repair.device - Danh sách thiết bị sở hữu) |
| 5 | `product.template` (Inherit) | `ProductTemplate` | `models/product.py` | Linh kiện & Dịch vụ. Kế thừa để phân biệt hàng thay thế và công sửa | `is_repair_part` (Boolean), `list_price` (Float - Giá bán), `standard_price` (Float - Giá vốn) | Không thay đổi quan hệ gốc |

### 2. Operations Models

| STT | Model (Technical Name) | Class (Python) | File | Mô tả | Key Fields | Relations |
|-----|----------------------|----------------|------|-------|------------|-----------|
| 6 | `repair.order` | `RepairOrder` | `models/repair_order.py` | Phiếu Sửa chữa (Header). Chứng từ giao dịch chính. Quản lý trạng thái và tổng tiền | `name` (Seq - Readonly), `state` (Selection), `date_receipt` (Date - Nhận), `deadline` (Date - Hẹn trả), `amount_total` (Monetary) | `partner_id` (M2O), `device_id` (M2O), `technician_id` (M2O res.users), `line_ids` (O2M) |
| 7 | `repair.line` | `RepairLine` | `models/repair_order.py` | Chi tiết Vật tư/Công. Các dòng chi tiết trong phiếu sửa chữa | `product_uom_qty` (Float), `price_unit` (Float), `price_subtotal` (Computed) | `order_id` (M2O repair.order), `product_id` (M2O product.product) |
| 9 | `repair.appointment` | `RepairAppointment` | `models/repair_appointment.py` | Lịch hẹn. Quản lý việc khách đặt lịch mang máy đến | `name` (Seq), `appointment_date` (Datetime), `note` (Text) | `partner_id` (M2O), `device_id` (M2O) |

### 3. History Models

| STT | Model (Technical Name) | Class (Python) | File | Mô tả | Key Fields | Relations |
|-----|----------------------|----------------|------|-------|------------|-----------|
| 8 | `repair.history` | `RepairHistory` | `models/repair_history.py` | Lịch sử sự cố. Ghi nhận chi tiết các lần hư hỏng của thiết bị | `issue_description` (Text), `diagnosis_result` (Text), `date_log` (Date) | `device_id` (M2O repair.device), `order_id` (M2O repair.order - Link tới phiếu sửa nếu có) |

### 4. Security Models

| STT | Model (Technical Name) | Class (Python) | File | Mô tả | Key Fields | Relations |
|-----|----------------------|----------------|------|-------|------------|-----------|
| 10 | `res.users` (Inherit) | `ResUsers` | `models/repair_order.py` | Kỹ thuật viên. User hệ thống chịu trách nhiệm sửa chữa | Không thêm field mới | `assigned_repair_ids` (O2M - Các phiếu đang phụ trách) |

---

## 📝 DANH SÁCH TASK THEO NHÓM CHỨC NĂNG

### 🏗️ 1. CẤU TRÚC & DỮ LIỆU NỀN (Tiết 1) - 20 điểm

| # | Task | File/Location | Chi tiết | Yêu cầu | Điểm |
|---|------|---------------|----------|---------|------|
| 1 | Khởi tạo Module | `__manifest__.py` | Tạo `__manifest__.py`. Name: `device_repair`. Depends: `['base', 'product', 'mail']` | Bắt buộc | 2 |
| 2 | Model Thiết bị (Gốc) | `models/device.py` | File: `models/device.py`. Class: `RepairDevice`. Field: `name`, `serial_number`, `image`. Logic Computed: Thêm field `warranty_status` (Trạng thái bảo hành). Dùng `@api.depends('purchase_date')`. Nếu quá 12 tháng -> "Hết hạn", ngược lại "Còn bảo hành" | Bắt buộc | 2 |
| 3 | Model Loại/Hãng | `models/device_brand.py` | File: `models/device_brand.py`. Class `DeviceBrand`, `DeviceModel`. Quan hệ: 1 Hãng (Apple) có nhiều Model (iPhone 13, iPhone 14). Quan hệ cha-con | Bắt buộc | 2 |
| 4 | Kế thừa Partner (Khách) | `models/res_partner.py` | File: `models/res_partner.py`. Inherit `res.partner`. Logic: Thêm field `device_ids` (One2many) để xem lịch sử khách hàng này sở hữu những thiết bị nào | Bắt buộc | 2 |
| 5 | Link Device về Partner | `models/device.py` | File: `models/device.py`. Field `owner_id` (Many2one). Logic Onchange: Chọn `owner_id` -> Tự fill số điện thoại khách hàng vào form Thiết bị để tiện liên lạc | Bắt buộc | 2 |
| 6 | Kế thừa Product (Linh kiện) | `models/product.py` | File: `models/product.py`. Inherit `product.template`. Logic: Thêm field `is_parts` (Boolean) để lọc đâu là Linh kiện thay thế (Màn hình, Pin), đâu là Dịch vụ (Công thợ) | Bắt buộc | 2 |
| 7 | View Thiết bị (Form) | `views/device_views.xml` | XML: `views/device_views.xml`. UI/UX: Form hiển thị ảnh thiết bị, Số Serial, Nhóm thông tin "Chủ sở hữu" và "Thông tin kỹ thuật" | Bắt buộc | 2 |
| 8 | View Thiết bị (List) | `views/device_views.xml` | XML: `views/device_views.xml`. Tree view + Search view. Search Logic: Tìm theo Số Serial, Tên Chủ, Tên Model. Filter: "Máy hết bảo hành" | Bắt buộc | 2 |
| 9 | View Kế thừa Partner | `views/res_partner_views.xml` | XML: `views/res_partner_views.xml`. UI/UX: Thêm Tab "Thiết bị sở hữu" trong hồ sơ khách hàng. Hiển thị list máy của họ | Bắt buộc | 2 |
| 10 | View Kế thừa Product | `views/product_views.xml` | XML: `views/product_views.xml`. UI/UX: Thêm checkbox "Is Repair Part" vào form Product | Bắt buộc | 2 |

---

### 🔧 2. KỸ THUẬT & LỊCH SỬ (Tiết 2) - 20 điểm

| # | Task | File/Location | Chi tiết | Yêu cầu | Điểm |
|---|------|---------------|----------|---------|------|
| 1 | Model Kiểm tra (Checklist) | `models/repair_diagnosis.py` | File: `models/repair_diagnosis.py`. Class: `RepairDiagnosis`. Logic: Danh sách các hạng mục cần test (Loa, Mic, Màn hình, Cảm ứng) trước khi nhận máy | Bắt buộc | 2 |
| 2 | Model Lịch sử sự cố | `models/repair_history.py` | File: `models/repair_history.py`. Class `RepairHistory`. Logic: Ghi nhận ngày lỗi, mô tả lỗi, hình ảnh lỗi, kỹ thuật viên tiếp nhận | Bắt buộc | 2 |
| 3 | Link Lịch sử vào Device | `models/device.py` | File: `models/device.py`. One2many `history_ids`. Logic: Hiển thị toàn bộ lịch sử hư hỏng/sửa chữa ngay trên form Thiết bị | Bắt buộc | 2 |
| 4 | Embed View Kỹ thuật | `views/device_views.xml` | XML: `views/device_views.xml`. UI/UX: Dùng Notebook chia tab: "Thông tin chung", "Lịch sử lỗi", "Lịch sử thay thế linh kiện" | Bắt buộc | 2 |
| 5 | Logic Mã tự động | `data/ir_sequence_data.xml` | File: `data/ir_sequence_data.xml`. Logic SQL Constraints: Mã thiết bị (IMEI/Serial) phải là duy nhất. Sequence sinh mã nội bộ: DEV/00001 | Bắt buộc | 2 |
| 6 | Model Lịch hẹn | `models/repair_appointment.py` | File: `models/repair_appointment.py`. Class `RepairAppointment`. Logic: Khách đặt lịch mang máy đến sửa. Field: Ngày hẹn, Khách, Máy, Mô tả lỗi sơ bộ | Bắt buộc | 2 |
| 7 | Calendar View | `views/repair_appointment_views.xml` | XML: `views/repair_appointment_views.xml`. UI/UX: Hiển thị lịch tiếp nhận máy cho Lễ tân/Kỹ thuật viên theo dõi | Bắt buộc | 2 |
| 8 | Kanban View | `views/device_views.xml` | XML: `views/device_views.xml`. UI/UX: Hiển thị danh sách Thiết bị dạng thẻ, có ảnh đại diện, màu sắc phân biệt Hãng sx | Bắt buộc | 2 |
| 9 | Smart Button (Partner) | `views/res_partner_views.xml` | XML: `res.partner`. Logic Smart Button: Đếm số lượng thiết bị của khách. Bấm vào -> Link sang list thiết bị của khách đó | Không bắt buộc | 2 |
| 10 | Smart Button (Device) | `views/device_views.xml` | XML: `repair.device`. Logic Smart Button: Đếm số lần sửa chữa (`repair_count`). Bấm vào -> Xem lịch sử các phiếu sửa chữa | Không bắt buộc | 2 |

---

### 💰 3. GIAO DỊCH (REPAIR ORDER) (Tiết 3) - 20 điểm

| # | Task | File/Location | Chi tiết | Yêu cầu | Điểm |
|---|------|---------------|----------|---------|------|
| 1 | Model Repair Header | `models/repair_order.py` | File: `models/repair_order.py`. Class: `RepairOrder`. Logic: Phiếu sửa chữa (tương tự Hóa đơn). Thông tin: Khách, Máy, Ngày nhận, Hạn trả | Bắt buộc | 2 |
| 2 | Model Repair Line | `models/repair_order.py` | File: `models/repair_order.py`. Class `RepairLine`. Logic: Chi tiết vật tư/công thợ. Field: `product_id`, `qty`, `price_unit`, `subtotal` | Bắt buộc | 2 |
| 3 | Compute Line Subtotal | `models/repair_order.py` | Python: `_compute_subtotal`. Logic Computed: Thành tiền = Số lượng * Đơn giá. Dùng `@api.depends`. `Store=True` | Bắt buộc | 2 |
| 4 | Compute Header Total | `models/repair_order.py` | Python: `_compute_total`. Logic Computed: Tổng phiếu = Tổng các dòng chi tiết. Tự động cập nhật khi thêm bớt linh kiện | Bắt buộc | 2 |
| 5 | Onchange Product | `models/repair_order.py` | Python: `_onchange_product_id`. Logic Onchange: Khi chọn Linh kiện -> Tự động điền Giá bán vào ô Đơn giá | Bắt buộc | 2 |
| 6 | Onchange Partner | `models/repair_order.py` | Python: `_onchange_partner_id`. Logic Onchange: Chọn Khách hàng -> Tự gợi ý danh sách Thiết bị (domain filter) của khách đó | Không bắt buộc | 2 |
| 7 | View Order Form | `views/repair_order_views.xml` | XML: `repair_order_views.xml`. UI/UX: Widget `section_and_note_one2many` để nhập liệu linh kiện đẹp như hóa đơn bán hàng | Bắt buộc | 2 |
| 8 | View Order Tree | `views/repair_order_views.xml` | XML: `repair_order_views.xml`. UI/UX: List view hiển thị: Mã phiếu, Khách, Máy, Tổng tiền, Trạng thái (Màu sắc) | Bắt buộc | 2 |
| 9 | Validation (Date) | `models/repair_order.py` | Python: `@api.constrains('deadline_date')`. Logic Validation: Ngày hẹn trả máy (deadline) phải lớn hơn hoặc bằng Ngày tiếp nhận | Bắt buộc | 2 |
| 10 | Validation (Qty) | `models/repair_order.py` | Python: `@api.constrains('product_uom_qty')`. Logic Validation: Số lượng linh kiện thay thế không được âm | Bắt buộc | 2 |

---

### 🔄 4. QUY TRÌNH (WORKFLOW) (Tiết 4) - 20 điểm

| # | Task | File/Location | Chi tiết | Yêu cầu | Điểm |
|---|------|---------------|----------|---------|------|
| 1 | Workflow States | `models/repair_order.py` | Python: `state` Selection. Logic: Mới -> Kiểm tra (Diagnose) -> Báo giá -> Đang sửa -> Hoàn thành -> Trả máy | Bắt buộc | 2 |
| 2 | Buttons Logic (Confirm) | `models/repair_order.py` | Python: `action_quote`, `action_start`, `action_done`. Logic: Các nút bấm chuyển trạng thái tương ứng trên thanh Header | Bắt buộc | 2 |
| 3 | View Statusbar | `views/repair_order_views.xml` | XML: Form Repair Order. UI/UX: Header chứa thanh trạng thái (statusbar) và các nút bấm (object type) | Bắt buộc | 2 |
| 4 | Tích hợp Chatter | `models/repair_order.py` | Python: `_inherit = ['mail.thread']`. Logic: Hiện khung chat, log ghi chú. Gửi tin nhắn trao đổi nội bộ về tình trạng máy | Bắt buộc | 2 |
| 5 | Tracking Fields | `models/repair_order.py` | Python: `tracking=True` vào field `state`. Logic: Tự động ghi log "Kỹ thuật viên A đã đổi trạng thái từ Đang sửa sang Hoàn thành" | Bắt buộc | 2 |
| 6 | Logic Update Device | `models/repair_order.py` | Python: Hàm `action_done`. Logic: Khi phiếu Hoàn thành -> Tự động cập nhật "Ngày sửa gần nhất" vào hồ sơ Thiết bị | Bắt buộc | 2 |
| 7 | Logic Raise Error | `models/repair_order.py` | Python: Hàm `action_cancel`. Logic: Không được hủy phiếu khi đã thay linh kiện (Đã xuất kho/Đang sửa). Chỉ hủy khi ở nháp | Không bắt buộc | 2 |
| 8 | Readonly Logic | `views/repair_order_views.xml` | XML: Form Repair Order. Logic UI: Khi trạng thái là "Hoàn thành/Trả máy", khóa toàn bộ form (readonly) | Bắt buộc | 2 |
| 9 | Smart Button (Device) | `views/device_views.xml` | XML: Form Device. Logic Smart Button: Nút "Lịch sử Sửa chữa". Bấm vào xem danh sách các Repair Order của máy này | Không bắt buộc | 2 |
| 10 | Menu Organization | `views/menus.xml` | XML: `menus.xml`. Logic: Sắp xếp menu: Trung tâm Sửa chữa / Phiếu sửa / Thiết bị / Báo cáo / Cấu hình | Bắt buộc | 2 |

---

### 📊 5. BÁO CÁO & BẢO MẬT (Tiết 5) - 20 điểm

| # | Task | File/Location | Chi tiết | Yêu cầu | Điểm |
|---|------|---------------|----------|---------|------|
| 1 | Nhóm quyền (Groups) | `security/repair_security.xml` | XML: `repair_security.xml`. Logic: 2 Nhóm: Technician (Kỹ thuật - Xem/Sửa phiếu được giao) và Manager (Quản lý) | Bắt buộc | 2 |
| 2 | Phân quyền (CSV) | `security/ir.model.access.csv` | File: `ir.model.access.csv`. Logic: Cấp quyền CRUD cho từng model. User không được xóa phiếu sửa chữa | Bắt buộc | 2 |
| 3 | Pivot View (Doanh thu) | `views/repair_order_views.xml` | XML: `repair_order_views.xml`. Báo cáo: Tổng doanh thu theo Tháng / Theo Hãng (Apple, Samsung) / Theo Kỹ thuật viên | Bắt buộc | 2 |
| 4 | Graph View (Bar) | `views/repair_order_views.xml` | XML: `repair_order_views.xml`. Báo cáo: Biểu đồ cột: So sánh số lượng máy sửa chữa giữa các Hãng | Bắt buộc | 2 |
| 5 | Graph View (Pie) | `views/repair_order_views.xml` | XML: `repair_order_views.xml`. Báo cáo: Biểu đồ tròn: Tỉ trọng doanh thu từ Linh kiện vs Tiền công sửa chữa | Bắt buộc | 2 |
| 6 | Search View | `views/repair_order_views.xml` | XML: Search View. Logic: Bộ lọc: "Phiếu quá hạn", "Đang chờ linh kiện". Group By: "Trạng thái" | Bắt buộc | 2 |
| 7 | Record Rules | `security/repair_security.xml` | XML: `repair_security.xml`. Logic Bảo mật: Kỹ thuật viên chỉ thấy Phiếu mình phụ trách hoặc tạo. Manager thấy tất cả | Không bắt buộc | 3 |
| 8 | Field Permission | `views/product_views.xml` | XML: Form Product. Logic Bảo mật: Chỉ Manager mới nhìn thấy field "Giá vốn" (`standard_price`) của linh kiện | Không bắt buộc | 3 |
| 9 | Dữ liệu Demo | `data/demo_data.xml` | File: `data/demo_data.xml`. Logic: Tạo sẵn 5 Thiết bị mẫu (iPhone, Dell XPS...), 3 Dịch vụ, 2 Khách hàng | Không bắt buộc | 2 |

---

## 🎯 WORKFLOW STATES

**Trạng thái phiếu sửa chữa:**
1. **Mới** (Draft) - Phiếu vừa tạo
2. **Kiểm tra** (Diagnose) - Đang kiểm tra lỗi
3. **Báo giá** (Quoted) - Đã báo giá cho khách
4. **Đang sửa** (In Progress) - Đang thực hiện sửa chữa
5. **Hoàn thành** (Done) - Đã sửa xong
6. **Trả máy** (Returned) - Đã trả máy cho khách

---

## 🔐 PHÂN QUYỀN

### Groups
1. **Technician** (Kỹ thuật viên)
   - Xem/Sửa phiếu được giao
   - Chỉ thấy phiếu mình phụ trách hoặc tạo

2. **Manager** (Quản lý)
   - Xem tất cả phiếu
   - Xem được field "Giá vốn" (`standard_price`)
   - Toàn quyền quản lý

### Record Rules
- Kỹ thuật viên: Chỉ thấy phiếu mình phụ trách hoặc tạo
- Manager: Thấy tất cả phiếu
- User không được xóa phiếu sửa chữa

---

## 📈 BÁO CÁO

1. **Pivot View - Doanh thu:**
   - Tổng doanh thu theo Tháng
   - Tổng doanh thu theo Hãng (Apple, Samsung...)
   - Tổng doanh thu theo Kỹ thuật viên

2. **Graph View - Bar:**
   - So sánh số lượng máy sửa chữa giữa các Hãng

3. **Graph View - Pie:**
   - Tỉ trọng doanh thu từ Linh kiện vs Tiền công sửa chữa

---

## 🚀 BƯỚC TIẾP THEO

1. ✅ Tạo cấu trúc thư mục module `device_repair`
2. ✅ Tạo file `__manifest__.py`
3. ✅ Tạo các model Python trong thư mục `models/`
4. ✅ Tạo các view XML trong thư mục `views/`
5. ✅ Tạo file phân quyền trong thư mục `security/`
6. ✅ Tạo dữ liệu sequence và demo trong thư mục `data/`
7. ✅ Tạo menu trong `views/menus.xml`
8. ✅ Test và debug module

---

## 📌 LƯU Ý QUAN TRỌNG

- **Tên module:** `device_repair` (không có dấu gạch ngang)
- **Dependencies:** `base`, `product`, `mail` (bắt buộc)
- **Mã thiết bị:** Phải unique (SQL Constraint)
- **Sequence:** DEV/00001 (thiết bị), REP/00001 (phiếu sửa)
- **Computed Fields:** Sử dụng `@api.depends` và `store=True` khi cần
- **Validation:** Sử dụng `@api.constrains` cho các ràng buộc
- **Onchange:** Sử dụng `@api.onchange` cho logic tự động điền

---

**Tổng điểm:** 100 điểm  
**Số task:** 50 tasks  
**Deadline:** 5 tiết học
