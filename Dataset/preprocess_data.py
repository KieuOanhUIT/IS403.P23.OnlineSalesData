import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV
df = pd.read_csv("Dataset/cinemaTicket_Ref.csv")

# Xoá dòng trùng lặp hoàn toàn
df = df.drop_duplicates()

# Xoá dòng có bất kỳ giá trị nào bị thiếu
df = df.dropna()

# Làm sạch khoảng trắng đầu cuối
df["date"] = df["date"].astype(str).str.strip()

# Chuyển trực tiếp sang datetime
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# In ra để kiểm tra xem có bị None không
print("Date sau extract:", df["date"].unique()[:5])

# Sắp xếp theo ngày
df = df.sort_values(by="date").reset_index(drop=True)

# Loại bỏ dòng có date bị NaT sau khi chuyển đổi
df = df.dropna(subset=["date"])

# Tách năm ra thành cột mới (kiểu int)
df["year"] = df["date"].dt.year.astype(int)

# Gộp dữ liệu theo ngày
grouped = df.groupby("date", as_index=False).agg({
    'total_sales': 'sum',           # Tổng doanh thu trong ngày
    'tickets_sold': 'sum',          # Tổng số vé bán
    'tickets_out': 'sum',           # Tổng số vé xuất
    'show_time': 'sum',             # Tổng số suất chiếu
    'occu_perc': 'mean',            # Trung bình % ghế sử dụng
    'ticket_price': 'mean',         # Trung bình giá vé
    'ticket_use': 'sum',            # Tổng số vé sử dụng
    'capacity': 'mean',             # Trung bình sức chứa rạp
    'film_code': 'first',           
    'cinema_code': 'nunique',       # Đếm số rạp chiếu khác nhau trong ngày
    'month': 'first',               # Giữ nguyên tháng
    'quarter': 'first',             # Giữ nguyên quý
    'day': 'first',                 # Giữ nguyên ngày trong tháng
    'year': 'first'                 
})

# Vẽ biểu đồ doanh thu theo thời gian
plt.figure(figsize=(14, 6))
sns.lineplot(x='date', y='total_sales', data=df)
plt.title('Doanh thu phim theo thời gian', fontsize=18)
plt.xlabel('Ngày', fontsize=14)
plt.ylabel('Doanh thu (VND)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Xuất dữ liệu ra file CSV mới
grouped.to_csv("Dataset/cleaned_data.csv", index=False)

print(result)

print("Đã lưu kết quả vào file 'cleaned_data.csv'")