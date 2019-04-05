from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/high-rating/"

res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")

recommand = soup.select("ul.slides")[0]
for e in recommand:
    print(e.select_one("h4.block_title > a"))
print(recommand)

print(soup)
