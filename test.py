
import requests
import json
from requests.exceptions import RequestException

headers = {
    'Host': 'manhua1017-61-174-50-99.cdndm5.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'http://www.dm5.com/m60100-p10/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
}

def download_image(url):
    print('正在下载',url)
    try:
        response = requests.get(url,headers=headers)
        print(response)
        if response.status_code == 200:
            # 返回二进制内容
            pass
        return response.status_code
    except RequestException:
        print("请求失败~")
        return None

url = 'http://manhua1016-61-174-50-98.cdndm5.com/j/绝代双骄/绝代双骄2_ch566/jdsj566-12.jpg?cid=60100&key=51095cd792c39023a9f6902e342b2c2a'

download_image(url)






