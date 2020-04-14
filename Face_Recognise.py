import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import os

class Face_Recognize():
    def __init__(self):
        self.face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_extractor(self,img):
        #Finding face in image
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
        
        if faces is():
            return None

        for(x,y,w,h) in faces:
            cropped_face=img[y:y+h,x:x+w]

        return cropped_face

    def face_detection(self,img,size=0.5):
        #Face detection
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.face_cascade.detectMultiScale(gray,1.3,5)

        if faces is():
            return img,[]

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi=img[y:y+h,x:x+w]
            roi=cv2.resize(roi,(200,200))

        return img,roi

    #For sign_up
    def Signup(self,user_name):
        cap=cv2.VideoCapture(0)

        #Counting number of images stored
        count=0
        while True:
            ret,frame=cap.read()
            if self.face_extractor(frame) is not None:
                count+=1
                face=cv2.resize(self.face_extractor(frame),(200,200))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                file_name_path='./user_photo/'+user_name+'/user'+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)

                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,250,0),2)
                cv2.imshow('Face Cropper',face)
            else:
                pass
            if cv2.waitKey(1)==13 or count==100:
                break
        cap.release()
        cv2.destroyAllWindows()
        return 1

    #For log in
    def login(self,user_name):
        data_path='./user_photo/'+user_name+"/"
        #Fetching all files from folder of user
        onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]

        #Trainig the data
        Training_Data,Labels=[],[]

        for i, files in enumerate(onlyfiles):
            image_path=data_path+onlyfiles[i]
            images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images,dtype=np.uint8))
            Labels.append(i)


        Labels=np.asarray(Labels,dtype=np.int32)

        model=cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data),np.asarray(Labels))


        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        cap=cv2.VideoCapture(0)

        #Flag is for, if the face is matched
        flag=0

        #To match the face for particular time i.e. upto k=200
        k=0
        while k!=200 and flag==0:
            ret,frame=cap.read()

            image,face=self.face_detection(frame)

            try:
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                result=model.predict(face)

                if result[1]<500:
                    confidence= int(100*(1-(result[1])/300))
                    display_string=str(confidence)+"% confidence it is user"
                cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)

                #if >=75% match found then unlocked
                if confidence>=75:
                    flag=-1
                    cv2.putText(image,"Unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    break
                    cv2.imshow("Face Cropper",image)
                else:
                    cv2.putText(image,"Locked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.imshow("Face Cropper",image)
                    
            except:
                cv2.putText(image,"Face Not Found",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
                cv2.imshow("Face Cropper",image)
                pass
            
            #Press enter to stop
            if cv2.waitKey(1)==13:
                break
            k+=1
        if flag==-1:
            cap.release()
            cv2.destroyAllWindows()
            return ""
        else:
            cap.release()
            cv2.destroyAllWindows()
            return "Face not matched"
        

