import json

# Đọc dữ liệu từ tệp JSON
with open("employees.json", "r") as json_file:
    data = json.load(json_file)

# Lấy thông tin về công ty
company_name = data["company_name"]
company_address = data["company_address"]
employees = data["employees"]

# Tạo một từ điển để thống kê nhân viên theo đơn vị
unit_stats = {}

# Đếm tổng số nhân viên
total_employees = len(employees)

# Thống kê nhân viên theo đơn vị
for employee in employees:
    unit = employee["unit"]
    if unit in unit_stats:
        unit_stats[unit]["count"] += 1
    else:
        unit_stats[unit] = {
            "count": 1,
            "percentage": 0.0
        }

# Tính tỷ lệ % cho từng đơn vị
for unit, stats in unit_stats.items():
    stats["percentage"] = (stats["count"] / total_employees) * 100

# In thông tin công ty
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}")
print("-----Thống kê nhân viên theo đơn vị-----")

# In thống kê nhân viên theo đơn vị
for unit, stats in unit_stats.items():
    print(f"Tên đơn vị: {unit}")
    print(f"- Số nhân viên: {stats['count']}")
    print(f"- Tỷ lệ: {stats['percentage']:.2f}%")
