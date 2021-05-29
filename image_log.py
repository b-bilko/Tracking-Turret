import cv2
import threading
from datetime import datetime, timedelta
import os

class ImageLogger(object):
    def __init__(self, folder, limit, min_time = timedelta(seconds=3)):
        self.folder = folder
        self.limit = limit
        self.min_time = min_time
        self.prev = datetime.min
        

    def consider_img(self, img, motion):
        thread = threading.Thread(target = self.save_img, args=(img, "ALL"))
        thread.run()

    def save_img(self, img, reason):
        now = datetime.now()
        if now - self.prev > self.min_time:
            self.prev = now
            cv2.imwrite(os.path.join(self.folder, now.strftime("%Y%m%d%H%M%S.png")), img)
