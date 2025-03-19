from SinhVien import QuanLySinhVien

def menu():
    qlsv = QuanLySinhVien()
    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp danh sách sinh viên theo điểm trung bình")
        print("6. Sắp xếp danh sách sinh viên theo tên chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            ten = input("Nhập tên: ")
            gioi_tinh = input("Nhập giới tính: ")
            chuyen_nganh = input("Nhập chuyên ngành: ")
            diem_trung_binh = float(input("Nhập điểm trung bình: "))
            qlsv.them_sinh_vien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        elif choice == '2':
            id = int(input("Nhập ID sinh viên: "))
            ten = input("Nhập tên mới (bỏ qua nếu không thay đổi): ")
            gioi_tinh = input("Nhập giới tính mới (bỏ qua nếu không thay đổi): ")
            chuyen_nganh = input("Nhập chuyên ngành mới (bỏ qua nếu không thay đổi): ")
            diem_trung_binh = input("Nhập điểm trung bình mới (bỏ qua nếu không thay đổi): ")
            diem_trung_binh = float(diem_trung_binh) if diem_trung_binh else None
            if qlsv.cap_nhat_sinh_vien(id, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
                print("Cập nhật thành công.")
            else:
                print("Không tìm thấy sinh viên với ID đã nhập.")
        elif choice == '3':
            id = int(input("Nhập ID sinh viên: "))
            qlsv.xoa_sinh_vien(id)
            print("Xóa thành công.")
        elif choice == '4':
            ten = input("Nhập tên sinh viên cần tìm: ")
            ket_qua = qlsv.tim_kiem_sinh_vien(ten)
            if ket_qua:
                for sv in ket_qua:
                    print(sv)
            else:
                print("Không tìm thấy sinh viên với tên đã nhập.")
        elif choice == '5':
            qlsv.sap_xep_theo_diem_trung_binh()
            print("Sắp xếp thành công.")
        elif choice == '6':
            qlsv.sap_xep_theo_chuyen_nganh()
            print("Sắp xếp thành công.")
        elif choice == '7':
            qlsv.hien_thi_danh_sach()
        elif choice == '8':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()