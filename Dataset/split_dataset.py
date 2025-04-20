import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("Dataset/ticket_sales_cleaned.csv")

# Sắp xếp theo thời gian để đảm bảo thứ tự chuỗi thời gian
df = df.sort_values('date').reset_index(drop=True)

# Tính số dòng cho từng tập
n = len(df)
train_end = int(n * 0.7)
valid_end = train_end + int(n * 0.1)

# Chia dữ liệu
df_train = df.iloc[:train_end]
df_valid = df.iloc[train_end:valid_end]
df_test = df.iloc[valid_end:]

# Xuất kích thước mỗi tập
print("Train size:", len(df_train))
print("Validation size:", len(df_valid))
print("Test size:", len(df_test))

# (Tuỳ chọn) Lưu thành các file CSV riêng nếu muốn
df_train.to_csv("Dataset/712/train.csv", index=False)
df_valid.to_csv("Dataset/712/validation.csv", index=False)
df_test.to_csv("Dataset/712/test.csv", index=False)
