import cv2

filename = "./img/PlayerMove.jpg"

cam = cv2.VideoCapture(0)   

def TakePicture():
    s, img = cam.read()
    cv2.imwrite(filename, img)

def GetFileName():
    return filename