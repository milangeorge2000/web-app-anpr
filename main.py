import cv2
import numpy as np
import time
import imutils
from find_plate import detection
# from ocr import ocr 
from ocr import ocr
import os.path
from os import path



from flask import Flask, render_template, Response
import cv2
app=Flask(__name__)
camera = cv2.VideoCapture(0)



def gen_frames():  
    font = cv2.FONT_HERSHEY_PLAIN
    starting_time = time.time()
    frame_id = 0
    detector = detection()
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = imutils.resize(frame,width=400,height=400)
            frame_id += 1
            detector.detect(frame)
         
            


            elapsed_time = time.time() - starting_time
            fps = frame_id / elapsed_time
            cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)
            if(path.exists("ocr.txt")):
                pass 
            else:
             if(path.exists("crop4.jpg")):
                 r = ocr.image_to_text()

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
     

@app.route('/')
def index():
    return render_template('video.html')



@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__=='__main__':
    app.run(debug=True)