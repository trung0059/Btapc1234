import xml.dom.minidom
# Tải và phân tích file XML
doc = xml.dom.minidom.parse("sample.xml")
# Lấy nút gốc
company = doc.documentElement #trả về company 
# Lấy thông tin về nhân viên
nhanvien = company.getElementsByTagName("staff")
for staff in nhanvien:
    id = staff.getAttribute("id")    
    name = staff.getElementsByTagName("name")[0].childNodes[0].data
    #sử dụng childnodes[0] để lấy nút con của phàn tử Name, sử dụng [0] để lấy phần thử đầu tiên

    salary = staff.getElementsByTagName("salary")[0].childNodes[0].data

    print("Nhân viên (ID:{}) - Tên: {}, Lương: {}".format(id, name, salary))