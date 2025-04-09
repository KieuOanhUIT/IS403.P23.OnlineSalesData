import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("Dataset/online_sales_dataset_cleaned.csv", parse_dates=['InvoiceDate'])

# Sắp xếp theo thời gian để đảm bảo đúng chuỗi thời gian
df = df.sort_values('InvoiceDate').reset_index(drop=True)

# Tính toán kích thước các tập
total_len = len(df)
train_size = int(0.7 * total_len)
valid_size = int(0.1 * total_len)

# Cắt tập dữ liệu theo tỷ lệ 7:1:2
train_df = df.iloc[:train_size]
valid_df = df.iloc[train_size:train_size + valid_size]
test_df = df.iloc[train_size + valid_size:]

# Xuất ra các file CSV
train_df.to_csv("Dataset/712/train.csv", index=False)
valid_df.to_csv("Dataset/712/valid.csv", index=False)
test_df.to_csv("Dataset/712/test.csv", index=False)
