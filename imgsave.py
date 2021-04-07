import urllib.request
import pandas as pd
import xlrd
import openpyxl

if __name__ == '__main__':
    reader = pd.read_excel("D:/2021 파일들/1학기 과제 파일들/캡스톤/YouTube-Playlist.xlsx")
    print("확인")
    count=1
    for video_ID in reader["Video URL"]:
        #다운받을 이미지 url
        url = "http://img.youtube.com/vi/"+video_ID[32:]+"/hqdefault.jpg"
        print(url)
        # 이미지 요청 및 다운로드
        name="img"+str(count)+".jpg"
        urllib.request.urlretrieve(url, name)
        count+=1