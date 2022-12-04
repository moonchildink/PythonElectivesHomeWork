import requests
from bs4 import BeautifulSoup
import re

urls = ['http://xc.hfut.edu.cn/1954/list.htm']
for i in range(2, 6):
    s = 'http://xc.hfut.edu.cn/1954/list{0}.htm'.format(i)
    urls.append(s)

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Cookie': 'bid=03QzRATVvZI; douban-fav-remind=1; __gads=ID=235109b723938ba4-2224407c19d8000c:T=1668039578:RT'
              '=1668039578:S=ALNI_MYFFJ5HU2_bVR7eqoxZtDCAQBeaiA; '
              '__gpi=UID=00000b78f6a2bf6c:T=1668039578:RT=1668325134:S=ALNI_MZJXHay5I4KEyvwl_-VLHskRpbIyA; '
              '__utma=30149280.1863681919.1668039577.1668325999.1668341717.4; '
              '__utmz=30149280.1668325999.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; '
              'push_doumail_num=0; __utmv=30149280.17848; gr_user_id=dccf8534-bc90-42d8-b1be-c133a8b1daf7; ap_v=0,'
              '6.0; __utmb=30149280.9.8.1668341833502; __utmc=30149280; __utmt_douban=1; __utmt_t1=1; '
              'RT=s=1668341920729&r=https%3A%2F%2Fbook.douban.com%2Fsubject%2F6025373%2Fcomments%2F%3Fstart%3D220'
              '%26amp%3Blimit%3D20%26amp%3Bstatus%3DP%26amp%3Bsort%3Dnew_score; dbcl2="178484147:wK+jx5QTARI"; '
              'ck=PDDZ '
}

docs = []
contents = []
titles = []

for url in urls:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    docs.append(soup)

for doc in docs:
    contents.append(str(doc.find_all('span', class_='news_title')))  # 标题包裹在span之中
for content in contents:
    li = re.findall(r'(?<=title=")[\u4e00-\u9fa5\d（）”—“：、《》， ]*(?=">)',content)   # 正则表达式要匹配数字.逗号.引号.括号.
    for i in li:
        titles.append(i)
print(titles)