import threading
import requests
import time

url_pool = [
    f'https://buff.163.com/s/goods.html?game=csgo&goods_id={index}'
    for index in range(36000,36011)
]


def get_page(url):
    response = requests.get(url= url)
    print(url)


def mult_thread():
    thread_list = []
    for url in url_pool:
        thread_list.append(
            threading.Thread(target= get_page,args= (url,))
        )

    for thread in thread_list:
        thread.start()


    for thread in thread_list:
        thread.join()

if __name__ == '__main__':
    start = time.time()
    mult_thread()
    end = time.time()
    print(end-start)




