class hinh_chu_nhat:
    chieu_dai=int(input("nhập chiều dài của hình chữ nhật là :"))
    chieu_rong=int(input("nhập chiều rộng của hình chữ nhật là : "))
    chu_vi_hcn = (chieu_dai+chieu_rong)*2
    dien_tich_hcn = chieu_dai*chieu_rong
    def display(self):
        print("chiều dài của hình chữ nhật là ",self.chieu_dai)
        print("chiều rộng của hình chữ nhật là ",self.chieu_rong)
        print("diện tích hình chữ nhật là ",self.dien_tich_hcn)
        print("chu vi hình chữ nhật là ", self.chu_vi_hcn)
hcn1=hinh_chu_nhat()
hcn1.display()