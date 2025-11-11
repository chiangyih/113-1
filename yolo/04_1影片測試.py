#https://twgo.io/xpuka
#測試影片：https://twgo.io/vlpwc
#tw live可搜尋台灣即時影像：https://trafficvideo2.tainan.gov.tw/b596d902

from ultralytics import YOLO
import cv2,time
#設定視窗名稱及型態
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL) #cv2.WINDOW_NORMAL可以讓視窗放大縮小

# target=1
#target='city.mp4'
target='https://trafficvideo.tainan.gov.tw/e2e14cfa'

model = YOLO('yolov8m.pt')  # n,s,m,l,x 五種大小

names=model.names #辨識類別, 80種 
print(names) #顯示辨識類別

cap=cv2.VideoCapture(target) #0:代表第一隻攝影機，這裡用target變數讀取

while 1:
    st=time.time() #計算時間,開始時間
    r,frame = cap.read() #讀取攝影機畫面, r:讀取成功True/失敗False, frame:攝影機畫面
    if r==False:
        break
    results = model(frame) # YOLOv8模型辨識,回傳結果,results[0]:辨識結果,results[1]:辨識時間,results[2]:辨識框,results[3]:辨識類別,model():辨識,frame:畫面
    frame= results[0].plot() #畫出辨識結果,results[0]:辨識結果
    et=time.time() #計算時間,結束時間
   
    FPS=round((1/(et-st)),1) #FPS:每秒幾張畫面,1/(結束時間-開始時間)

    cv2.putText(frame, 'FPS=' + str(FPS), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('YOLOv8', frame)
    key=cv2.waitKey(1)
    if key==27:
        break



