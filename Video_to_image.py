import cv2

#capturing video
vidcap = cv2.VideoCapture('D:\\ashish\\Get Ready To Fight.mp4')

#reading image
ret, image = vidcap.read()
count = 0 

while True:
    if ret == True:
        
        #saving frames which were capture
        cv2.imwrite('D:\\ashish\\imgN%d.jpg' %count, image) 

        #to set how many frames should be captured in one second
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*200))
        
        ret,image = vidcap.read()

        cv2.imshow("Video to image", image)
        count += 1

        if cv2.waitKey(1) == ord('q'):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()
