import cv2
import os
show_heigth = 30              
show_width = 80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)

vc = cv2.VideoCapture("1.flv") 

if vc.isOpened(): 
    rval , frame = vc.read()
else:
    rval = False
    
frame_count = 0
outputList = []
while rval:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(show_width,show_heigth))
    text = ""
    for pixel_line in gray:
        for pixel in pixel_line:
            text += ascii_char[int(pixel / 256 * char_len )]
        text += "\n"                                
    outputList.append(text)
    frame_count = frame_count + 1                           
    if frame_count % 100 == 0:
        print("已处理" + str(frame_count) + "帧")
    rval, frame = vc.read()  
print("处理完毕")

for frame in outputList:            
    os.system("cls")
    print(frame)
    print()
    print()
