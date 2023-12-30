import requests
import xml.etree.ElementTree as ET
import csv

# URL của RSS feed
rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

# Tải dữ liệu RSS từ URL và lưu vào tệp XML
response = requests.get(rss_url)
if response.status_code == 200:
    with open("rss_feed.xml", "wb") as file:
        file.write(response.content)

# Phân tích cú pháp tệp XML
tree = ET.parse("rss_feed.xml")
root = tree.getroot()

# Tạo danh sách lưu trữ các mục tin tức dưới dạng từ điển
news_items = []

# Duyệt qua các mục tin tức và lưu chúng vào danh sách
for item in root.findall(".//item"):
    news_item = {
        "title": item.find("title").text,
        "link": item.find("link").text,
        "description": item.find("description").text,
        "pubDate": item.find("pubDate").text
    }
    news_items.append(news_item)

# Lưu danh sách mục tin tức vào tệp CSV
csv_filename = "news_feed.csv"
csv_fields = ["title", "link", "description", "pubDate"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    writer.writeheader()
    writer.writerows(news_items)

print(f"Dữ liệu đã được lưu vào tệp CSV: {csv_filename}")
