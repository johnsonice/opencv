#import numpy as np
import cv2

cap = cv2.VideoCapture('data/video.avi')
#print(len(cap))
print(cap.grab())


#%%
counter = 0
while(cap.isOpened()):
    frame = cap.grab()
    
    counter+=1
    print(counter)

print('finished')
cap.release()




#%%
#while(cap.isOpened()):
#    ret, frame = cap.read()
#    #print('works')
#
#    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    try:
#        cv2.imshow('frame',frame)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break
#    except:
#        cap.release()
#        cv2.destroyAllWindows()
#
#
#cap.release()
#cv2.destroyAllWindows()
