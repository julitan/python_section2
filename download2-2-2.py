import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://cafefiles.naver.net/20150404_41/onehodang2_1428121325007MWF8c_JPEG/10.jpg"
htmlURL ="http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"

f = dw.urlopen(imgUrl).read()
saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()


print("다운로드 완료!")
