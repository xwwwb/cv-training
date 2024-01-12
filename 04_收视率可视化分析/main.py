# 隐秘而伟大数据爬取与分析
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt, font_manager

URL = "https://baike.baidu.com/item/%E9%9A%90%E7%A7%98%E8%80%8C%E4%BC%9F%E5%A4%A7/22454129"


# 爬取收视情况并保存
def crawl_viewing_data():
    # 构造虚假的UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    try:
        # 发送请求
        res = requests.get(URL, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        # 找到所有表格
        tables = soup.find_all('table')

        for table in tables:
            # 在表格中找到含有 播出日期 以及 收视率的字符串
            if "播出日期" in table.text and "收视率" in table.text:
                return table
    except Exception as e:
        print(e)


def parse_viewing_data(viewing_table):
    # 解析表格 拿到所有的行
    viewing_datas = []
    trs = viewing_table.find_all('tr')
    # 去除前两行
    trs = trs[2:]
    for i in range(len(trs)):
        tds = trs[i].find_all('td')
        data = {
            'date': tds[0].text,
            'csm59_rating': tds[1].text,
            'csm59_rating_share': tds[2].text,
            'csm59_ranking': tds[3].text,
            'csm_rating': tds[4].text,
            'csm_rating_share': tds[5].text,
            'csm_ranking': tds[6].text,
        }
        viewing_datas.append(data)

    return viewing_datas


if __name__ == '__main__':
    data = parse_viewing_data(crawl_viewing_data())
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.figure(figsize=(20, 15), dpi=200)
    # 绘制收视率线
    dates = [d['date'] for d in data]
    csm59_ratings = [float(d['csm59_rating']) for d in data]
    csm_rating = [float(d['csm_rating']) for d in data]
    plt.title("隐秘而伟大收视率", fontsize=50)
    plt.xticks([])
    plt.yticks(fontsize=50)
    plt.xlabel("日期", fontsize=50)
    plt.ylabel("收视率", fontsize=50)
    plt.plot(dates, csm59_ratings, label="CSM59城市网收视率")
    plt.plot(dates, csm_rating, label="CSM全国网收视率")
    # legend大小
    plt.legend(prop=font_manager.FontProperties(size=30))
    plt.show()
