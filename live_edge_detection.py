import cv2
def sketch(img):
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur=cv2.bilateralFilter(img,9,75,75)
    canny_edge=cv2.Canny(img_blur,10,70)
    ret,mask=cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY_INV)
    return mask

cap=cv2.VideoCapture(0)
while(True) :
    ret,frame=cap.read()
    cv2.imshow('live sketch', sketch(frame))
    if cv2.waitKey(1)==13 :
        break

cap.release()
cv2.destroyAllWindows()
