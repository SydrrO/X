import json

# 从输出的JSON文件中读取数据
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取需要处理的name
name_to_update = input("请输入要处理的name：")

# 检查是否存在该name对应的键值
if name_to_update in data:
    yyyp_index = input(f"请输入{name_to_update}的yyyp_index值：")
    try:
        yyyp_index = int(yyyp_index)
    except ValueError:
        yyyp_index = None
    data[name_to_update]['yyyp_index'] = yyyp_index
    print(f"已更新{name_to_update}的yyyp_index为：{yyyp_index}")
else:
    buff_index = ''  # 新增键的buff_index留空
    yyyp_index = input(f"请输入{name_to_update}的yyyp_index值：")
    try:
        yyyp_index = int(yyyp_index)
    except ValueError:
        yyyp_index = None
    data[name_to_update] = {'buff_index': buff_index, 'yyyp_index': yyyp_index}
    print(f"已新增{name_to_update}的键值对：{name_to_update}:{yyyp_index}")

# 写入更新后的数据到同一文件中
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 生成日志记录
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(f"更新{name_to_update}的yyyp_index为：{yyyp_index}\n")
