## 爬取网络数据的一般步骤

1. 引入文件
```python
import requests
from bs4 import BeautifulSoup
```
2. 几种方法
+ `pandas.read_html()`,之中放入网站
+ 使用`requests`和`BeautifulSoup
```python
import requests

head  = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
param=  {'wd':'python'}
res = requests.get('http://www.baidu.com/s',params=param,headers=head)
```
or
```python
import requests

URLTop250Moi = 'https://movie.douban.com/top250'
headers = {
	'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
	'Cookie': 'bid=03QzRATVvZI; douban-fav-remind=1; __gads=ID=235109b723938ba4-2224407c19d8000c:T=1668039578:RT=1668039578:S=ALNI_MYFFJ5HU2_bVR7eqoxZtDCAQBeaiA; __gpi=UID=00000b78f6a2bf6c:T=1668039578:RT=1668325134:S=ALNI_MZJXHay5I4KEyvwl_-VLHskRpbIyA; __utma=30149280.1863681919.1668039577.1668325999.1668341717.4; __utmz=30149280.1668325999.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17848; gr_user_id=dccf8534-bc90-42d8-b1be-c133a8b1daf7; ap_v=0,6.0; __utmb=30149280.9.8.1668341833502; __utmc=30149280; __utmt_douban=1; __utmt_t1=1; RT=s=1668341920729&r=https%3A%2F%2Fbook.douban.com%2Fsubject%2F6025373%2Fcomments%2F%3Fstart%3D220%26amp%3Blimit%3D20%26amp%3Bstatus%3DP%26amp%3Bsort%3Dnew_score; dbcl2="178484147:wK+jx5QTARI"; ck=PDDZ'
}
res = requests.get(URLTop250Moi, headers=headers)
```

3. session()的使用
> The Session object allows you to persist certain
> parameters across requests. It also persists cookies 
> across all requests made from the Session instance, 
> and will use urllib3’s connection pooling.
> So if you’re making several requests to 
> the same host, the underlying TCP connection will be reused, which can result in a significant performance increase (see HTTP persistent connection).
```python
# 感觉主要是使用post()方法报送数据
import requests
import requests

head = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
}
postURL = 'https://login2.scrape.center/login'
url = 'https://login2.scrape.center'
postData = {
	'username' : 'admin',
	'password':'admin'
}
session = requests.session()
session.post(postURL,headers = head,data = postData)
res = session.get(url)
res.text
```
