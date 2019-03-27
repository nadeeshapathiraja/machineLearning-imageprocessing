import cv2 #loading the opencv Library into your python code

img=cv2.imread('Samples/flower.jpg')##imread-image read

#print (img[100][100])#get one pixel

#img[100][100]=[255,255,255]

#img[100][100]=[0,0,0]# change its color

#cv2.rectangle(img,(100,100),(200,200),(0,255,0),2)#sourceimage #start # end #colour #line ake width for 2pixel

#cv2.circle(img,(150,150),40,(250,0,0),3)#drow sircle 
cv2.circle(img,(150,150),40,(250,0,0),-1)#drow the circle and filed the circle


cv2.imshow("WINDOW",img)#display another  window for image



