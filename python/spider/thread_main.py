import threading
import requests
import random
import re
import urllib.error
import time

start_index = int(input('start: '))
end_index = int(input('end: '))

url_pool = [
        f'https://buff.163.com/goods/{index}'
        for index in range(start_index,end_index+1)
]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/114a.0.0.0 Safari/537.36'
    }

proxies_pool =[
    {"http":"192.168.1.45:80"},
    {'http':'123.23.191.210:80'},
    {'http':'223.107.249.1:80'},
    {'http':'43.227.139.184:80'}
]

success_list = []
def get_page(url,writing_file):  
    content = requests.get(url= url,
                            headers= headers,
                            proxies= random.choice(proxies_pool)
                        ).text
    try:
            # 使用正则表达式匹配并提取标题文本
        title_pattern = r"<title>(.*?)</title>"
        title_match = re.search(title_pattern, content, re.IGNORECASE)
        if title_match:
            title_text = title_match.group(1)
                # 判断是否包含目标关键词
            if "CS:GO饰品交易" in title_text:
                    # 提取目标名称
                name_pattern = r"(.*?)_"
                name_match = re.search(name_pattern, title_text)
                if name_match:
                    name = name_match.group(1)    
                index = re.search(r"\d+$", url)
                success_list.append(name)
                print(name)
                writing_file.write("%s,%s\n" % (str(index),name))
        
    
    except:
         print('出现未知错误')


def muti_threads(writing_file):
    thread_pool=[]
    for url in url_pool:
        thread_pool.append(threading.Thread(target= get_page,args= (url,writing_file )))
    for thread in thread_pool:
            thread.start()


    for thread in thread_pool:
            thread.join()

if __name__ == '__main__':
    start = time.time()
    with open('data.txt','a',encoding='utf-8') as wr:
        muti_threads(writing_file= wr)
    end = time.time()
    secoends = (end-start)/len(url_pool)
    print(
         '爬取范围: %i 至 %i\n'
         '总共爬取数据: %i 条\n'
         '有效数据: %i 条\n'
         '耗时: %.3f s\n'
         '单次响应耗时: %.3f s'
         %(start_index,end_index,len(url_pool),len(success_list),end-start,secoends)
    )


