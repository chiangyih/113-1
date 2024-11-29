#twgo.io/pgibn
import cv2,numpy as np
#設定視窗名稱及型態
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)
target = 'pos.mp4'
cap=cv2.VideoCapture(target)

area=[
    [[1022, 79],[1174, 61],[1401, 945],[1401, 945],[1116, 979]], #區域1
    [[1449, 27],[1637, 30],[1907, 636],[1907, 636],[1904, 854],[1825, 854],[1855, 718],[1601, 267],[1606, 267]], #區域2
    ]

#繪製區域
def drawArea(f,area,color,th): # f:畫面, area:區域, color:顏色, th:線條粗細
    for a in area: #a:區域
        v =  np.array(a, np.int32) #將a轉換為numpy array,型態為int32
        cv2.polylines(f, [v], isClosed=True, color=color, thickness=th) #畫出多邊形, isClosed=True:封閉多邊形, color:顏色, thickness:線條粗細
    return f

 

while 1:
    r,frame=cap.read() #讀取一張影像
    frame = drawArea(frame,[area[0]],(0,0,255),3) # area[]是一個三維陣列，若只選其中一個區域，則會變成二維陣列，因次要加上[]
    frame = drawArea(frame,[area[1]],(0,255,255),3)
    cv2.imshow('YOLOv8',frame) #顯示影像
    key=cv2.waitKey(1) #使用者按了鍵盤
    if key==27: #27代表鍵盤的ESC
        break   #退出迴圈




