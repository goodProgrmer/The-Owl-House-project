from PIL import Image

file= "gus"
SIZE= (1500, 700)
f=open(file+"/frames num.txt", "r")
frame_num= int(f.read())
f.close()
for i in range(frame_num):
    im= Image.open(file+"/"+str(i)+".jpg")
    ans= im.resize(SIZE)
    ans.save(file+"/"+str(i)+".jpg")

