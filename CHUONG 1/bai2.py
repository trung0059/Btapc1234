class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print("Họ tên: " ,self.ho_ten)
        print("Điểm Toán: ",self.diem_toan)
        print("Điểm Lý: ",self.diem_ly)
        print("Điểm Hóa: ",self.diem_hoa)
        print("Tổng điểm: ",self.tinh_tong_diem())

def main():
    so_luong_thisinh = int(input("Nhập số lượng thí sinh: "))
    danh_sach_thi_sinh = []

    for i in range(so_luong_thisinh):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        thi_sinh = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach_thi_sinh.append(thi_sinh)

    diem_chuan = 20
    print("Danh sách thí sinh trúng tuyển:")
    for ts in danh_sach_thi_sinh:
        if ts.tinh_tong_diem() >= diem_chuan:
            ts.in_thong_tin()
            print()

if __name__ == "__main__":
    main()
