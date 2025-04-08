import pandas as pd
from sklearn.model_selection import train_test_split

# Đọc dữ liệu đã được tiền xử lý
df = pd.read_csv('Dataset/online_sales_dataset_cleaned.csv')

# 1. Tỷ lệ 6:2:2
train_60, temp_40 = train_test_split(df, test_size=0.4, random_state=42)
valid_20, test_20 = train_test_split(temp_40, test_size=0.5, random_state=42)

# Lưu các tập dữ liệu
train_60.to_csv('Dataset/622/train_60.csv', index=False)
valid_20.to_csv('Dataset/622/valid_20.csv', index=False)
test_20.to_csv('Dataset/622/test_20.csv', index=False)

# 2. Tỷ lệ 7:1:2
train_70, temp_30 = train_test_split(df, test_size=0.3, random_state=42)
valid_10, test_20_v2 = train_test_split(temp_30, test_size=2/3, random_state=42)  # 20/30 = 2/3

# Lưu các tập dữ liệu
train_70.to_csv('Dataset/712/train_70.csv', index=False)
valid_10.to_csv('Dataset/712/valid_10.csv', index=False)
test_20_v2.to_csv('Dataset/712/test_20_v2.csv', index=False)
