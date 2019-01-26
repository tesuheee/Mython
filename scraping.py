import time
import sys #システムのライブラリをインポート
import requests #HTMLを取得する
from bs4 import BeautifulSoup #モジュール名bs4 よりbeautifulsoupをインポート

url = 'http://yylab.ce.cst.nihon-u.ac.jp/~inatok/today.php'

res = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')
    
records = soup.select('h3')
for record in records:
    print(record.get_text())