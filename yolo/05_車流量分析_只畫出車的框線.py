

from ultralytics import YOLO
import cv2,time
#設定視窗名稱及型態
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL) #cv2.WINDOW_NORMAL可以讓視窗放大縮小

target='city.mp4'


model = YOLO('yolov8s.pt')  # n,s,m,l,x 五種大小

names=model.names #辨識類別, 80種 
# print(names) #印出辨識物件的編號與名稱;型態為dictionary

cap=cv2.VideoCapture(target) #0:代表第一隻攝影機，這裡用target變數讀取

while 1:
    st=time.time() #計算時間,開始時間
    r,frame = cap.read() #讀取攝影機畫面, r:讀取成功True/失敗False, frame:攝影機畫面
    if r==False:
        break
    results = model(frame,verbose=False) # 用YOLOv8模型辨識,回傳辨識結果存於results；verbose=False:在終端機不顯示辨識結果
    # frame= results[0].plot() #使用plot()畫出辨識結果(boxes),results[0]:第一張frame
    #分析每張圖片中的boxes(共6個欄位)
    for box in results[0].boxes.data: #results[0].boxes.data:辨識結果的boxes
        x1=int(box[0]) #x1:box的左邊線位置
        y1=int(box[1]) #y1:box的上邊線位置
        x2=int(box[2]) #x2:box的右邊線位置
        y2=int(box[3]) #y2:box的下邊線位置
        r=round(float(box[4]),2) #r:box的信心度；原始值為科學記號，因此先取福點數後，再round():取小數點後兩位
        n=names[int(box[5])] #n:box辨識出來的物件編號，再藉由names字典找出物件名稱
        #只畫出車輛的框(檢查是否為car, truck, bus)
        if n in ['car', 'truck', 'bus']: #如果辨識出來的物件名稱為car, truck, bus
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) #畫出box, (0, 255, 0):box的顏色, 2:box的粗細
            cv2.putText(frame, n , (x1, y1+18), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv2.LINE_AA) #在box左上方寫上物件名稱
            cv2.putText(frame, str(r) , (x1, y1+38), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2, cv2.LINE_AA) #在box左上方，物件名稱下方寫上信心度
        
        
    
    et=time.time() #計算時間,結束時間
   
    FPS=round((1/(et-st)),1) #FPS:每秒幾張畫面,1/(結束時間-開始時間)

    cv2.putText(frame, 'FPS=' + str(FPS), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('YOLOv8', frame)
    key=cv2.waitKey(1)
    if key==27:
        break



