import urllib.request
import cv2 as cv
import numpy as np
import cvlib
import time

frame = None
key = None
print('start')

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydb']

collection = db['OPENLAB__Data']


def timer_calc(n):
    a = min(n * 3 + 3, 30)
    return max(5, a)


while True:

    imgResp = urllib.request.urlopen('http://192.168.43.215/capture?')
    imgnp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv.imdecode(imgnp, -1)
    box, label, count = cvlib.detect_common_objects(frame)
    cnt = len(label)
    time.sleep(5)
    if cnt == 0:
        collection.update_one({"_id": 1}, {"$set": {"Green": 5}})
    else:
        collection.update_one({"_id": 1}, {"$set": {"count": cnt}})
        collection.update_one({"_id": 1}, {"$set": {"Green": timer_calc(cnt)}})
    imgResp = urllib.request.urlopen('http://192.168.43.215/capture?')
    imgnp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv.imdecode(imgnp, -1)
    box, label, count = cvlib.detect_common_objects(frame)

    cnt = len(label)
    time.sleep(5)
    if cnt == 0:
        collection.update_one({"_id": 2}, {"$set": {"Green": 5}})
    else:
        collection.update_one({"_id": 2}, {"$set": {"count": cnt}})
        collection.update_one({"_id": 2}, {"$set": {"Green": timer_calc(cnt)}})


    imgResp = urllib.request.urlopen('http://192.168.43.215/capture?')
    imgnp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv.imdecode(imgnp, -1)
    box, label, count = cvlib.detect_common_objects(frame)

    cnt = len(label)
    time.sleep(5)
    if cnt == 0:
        collection.update_one({"_id": 3}, {"$set": {"Green": 5}})
    else:
        collection.update_one({"_id": 3}, {"$set": {"count": cnt}})
        collection.update_one({"_id": 3}, {"$set": {"Green": timer_calc(cnt)}})

    imgResp = urllib.request.urlopen('http://192.168.43.215/capture?')
    imgnp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv.imdecode(imgnp, -1)
    box, label, count = cvlib.detect_common_objects(frame)

    cnt = len(label)
    time.sleep(5)
    if cnt == 0:
        collection.update_one({"_id": 3}, {"$set": {"Green": 5}})
    else:
        collection.update_one({"_id": 3}, {"$set": {"count": cnt}})
        collection.update_one({"_id": 3}, {"$set": {"Green": timer_calc(cnt)}})

    collection.update_one({"_id": 4}, {"$set": {"count": cnt}})
    collection.update_one({"_id": 4}, {"$set": {"Green": timer_calc(cnt)}})

    '''
    
    cv.imshow('window',frame)
    if cv.waitKey(500) == ord('q'):
        break
    
    '''
cv.destroyAllWindows()
print('end')
