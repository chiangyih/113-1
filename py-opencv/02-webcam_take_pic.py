import cv2 # Import the OpenCV library
import time

cap=cv2.VideoCapture(0) # 開啟usb攝影機

while cap.isOpened(): # 當攝影機有開啟時
    ret, frame=cap.read() # 讀取影像, ret為讀取成功或失敗, frame為影像
    
    if ret==True: # 如果讀取成功
        cv2.imshow('Frame', frame) # 顯示影像
        if cv2.waitKey(1) & 0xFF==ord('c'): # 按下c鍵則儲存影像,oxff為16進位,ord()為取得字元的ASCII碼; waitKey(1)為延遲1毫秒
            cv2.imwrite('photo.jpg', frame) # 儲存影像
        elif cv2.waitKey(1) & 0xFF==ord('q'): # 按下q鍵則離開,oxff為16進位,ord()為取得字元的ASCII碼; waitKey(1)為延遲1毫秒
            cap.release() # 釋放攝影機
            break
    else:
        break
    
    
