import urllib.request
import cv2
import numpy as np

def getWidth(link):
    cap = cv2.VideoCapture(link)
    return cap.get(cv2.CAP_PROP_FRAME_WIDTH )

def getHeight(link):
    cap = cv2.VideoCapture(link)
    return cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

