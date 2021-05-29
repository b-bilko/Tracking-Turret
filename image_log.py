import cv2
import threading
from datetime import datetime, timedelta
import os
import motion_sensor

class ImageLogger(object):
    def __init__(self, folder, limit, min_time = timedelta(seconds=3)):
        self.folder = folder
        self.limit = limit
        self.min_time = min_time
        self.prev = datetime.min
        self.first = True
        self.busy = False

    def consider_img(self, img, motion, motion_sensor_state, firing):
        if motion_sensor_state == motion_sensor.MotionSensor.TRACKING:
            log = True
            if self.first:
                self.last = "FIRST"
                self.first = False
            elif firing:
                self.last = "FIRING"
            elif self.last != "MOTION" and motion:
                self.last = "MOTION"
            else:
                log = False

            if log and not self.busy:
                self.busy = True
                thread = threading.Thread(target = self.save_img, args=(img, self.last))
                thread.run()

    def save_img(self, img, reason):
        now = datetime.now()
        if now - self.prev > self.min_time:
            self.prev = now
            cv2.imwrite(os.path.join(self.folder, now.strftime("%Y%m%d%H%M%S.REASON.png").replace("REASON", reason)), img)
        self.busy = False
