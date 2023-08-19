
import threading
import requests

async def gospider(urls):
    '''这是普通爬虫，传入urls，单个或多个都可以——Sydrro'''
    if len(urls) == 1:
        content = requests.get(urls).text
        return content

    if len(urls) >= 2:
        content_list = []
        for url in urls:
            content_list.append(requests.get(url).text)
        return content_list
    else:
        return None
    
         
def gomultspider(urls:list):
    content_list = []
    def get_page(url):
        content = requests.get(url).text
        content_list.append(content)

        return content
    '''这是并发爬虫，传入urls，只能传入多个url——Sydrro'''
    if len(urls) >= 2:
        thread_list = []
        
        for url in urls:
            thread_list.append(
                threading.Thread(target= get_page,args= (url,))
            )

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()    

if __name__ == '__main__':
    urls = [
        f'https://buff.163.com/goods/{index}'
        for index in (0,10)
    ]
    a = gospider(urls=urls)
    print(a)