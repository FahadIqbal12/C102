import cv2
import dropbox
import time
import random

start_time = time.time() # Return time in floating point number

def take_snapshot():
    number = random.randint(0,100) #Random Integer
    videoCaptureObject = cv2.VideoCapture(0)  #Initializing the library,this will start the web cam
    result = True
    while(result):
        ret,frame = videoCaptureObject.read() #ret is a dummy variable. Read is used to read the frames. Frames will have the picture
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame) # imwrite method is used to save the image
        result = False
        return img_name
    print('Snapshot Taken')
    videoCaptureObject.release() #release method is used to close the web cam
    cv2.destroyAllWindows() # This method is used to close any window opened by camera


#take_snapshot()

def upload_file(img_name):
    access_token = 'cFJ57_TZmeIAAAAAAAAAAZv9_QKhigDh7ciLbdS19br15NNfNdH0WpOFXOmFSVBe'
    file = img_name
    file_from = file
    file_to = "/newFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        print(time.time()-start_time)
        if((time.time()-start_time)>=15):
            name = take_snapshot()
            upload_file(name)


main()


