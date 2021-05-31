import os
import cv2
import numpy as np
import tensorflow as tf
import time
from utils.PlaySound import Play_temperature, Play_Nomask, Play_thank_you
from utils.Arduino_serialCom import Temperature
import time

#--------------- FLAGS --------------------------
F_DISPLAY_DETECTION = True # To display the detections onoutput img when runnuing
F_DISPLAY_OUTPUT = True # This will give the output window
F_MASK_DETECTED = False # will be set to True when mask detected
F_PLAYED_SOUND_NOMASK_DETECTED = False # indicateing that no-mask detected mp3 is played
F_PLAY_AUDIO_FEEDBACK = True # do you want the audio to be played?
#------------------------------------------------

#--------------- Counters ------------------------
CNT_REPLAY_NOMASK_DETECTED = 0
#-------------------------------------------------
#--------------- Functions -----------------------------
def DISPLAY_DETECTION(object_name,image,xmin,ymin,xmax,ymax):
    colour = (10,255,0) if object_name=="Mask" else (0,10,255)
    cv2.rectangle(image, (xmin,ymin), (xmax,ymax), colour, 2)
    labelSize, baseLine = cv2.getTextSize(object_name, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
    label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
    cv2.rectangle(image, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
    cv2.putText(image, object_name, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text


def DISPLAY_OUTPUT(image):
    # returns True if user wants to quit
    cv2.imshow('Object detector', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        return True
#-------------------------------------------------------

print('[INFO] Loading labels..')
with open('utils/model/lbl.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

print('[INFO] Loading model..')
interpreter = tf.lite.Interpreter(model_path='utils/model/KAYA_detectMask.tflite',num_threads=4)  #experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
interpreter.allocate_tensors()
    
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]
chk = None
video = cv2.VideoCapture(0)
while True:
    if chk == False:
        break
    while not F_MASK_DETECTED:
        start_time = time.time()
        chk, image = video.read()
        if chk == False:
            break
        #image = cv2.resize(image,(int(image.shape[1]),int(image.shape[0])))
        if image.shape[0] > image.shape[1]:
            re_width = 720
            re_hight = 480
        else:
            re_width = 480
            re_hight = 720
        image = cv2.resize(image,(re_hight,re_width))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imH, imW = image.shape[:2]
        image_resized = cv2.resize(image_rgb, (width, height))
        input_data = np.expand_dims(image_resized, axis=0)
        #input_data = input_data.astype(np.float32)

        interpreter.set_tensor(input_details[0]['index'],input_data)
        interpreter.invoke()
        
        boxes = interpreter.get_tensor(output_details[0]['index'])[0][0] # Bounding box coordinates of detected objects
        classes = interpreter.get_tensor(output_details[1]['index'])[0][0] # Class index of detected objects
        scores = interpreter.get_tensor(output_details[2]['index'])[0][0] # Confidence of detected objects
        
        end_time = time.time()
        FPS = end_time-start_time

        ymin = int(max(1,(boxes[0] * imH)))
        xmin = int(max(1,(boxes[1] * imW)))
        ymax = int(min(imH,(boxes[2] * imH)))
        xmax = int(min(imW,(boxes[3] * imW)))
        area = (xmax-xmin)*(ymax-ymin)
        
        # this section will re-set the flag F_PLAYED_SOUND_NOMASK_DETECTED------
        if (scores < 0.5) or (area < 32000) :
            CNT_REPLAY_NOMASK_DETECTED += 1

        if CNT_REPLAY_NOMASK_DETECTED > 15: # number 15 should be changed for PI
            F_PLAYED_SOUND_NOMASK_DETECTED = False
        #-----------------------------------------------------------------------

        if ((scores > 0.5) and (scores < 1.0)):
            # area >= 9700 should be selected for distance = 50 inch
            # area >= 21000 should be selected for distance = 37 inch
            # area >= 34000 should be selected for distance = 30 inch
            # area <= 80000 is selected as the min distance between the camera and person
            # and the distance is 17 inch
            if area >=32000 and area<=80000:
                # Draw label
                object_name = labels[int(classes)] # Look up object name from "labels" array using class index

                # Setting the flag for Mask detected
                if object_name == "Mask":
                    F_MASK_DETECTED = True

                if F_DISPLAY_DETECTION:
                    DISPLAY_DETECTION(object_name,image,xmin,ymin,xmax,ymax)

                if object_name == "Nomask":
                    if not F_PLAYED_SOUND_NOMASK_DETECTED:
                        if F_PLAY_AUDIO_FEEDBACK:
                            Play_Nomask()
                            CNT_REPLAY_NOMASK_DETECTED = 0
                    F_PLAYED_SOUND_NOMASK_DETECTED = True
                    
                
        frame_time = str('{:.2}'.format(FPS))+' Sec for 1 Frame'
        cv2.rectangle(image,(13,1),(310,25),(0,0,0),cv2.FILLED)
        cv2.putText(image, (frame_time), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
        if F_DISPLAY_OUTPUT:
            chk_break = DISPLAY_OUTPUT(image)
            if chk_break:
                video.release()
                cv2.destroyAllWindows()
                break

    else:
        cv2.destroyAllWindows()
        F_PLAYED_SOUND_NOMASK_DETECTED = False
        CNT_REPLAY_NOMASK_DETECTED = 0
        if F_PLAY_AUDIO_FEEDBACK:
            Play_temperature()
        # from here on it will be as good as saying that mask was detected so....
        # what are your next steps....
        # you will scan temperature....
        # other loop can be weitten

        # here we have used a simple input to trigger the ouyput

        #-------------------- To Do -----------------------
        # Get the sensor data from the arduino via serial communication
        #--------------------------------------------------

        temp = Temperature()
        print("Your body temperature is ",temp)
        if F_PLAY_AUDIO_FEEDBACK:
            Play_thank_you()
        F_MASK_DETECTED = False
        time.sleep(1)

cv2.destroyAllWindows()


