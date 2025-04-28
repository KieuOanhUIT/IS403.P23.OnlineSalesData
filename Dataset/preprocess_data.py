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

# Xuất file kết quả
df.to_csv("Dataset/ticket_sales_cleaned.csv", index=False)

print("Xử lý xong! In vài dòng đầu:")
print(df.head())

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