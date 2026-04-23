import cv2
import os, sys, inspect #For dynamic filepaths

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 30)

# Pretrained classes in the model - Dictionary
classNames = {0: 'background',
              1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

#Function to return name from the dictionary
def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)			

  # Loading model
model = cv2.dnn.readNetFromTensorflow(execution_path('ExploreOpencvDnn/models/frozen_inference_graph.pb'),
                                      execution_path('ExploreOpencvDnn/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt'))
#image = cv2.imread(execution_path("image.jpeg"))

while True:
    check, frame = cam.read()
    if check == False:
        break

    image = cv2.flip(frame,0)#cv2.resize(frame, (1920,1080))#cv2.resize(frame, (0,0), fx = 0.8, fy = 0.8)    
    image_height, image_width, _ = image.shape

    

    #Sets our input as the image, turns it into a blob
    #Resizes and sets the colour mode to BGR
    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))

    # Returns a blob array
    output = model.forward()



    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .5: #This is our confidence threshold
            class_id = detection[1] #This is the ID of what it thinks it is
            class_name=id_class_name(class_id,classNames) #Returning the name from Dictionary
            print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
            
            #Draw the bounding box, scaled to size of the image
            box_x = detection[3] * image_width
            box_y = detection[4] * image_height
            box_width = detection[5] * image_width
            box_height = detection[6] * image_height
            cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
            
            #Put some text on the bounding box
            cv2.putText(image,class_name ,(int(box_x), int(box_y-.005*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.0015*image_height),(0, 0, 255))



    cv2.imshow('image', image)
    # cv2.imwrite("image_box_text.jpg",image)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
