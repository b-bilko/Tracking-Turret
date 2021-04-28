from turret import MotionSensor
from datetime import datetime

def on_motion(contour, frame):
    print(datetime.now(), "MOTION")
    
def on_no_motion(frame):
    print(datetime.now(), "NO MOTION")
    
motion_sensor = MotionSensor(diag=True)

motion_sensor.get_empty_frame()
#motion_sensor.find_motion(on_motion, on_no_motion, show_video=True)