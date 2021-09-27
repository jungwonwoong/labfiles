import cv2
import socketio
import numpy as py
import pybase64

sv = True
sio = socketio.Client()
sio.connect('http://localhost:3000', namespaces=['/video'])
@sio.event(namespace='/video')
def stopvideo(data):
    global sv
    sv = data

cap = cv2.VideoCapture(1)
cap.set(3, 960)
cap.set(4, 540)
posxcheck = []
posycheck = []
mog = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
while True:
    if sv:
        posx = []
        posy = []
        i=0
        j=0
        sum = 0
        v = 0
        ret, frame = cap.read()
        mogframe = mog.apply(frame)
        contours, _ = cv2.findContours(mogframe, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            mmt = cv2.moments(c)
            if mmt['m00'] > 70:
                i=i+1
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                cx = int(mmt['m10']/mmt['m00'])
                cy = int(mmt['m01']/mmt['m00'])
                posx.insert(i, cx)
                posy.insert(i, cy)
                #pos = str(mmt['m00'])
                #cv2.putText(frame, pos, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (157, 255, 0), 1, cv2.LINE_AA)
        if len(posx) == len(posxcheck) and len(posx) != 0:
            for a in posx:
                sum = sum + ((posx[j] - posxcheck[j])**2 + (posy[j] - posycheck[j])**2)**0.5
                j += 1
            v = sum/len(posx)
        else:
            v = -1
                
        sio.emit('posdata', {'x': posx, 'y': posy, 'v': v }, namespace='/video')
        #cv2.imshow('video view', mogframe)
        res, sframe = cv2.imencode('.jpg', frame)
        data = pybase64.b64encode(sframe)
        sio.emit('videocamera', data, namespace='/video')
        cv2.imshow('recttangle view', frame)
        posxcheck = posx
        posycheck = posy
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()
