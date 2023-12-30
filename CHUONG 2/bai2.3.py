import xml.dom.minidom
# Tải và phân tích tài liệu XML từ tệp "sample.xml"
doc = xml.dom.minidom.parse("sample.xml")
# Lấy danh sách các phần tử từ tài liệu XML
elements = doc.getElementsByTagName("*")
# In ra tên của từng phần tử
for element in elements:
    print("Tên phần tử:", element.tagName)
