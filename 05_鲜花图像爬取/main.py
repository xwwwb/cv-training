# 爬取百度图片搜索的结果

import json
import requests
import os


def get_image_url(keyword, page=1):
    # 爬取百度图片的页面 拿到下载链接
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = {
        'tn': 'resultjson_com',
        "ipn": "rj",
        "fp": "result",
        "word": keyword,
        "queryWord": keyword,
        "ie": "utf-8",
        "oe": "utf-8",
        "pn": page,
        "rn": "30",  # 每页30张图片 这里不变动了
    }
    res = requests.get("https://image.baidu.com/search/acjson", headers=headers, params=params)
    return json.loads(res.text)['data']


def spider(keyword, page):
    image_list = []
    for i in range(page):
        data = get_image_url(keyword, i + 1)
        for item in data:
            if item.get('thumbURL'):
                image_list.append(item.get('thumbURL'))
    print("已经拿到全部URL")
    # 没有文件夹就创建一个
    if not os.path.exists(keyword):
        os.mkdir(keyword)

    for index, url in enumerate(image_list):
        print("正在下载第{}张图片".format(index + 1))
        res = requests.get(url)
        with open("./{}/{}.jpg".format(keyword, index + 1), "wb") as f:
            f.write(res.content)


if __name__ == '__main__':
    spider("鲜花", 5)
