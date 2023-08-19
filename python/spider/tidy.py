# 读取文件内容
with open('data_full.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 去除换行符并按照逗号拆分行，并将编号和元素存储为字典
data = {}
for line in lines:
    line = line.strip()
    number, element = line.split(',', maxsplit=1)
    number = int(number)
    if number not in data:
        data[number] = []
    data[number].append(element)

# 删除相同编号的元素
unique_data = {}
for number, elements in data.items():
    unique_elements = list(set(elements))
    unique_data[number] = unique_elements

# 将字典按照键（编号）进行升序排序
sorted_data = sorted(unique_data.items(), key=lambda x: x[0])

# 输出结果
with open('data_full.txt', 'w', encoding='utf-8') as file:
    for number, elements in sorted_data:
        for element in elements:
            file.write(f'{number},{element}\n')

print("\n\nFinished!!!")