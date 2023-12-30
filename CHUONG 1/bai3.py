class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def kiem_tra(self):
        if self.mau == 0:
            return False
        return True
    def show(self):
        if self.tu == 0:
            print(0)
        else:
            print(self.tu, " /", self.mau)
def main():
    a = int(input("nhập tử số: "))
    b = int(input("nhập mẫu số: "))
    c = PS(a,b)
    if c.kiem_tra():
        c.show()
    else:
        print("bạn không thể nhập mẫu số là 0, vui lòng nhập lại")
        main()
if __name__ == '__main__':
    main()