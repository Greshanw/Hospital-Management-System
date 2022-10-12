import cv2, os, urllib.request
import numpy as np
from pyzbar.pyzbar import decode
from django.conf import settings

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.code = "0"

    def __del__(self):
        cv2.destroyAllWindows()
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        self.code = decoder(image)
        # ''' frame_flip = cv2.flip(image, 1) '''  flip video
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        return frame, self.code

def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qrcode = decode(gray_img)

    for obj in qrcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        codedata = obj.data.decode("utf-8")
        code = str(codedata)

        string = "Scanned"

        cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        return code