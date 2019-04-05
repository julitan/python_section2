import pytube
import os
import subprocess
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

yt = pytube.YouTube("https://www.youtube.com/watch?v=HZvD2ESqpvk") #다운받을 동영상 저장
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :
    print(i, ', ', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:\youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!")
