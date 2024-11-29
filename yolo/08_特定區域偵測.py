from shapely.geometry import Polygon #引入多邊形物件,用來判斷是否有重疊,並取得重疊比例 #利用重疊偵測套件 shapely來判斷是否有特定物件位於欲偵測區域
import cv2,numpy as np, time
from ultralytics import YOLO
#設定視窗名稱及型態
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)
#取得重疊比例
def inarea(object,area): #object:物件, area:區域
    inAreaPercent=[] #重疊比例
    b=[[object[0],object[1]],[object[2],object[1]],[object[2],object[3]],[object[0],object[3]]] # 物件座標轉多邊形
    for i in range(len(area)):        
        poly1 = Polygon(b) #物件多邊形,用來判斷是否有重疊
        poly2 = Polygon(area[i]) #區域多邊形,用來判斷是否有重疊
        intersection_area = poly1.intersection(poly2).area #取得重疊面積,用來計算重疊比例,poly1與poly2的交集(重疊)面積
        poly1Area = poly1.area  #取得poly1的面積     
        #union_area = poly1.union(poly2).area
        overlap_percent = (intersection_area / poly1Area) * 100 #計算poly1進入poly2的重疊比例,交集面積/物件面積
        inAreaPercent.append(overlap_percent)
    return inAreaPercent

area=[
    [[390,5],[590,5] ,[590,307],[590,460],[320,280]], #區域2
    ]

#繪製區域
def drawArea(f,area,color,th):
    for a in area:
        v =  np.array(a, np.int32)
        cv2.polylines(f, [v], isClosed=True, color=color, thickness=th)
    return f


cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)

target=0 #'city.mp4'
model = YOLO('yolov8m.pt')  # pretrained YOLOv8m model

names=model.names

cap=cv2.VideoCapture(target)

while 1:
    try:
        st=time.time()  
        r,frame = cap.read()
        results = model(frame)
        #frame= results[0].plot()
        frame = drawArea(frame,area,(0,0,255),3)

        for obj in results[0].boxes.data:
            x1,y1,x2,y2=int(obj[0]),int(obj[1]),int(obj[2]),int(obj[3])
            r=round(float(obj[4]),2)
            n=names[int(obj[5])]
            personList=[x1,y1,x2,y2,r,n]
            if n=='person':
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,255),3)
                p=inarea(personList,area)                
                print('比例=',p)
                cv2.putText(frame, str(round(p[0],2)), (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)



        et=time.time()
       
        FPS=round((1/(et-st)),1)
        cv2.putText(frame, 'FPS=' + str(FPS), (20, 150), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('YOLOv8', frame)
        key=cv2.waitKey(1)
        if key==27:
            break
    except Exception as e :
        print(e)
        break



