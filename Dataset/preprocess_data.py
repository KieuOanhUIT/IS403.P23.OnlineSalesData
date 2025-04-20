import pandas as pd

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

# Xoá cột date nếu không cần
df = df.drop(columns=["date"])

# Xuất file kết quả
df.to_csv("Dataset/ticket_sales_cleaned.csv", index=False)

print("Xử lý xong! In vài dòng đầu:")
print(df.head())
