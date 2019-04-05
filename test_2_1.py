import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl1 = "https://ssl.pstatic.net/tveta/libs/1231/1231920/1004f97664cc12d1f8de_20190308113314903.jpg"
imgUrl2 = "http://cfile282.uf.daum.net/image/994AD83E5C7E67E009620C"
savePath1 = "D:/test_2_1.jpg"
savePath2 = "D:/test_2_2.jpg"

dw.urlretrieve(imgUrl1,savePath1)
dw.urlretrieve(imgUrl2,savePath2)
print("완료!")
