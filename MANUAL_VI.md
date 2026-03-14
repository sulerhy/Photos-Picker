# Photos Picker - Hướng Dẫn Sử Dụng (Tiếng Việt)

Chào mừng bạn đến với Photos Picker! Hướng dẫn này sẽ giúp bạn sử dụng ứng dụng một cách hiệu quả.

## Mục Lục
1. [Cài Đặt](#cài-đặt)
2. [Bắt Đầu Nhanh](#bắt-đầu-nhanh)
3. [Tổng Quan Giao Diện](#tổng-quan-giao-diện)
4. [Hướng Dẫn Từng Bước](#hướng-dẫn-từng-bước)
5. [Các Tính Năng](#các-tính-năng)
6. [Cài Đặt Ngôn Ngữ](#cài-đặt-ngôn-ngữ)
7. [Xử Lý Sự Cố](#xử-lý-sự-cố)
8. [Mẹo & Thủ Thuật](#mẹo--thủ-thuật)

---

## Cài Đặt

### Windows
1. Tải `Photos_Picker_Windows.zip`
2. Giải nén tệp ZIP vào bất kỳ thư mục nào
3. Nhấp đôi `Photos Picker.exe` để chạy

### macOS
1. Tải `Photos_Picker_macOS.zip`
2. Giải nén tệp
3. Nhấp đôi `Photos Picker.app` để chạy
4. Nếu gặp lỗi "App is damaged", chạy trong Terminal:
   ```bash
   xattr -d com.apple.quarantine "Photos Picker.app"
   ```

### Linux
1. Tải `Photos_Picker_Linux.zip`
2. Giải nén và chạy: `./Photos\ Picker`

---

## Bắt Đầu Nhanh

**Hoàn thành trong 5 phút:**

1. ✅ **Chọn thư mục INPUT** - nơi lưu ảnh gốc
2. ✅ **Chọn thư mục OUTPUT** - nơi lưu ảnh được chọn
3. ✅ **Nhập số ảnh** - một số trên một dòng (ví dụ: 1234, 5678)
4. ✅ **Nhấp "Kiểm tra"** - kiểm tra ảnh nào tồn tại
5. ✅ **Nhấp "Tiến hành lọc ảnh"** - sao chép ảnh được chọn

Hoàn tất! Ảnh của bạn đã được sao chép.

---

## Tổng Quan Giao Diện

### Bố Cục Cửa Sổ Chính

```
┌─────────────────────────────────────────────────────────────┐
│  🌐 Tiếng Việt                         [Chuyển Đổi Ngôn Ngữ]
├─────────────────────────────────────────────────────────────┤
│ Phần Thư Mục INPUT                                           │
│ ├─ Đường dẫn hiện tại hoặc "Chưa chọn thư mục"             │
│ └─ [📁 Chọn INPUT]                                         │
│                                                              │
│ Phần Thư Mục OUTPUT                                          │
│ ├─ Đường dẫn hiện tại hoặc "Chưa chọn thư mục"             │
│ └─ [📁 Chọn OUTPUT]                                        │
├─────────────────────────────────────────────────────────────┤
│ Tiền tố:    [DSCF    ]  Hãng: [Fujifilm ▼]  Định dạng: [RAF ▼]│
├─────────────────────────────────────────────────────────────┤
│ PANEL TRÁI                   │ PANEL PHẢI                    │
│ Danh sách số ảnh             │ Kết quả                      │
│ ─────────────────────────    │ ─────────────────────────    │
│ [Vùng nhập văn bản]          │ ✔ 10  ✘ 2  ⚠ 1             │
│                              │ [Danh sách kết quả]          │
│ [🔍 Kiểm tra]                │                              │
├─────────────────────────────────────────────────────────────┤
│ [▶ Tiến hành lọc ảnh]  Tiến trình: 0 / 10 ảnh              │
│ [═══════════════════════] 50%                               │
│ [Vùng hiển thị nhật ký]                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Hướng Dẫn Từng Bước

### Bước 1: Chọn Thư Mục INPUT

Thư mục INPUT chứa ảnh RAW/JPEG gốc của bạn.

1. Nhấp nút **[📁 Chọn INPUT]**
2. Tìm duyệt và chọn một thư mục (ví dụ: `D:\Anh_Khach_Hang\RAW`)
3. Đường dẫn sẽ hiển thị dưới nút
4. ✅ Thư mục sẵn sàng sử dụng

**Cấu trúc thư mục ví dụ:**
```
D:\Anh_Khach_Hang\RAW\
├── DSCF0001.RAF
├── DSCF0002.RAF
├── DSCF0003.RAF
└── ...
```

### Bước 2: Chọn Thư Mục OUTPUT

Thư mục OUTPUT là nơi các ảnh được chọn sẽ được lưu.

1. Nhấp nút **[📁 Chọn OUTPUT]**
2. Chọn hoặc tạo thư mục mới (ví dụ: `D:\Anh_Khach_Hang\Da_Chon`)
3. Đường dẫn sẽ hiển thị dưới nút
4. ✅ Thư mục sẵn sàng

**Lưu ý:** Thư mục sẽ được tạo nếu chưa tồn tại.

### Bước 3: Đặt Thông Số Ảnh

Cấu hình cách đặt tên ảnh:

- **Tiền tố** - Chữ ở đầu tên ảnh (mặc định: `DSCF`)
  - Ví dụ: Nếu tiền tố là `DSCF` và số là `1234`, ứng dụng tìm `DSCF1234.RAF`

- **Hãng** - Hãng máy ảnh (Fujifilm, Canon, Nikon, v.v.)
  - Xác định định dạng tệp có sẵn

- **Định dạng** - Loại tệp (RAF, JPG, CR3, NEF, v.v.)
  - Thay đổi dựa trên hãng được chọn

**Các tổ hợp phổ biến:**
- Fujifilm + RAF
- Canon + CR3 (hoặc CR2)
- Nikon + NEF
- Sony + ARW

### Bước 4: Nhập Số Ảnh

Trong panel bên trái, nhập số ảnh:

1. Nhấp vào vùng **"Danh sách số ảnh"**
2. Nhập số, **một số trên một dòng**:
   ```
   1234
   5678
   1001
   999
   ```
3. Hoặc dán từ bảng tính (Excel, Google Sheets)
4. Mỗi dòng là một số ảnh

**Mẹo:**
- Sao chép từ Excel/Sheets và dán trực tiếp
- Khoảng trắng sẽ bị xóa
- Dòng trống bị bỏ qua
- Các số trùng lặp sẽ hiển thị trong Kết quả

### Bước 5: Kiểm Tra Ảnh

Xác minh ảnh nào tồn tại trước khi sao chép:

1. Nhấp nút **[🔍 Kiểm tra]**
2. Ứng dụng quét thư mục INPUT
3. Kết quả hiển thị trong panel bên phải:
   - **✔ OK** (xanh) - Ảnh tìm thấy, sẽ được sao chép
   - **✘ Không tìm thấy** (đỏ) - Ảnh không tìm thấy
   - **⚠ Trùng lặp** (cam) - Số ảnh xuất hiện hai lần

**Ví dụ Kết quả:**
```
✔ DSCF1234.RAF    (tìm thấy)
✔ DSCF5678.RAF    (tìm thấy)
✘ DSCF1001.RAF    (không tìm thấy)
⚠ DSCF999.RAF     (trùng lặp)
```

### Bước 6: Bắt Đầu Sao Chép

Sao chép các ảnh được chọn vào thư mục OUTPUT:

1. Kiểm tra kết quả (tùy chọn)
2. Nhấp nút **[▶ Tiến hành lọc ảnh]**
3. Thanh tiến trình hiển thị trạng thái sao chép
4. Nhật ký hiển thị từng tệp được sao chép
5. Khi hoàn tất, thư mục OUTPUT sẽ tự động mở

**Nhập nhật ký:**
```
✔ Đã sao chép: DSCF1234.RAF
✔ Đã sao chép: DSCF5678.RAF
✘ Không tìm thấy: DSCF1001.RAF
✔ Hoàn thành! Đã sao chép 2 ảnh.
```

---

## Các Tính Năng

### 1. Chuyển Đổi Ngôn Ngữ

Chuyển đổi giữa Tiếng Việt và Tiếng Anh:

- **Vị trí Nút:** Góc trên cùng bên phải
- **Hiện tại**: Hiển thị ngôn ngữ đối lập (ví dụ: "🌐 English" khi ở Tiếng Việt)
- **Nhấp để Chuyển:** Tất cả văn bản cập nhật ngay lập tức
- **Lưu lại:** Tùy chọn ngôn ngữ được lưu khi thoát

### 2. Hãng Máy Ảnh & Định Dạng

Các định dạng máy ảnh được hỗ trợ theo hãng:

| Hãng | Định dạng |
|------|-----------|
| Canon | CR3, CR2, CRW, JPG, JPEG |
| Nikon | NEF, NRW, JPG, JPEG |
| Sony | ARW, SR2, SRF, JPG, JPEG |
| Fujifilm | RAF, JPG, JPEG |
| Panasonic | RW2, RWL, JPG, JPEG |
| Olympus | ORF, JPG, JPEG |
| Pentax | PEF, DNG, JPG, JPEG |
| Leica | DNG, RWL, JPG, JPEG |
| Hasselblad | 3FR, FFF, JPG, JPEG |
| GoPro | GPR, JPG, JPEG |
| Phase One | IIQ, JPG, JPEG |
| Red | RED, JPG, JPEG |
| Sigma | X3F, JPG, JPEG |
| Blackmagic | BRAW, JPG, JPEG |

### 3. Phát Hiện Trùng Lặp

Ứng dụng ngăn chặn sao chép cùng một ảnh hai lần:

- **Đầu vào** - Nhập số `1234` hai lần
- **Kết quả Kiểm tra** - Một hiển thị ✔ (OK), một hiển thị ⚠ (Trùng lặp)
- **Sao chép** - Chỉ một bản sao được tạo

### 4. Bảo Toàn Tệp

Siêu dữ liệu gốc được bảo toàn:

- Ngày giờ tạo
- Dữ liệu EXIF
- Thuộc tính tệp

Sử dụng `shutil.copy2` (bảo toàn siêu dữ liệu trên tất cả các nền tảng).

### 5. Tương Thích Đa Nền Tảng

Hoạt động trên:
- ✅ Windows (7, 10, 11)
- ✅ macOS (10.13+)
- ✅ Linux (Ubuntu, Debian, v.v.)

---

## Cài Đặt Ngôn Ngữ

### Chuyển Đổi Ngôn Ngữ

**Phương pháp 1: Nút bấm**
- Nhấp **🌐 English** (khi ở Tiếng Việt) hoặc **🌐 Tiếng Việt** (khi ở Tiếng Anh)
- Tất cả văn bản giao diện cập nhật ngay lập tức

**Phương pháp 2: Lần đầu tiên chạy**
- Lần đầu chạy, ứng dụng sử dụng Tiếng Anh
- Chuyển sang Tiếng Việt bằng nút
- Cài đặt được lưu tự động

### Ngôn Ngữ Được Hỗ Trợ

| Ngôn Ngữ | Viết Tắt |
|----------|----------|
| Tiếng Anh | EN |
| Tiếng Việt | VI |

### Những Gì Được Dịch

✅ Tất cả nút và nhãn
✅ Thông báo lỗi
✅ Đầu ra nhật ký
✅ Tiêu đề hộp thoại
✅ Trình giữ chỗ

**Không được dịch:**
- Tên hãng máy ảnh (Canon, Nikon, v.v.)
- Mã định dạng tệp (RAF, NEF, JPG)

---

## Xử Lý Sự Cố

### Vấn Đề: "Vui lòng chọn thư mục INPUT!"

**Giải pháp:** Nhấp [📁 Chọn INPUT] và chọn thư mục chứa ảnh.

### Vấn Đề: "Vui lòng chọn thư mục OUTPUT!"

**Giải pháp:** Nhấp [📁 Chọn OUTPUT] và chọn (hoặc tạo) thư mục đích.

### Vấn Đề: "Vui lòng nhập danh sách ảnh!"

**Giải pháp:**
1. Nhập số ảnh trong vùng văn bản bên trái
2. Nhấp [🔍 Kiểm tra] trước
3. Sau đó nhấp [▶ Tiến hành lọc ảnh]

### Vấn Đề: Tất cả ảnh hiển thị "Không tìm thấy"

**Nguyên nhân:**
- Tiền tố sai (kiểm tra tên ảnh trong thư mục INPUT)
- Hãng/định dạng máy ảnh sai
- Đã chọn thư mục INPUT sai

**Giải pháp:**
1. Mở thư mục INPUT và kiểm tra tên ảnh
2. Điều chỉnh tiền tố để phù hợp (ví dụ: thay `DSCF` thành `IMG`)
3. Chọn hãng và định dạng đúng

### Vấn Đề: Ứng dụng không mở được trên macOS

**Lỗi:** "App is damaged or can't be opened"

**Giải pháp:**
```bash
xattr -d com.apple.quarantine "Photos Picker.app"
```

Hoặc trong System Preferences > Security & Privacy, cho phép ứng dụng.

### Vấn Đề: Thư mục OUTPUT trống

**Nguyên nhân:**
- Không có ảnh nào được đánh dấu là ✔ OK trong kết quả Kiểm tra
- Hoạt động sao chép không hoàn thành

**Giải pháp:**
1. Chạy Kiểm tra lại
2. Xác minh kết quả hiển thị mục ✔ OK
3. Đảm bảo thư mục OUTPUT có thể ghi được
4. Thử sao chép vào vị trí khác

### Vấn Đề: Tên ảnh không khớp

**Ví dụ:**
- Tệp: `DSCF1234.RAF`
- Nhập: `1234`
- Tiền tố: `DSCF` ✓ Đúng
- Định dạng: `RAF` ✓ Đúng
- Nhưng vẫn hiển thị "Không tìm thấy"

**Giải pháp:**
- Kiểm tra khoảng trắng: tệp có thể là `DSCF 1234.RAF` (có khoảng trắng)
- Xác minh tên tệp chính xác trong thư mục INPUT
- Sao chép tên tệp chính xác từ Explorer/Finder

### Vấn Đề: Phát hiện trùng lặp không hoạt động

**Ví dụ:**
- Nhập: `1234`, `1234` (cùng số hai lần)
- Cả hai đều hiển thị ✔ OK thay vì hiển thị một là trùng lặp

**Giải pháp:** Điều này không nên xảy ra. Thử:
1. Nhấp [🔍 Kiểm tra] lại
2. Khởi động lại ứng dụng
3. Nhập lại số cẩn thận

---

## Mẹo & Thủ Thuật

### Mẹo 1: Sử Dụng Đầu Vào Bảng Tính

Sao chép-dán từ Excel/Google Sheets:

1. Trong bảng tính, chọn cột số ảnh
2. Sao chép (Ctrl+C hoặc Cmd+C)
3. Trong Photos Picker, nhấp vùng văn bản
4. Dán (Ctrl+V hoặc Cmd+V)

### Mẹo 2: Lưu Cài Đặt

Ứng dụng nhớ:
- Thư mục được sử dụng lần cuối
- Giá trị tiền tố
- Hãng và định dạng được chọn
- Tùy chọn ngôn ngữ

Tiết kiệm thời gian lần sử dụng tiếp theo!

### Mẹo 3: Kiểm Tra Trước Khi Sao Chép

Luôn nhấp [🔍 Kiểm tra] trước [▶ Bắt đầu]:
- Xem ảnh nào sẽ được sao chép
- Xác minh số được nhập đúng
- Tránh sao chép những ảnh sai

### Mẹo 4: Xử Lý Các Ảnh Bị Thiếu

Nếu một số ảnh hiển thị ✘ Không tìm thấy:

**Tùy chọn 1:** Hỏi khách hàng để xác nhận số
**Tùy chọn 2:** Kiểm tra thư mục INPUT có tên tương tự
**Tùy chọn 3:** Thử tiền tố hoặc định dạng khác

### Mẹo 5: Hoạt Động Hàng Loạt

Để xử lý nhiều khách hàng:

1. Sao chép số khách hàng 1 → Kiểm tra → Sao chép
2. Xóa vùng văn bản
3. Nhập số khách hàng 2 → Kiểm tra → Sao chép
4. Lặp lại cho từng khách hàng

### Mẹo 6: Tìm Ảnh Dễ Dàng

Nếu bạn không biết số chính xác:

1. Mở thư mục INPUT
2. Sắp xếp theo tên hoặc ngày
3. Xác định tên ảnh
4. Nhập các số đó

---

## Phím Tắt Bàn Phím

| Phím Tắt | Hành Động |
|----------|-----------|
| Ctrl+A (Cmd+A trên Mac) | Chọn tất cả văn bản trong danh sách ảnh |
| Ctrl+C (Cmd+C) | Sao chép văn bản được chọn |
| Ctrl+V (Cmd+V) | Dán số ảnh |

---

## Nhận Trợ Giúp

**Vẫn gặp sự cố?**

1. Kiểm tra hướng dẫn này lại (sử dụng Ctrl+F để tìm kiếm)
2. Xác minh đường dẫn thư mục INPUT và tên ảnh
3. Thử khởi động lại ứng dụng
4. Kiểm tra yêu cầu hệ thống (Python 3.8+, 500MB dung lượng đĩa)

---

## Yêu Cầu Hệ Thống

- **Windows**: 7 hoặc mới hơn, 500MB dung lượng đĩa
- **macOS**: 10.13 hoặc mới hơn, 500MB dung lượng đĩa
- **Linux**: Ubuntu 18.04+, 500MB dung lượng đĩa
- **RAM**: 2GB tối thiểu (4GB được khuyến nghị)
- **Python**: 3.8+ (để phát triển)

---

## Thông Tin Phiên Bản

- **Phiên bản**: 1.0.0
- **Cập nhật lần cuối**: Tháng 3 năm 2026
- **Ngôn Ngữ**: Tiếng Anh, Tiếng Việt
- **Nền Tảng**: Windows, macOS, Linux

---

## Giấy Phép

Photos Picker được cung cấp dưới dạng nguyên trạng cho mục đích sử dụng cá nhân và chuyên nghiệp.

---

**Cảm ơn bạn đã sử dụng Photos Picker!**

Nếu có phản hồi hoặc gợi ý, vui lòng cho tôi biết.
