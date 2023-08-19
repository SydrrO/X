import pandas as pd
import json

# 读取CSV文件，指定header为None
df = pd.read_csv('data_full.csv', encoding='utf-8', header=None)

# 构建目标JSON格式数据
output_data = {}
for index, row in df.iterrows():
    buff_index = row[0]  # 第一列为buff_index
    name = row[1]  # 第二列为name
    output_data[name] = {'buff_index': buff_index, 'yyyp_index': None}  # yyyp_index留空

# 写入JSON文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False,indent= 4)
