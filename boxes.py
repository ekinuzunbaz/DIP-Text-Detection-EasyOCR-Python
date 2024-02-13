import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# read image
def textDetection(img,lang_code):
        
    # instance text detector
    reader = easyocr.Reader([lang_code], gpu=True)
    
    # detect text on image
    text_ = reader.readtext(img)
    
    threshold = 0.40
    # draw bbox and text
    fullText = ''
    for t_, t in enumerate(text_):
        print(t)    
        bbox, text, score = t 
        bbox = [[int(j) for j in i] for i in bbox]
        top_left = tuple(bbox[0])
        bottom_right = tuple(bbox[2])
        if score > threshold:
            fullText += text + '\n'
            cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
    
    print(fullText)
    plt.imshow(img)
    plt.show()
    cv2.imwrite('output.png', img)
    return fullText