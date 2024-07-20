import cv2

file="vika intro"
f=open(file+"/frames num.txt", "r")
frame_num= int(f.read())
f.close()

frameSize = (1280, 1280)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(file+".mp4",fourcc, 30, frameSize)

for i in range(frame_num):
    #print(file+"/"+str(i)+".jpg")
    img = cv2.imread(file+"/"+str(i//12)+".jpg")
    out.write(img)

out.release()
