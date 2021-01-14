# 翻页的处理
import requests
from lxml import etree
# pip install lxml
from time import sleep
# 控制请求的频率，引入了time模块

# 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

    header = {'user-agent':ua}
    response = requests.get(myurl,headers=header)

    selector = etree.HTML(response.text)
    # 评论名
    answers = selector.xpath('//div[@class="List-item"]//a[@class="UserLink-link"]/text()')

    # 评论内容
    answers_link = selector.xpath('//div[@class="List-item"]//div[@class="RichContent-inner"]/span[1]/p/text()')

    # 遍历对应关系字典, zip两个列表进行链接，转为film_info字典
    answer_info = dict(zip(answers, answers_link))

    for i in answer_info:
        # 写入并追加写入
        with open('zhihu.html','a', encoding='utf-8') as f:
            f.write(f'评论人： {i} \t\t 评论： {answer_info[i]}')

if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = 'https://www.zhihu.com/question/309630223'

    get_url_name(urls)
    