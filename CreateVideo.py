import cv2
import os
path = "Images/"

Images = []
 
for i in os.listdir(path):
    
    name, extension = os.path.splitext(i)
    print(extension)
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+i

        print(file_name)
        Images.append(file_name)
count = len(Images)

frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frames = cv2.imread(Images[i])
    out.write(frames)

out.release()    
    