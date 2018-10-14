import requests
import json

class jandan_spider():
    def __init__(self):
        self.start_url = "http://i.jandan.net/pic/page-{}#comments" #煎蛋无聊图板块{}用于填写页数
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"} # 模拟安卓手机访问

    def parse_url(self, url):
        response = requests.get(url, headers = self.hearders)

        return response.content.decode("utf-8")

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)

    def save_pic(self, pic):

    def main(self): # 实现爬虫主要逻辑
        num = 220 # 从220页开始
        # 1.准备一个start_URL地址
        url = self.start_url.format(num)
        # 2.发送请求，获取响应
        json_str = self.parse_url(url)
        # 3.提取数据
        # 4.保存数据
        # 5.构造下一页的URL地址
        # 6.进入循环234


if __name__ == "__main__":
    main()