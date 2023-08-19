import urllib.request,re,time
import urllib.error
import requests
import random
import datetime
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/114a.0.0.0 Safari/537.36'
    }
base_url = 'https://buff.163.com/goods/'
proxies_pool =[
    {"http":"192.168.1.45:80"},
    {'http':'123.23.191.210:80'},
    {'http':'223.107.249.1:80'},
    {'http':'43.227.139.184:80'}
]


successnum = 0
num = int(input('start: '))
startnum = num
endnum = int(input('end: '))
start_time = datetime.datetime.now()

while 1:
    url = base_url + str(num)
    proxie = random.choice(proxies_pool)
    response = requests.get(headers=headers, url=url,proxies=proxie)
    try:
        content = response.text

            # 使用正则表达式匹配并提取标题文本
        title_pattern = r"<title>(.*?)</title>"
        title_match = re.search(title_pattern, content, re.IGNORECASE)
        if title_match:
            title_text = title_match.group(1)

                # 判断是否包含目标关键词
            if "GO饰品交易" in title_text:
                    # 提取目标名称
                name_pattern = r"(.*?)_"
                name_match = re.search(name_pattern, title_text)
                if name_match:
                    name = name_match.group(1)

                        # 写入到 txt 文件
                    with open("data.txt", "a",encoding='utf-8') as output_file:
                            # 输入数字和换行符
                            output_file.write("%s,%s\n" % (str(num),name))
                print(num,": ", name)
                successnum += 1
            else:
                print(num,": unfound")
        if num == endnum:
            end_time = datetime.datetime.now()
            duration = (end_time - start_time).total_seconds()
            everage = duration/(endnum - startnum)
            print('已爬取%i条数据\n%i 至 %i\n有效数据: %s 条\n耗时: %.2fs\n平均每次访问耗时: %.2fs' % (endnum - startnum, startnum, endnum, successnum, duration,everage))
            break
        num += 1
    except urllib.error.HTTPError:
        print('太多访问了!!!\n'+'last one:',num,'\n5s 后重试!!!')
        time.sleep(5)
        num = num
        pass
