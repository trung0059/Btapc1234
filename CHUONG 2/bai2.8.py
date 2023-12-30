import json

# Tạo một từ điển Python (sắp xếp theo khóa)
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Chuyển đổi từ điển thành chuỗi JSON với mức thụt lề 4
json_string = json.dumps(my_dict, indent=4)

# In ra chuỗi JSON với thụt lề 4
print(json_string)
