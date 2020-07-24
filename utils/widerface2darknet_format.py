import os,cv2
import numpy as np
from os import listdir, getcwd


rootdir="/usr/src/persondata/face/WIDERFace" #widerface数据集所在目录
convet2yoloformat=True
minsize2select=20#widerface中有大量小人脸，只取20以上的来训练

datasetprefix="/usr/src/persondata/face/WIDER_Face"



def convertimgset(img_set="train"):
    imgdir=rootdir+"/WIDER_"+img_set+"/images"
    gtfilepath=rootdir+"/wider_face_split/wider_face_"+img_set+"_bbx_gt.txt"
    imagesdir=datasetprefix+"/images"
    labelsdir=datasetprefix+"/labels"
    if not os.path.exists(imagesdir):
        os.mkdir(imagesdir)
    if convet2yoloformat:
        if not os.path.exists(labelsdir):
            os.mkdir(labelsdir)
    index=1
    with open(gtfilepath,'r') as gtfile:
        while(True):#and len(faces)<10
            filename=gtfile.readline()[:-1]
            #print('filename1:', filename)
            if(filename==""):
                continue
            #sys.stdout.write("\r"+str(index)+":"+filename+"\t\t\t")
            #sys.stdout.flush()
            imgpath=imgdir+"/"+filename
            #print('imgpath:', imgpath)
            img=cv2.imread(imgpath)
            #print('img.shape:', img.shape)
            if img is None:
                continue
            numbbox=int(gtfile.readline())
            if numbbox==0:
                continue
            bboxes=[]
            for i in range(numbbox):
                line=gtfile.readline()
                line=line.split()
                line=line[0:4]
                if(int(line[3])<=0 or int(line[2])<=0):
                    continue
                x=int(line[0])
                y=int(line[1])
                width=int(line[2])
                height=int(line[3])
                bbox=(x,y,width,height)
                bboxes.append(bbox)
                #x2=x+width
                #y2=y+height
                #face=img[x:x2,y:y2]
            
                #cv2.rectangle(img,(x,y),(x2,y2),(0,0,255))
            #cv2.imwrite('xxxx.jpg', img)
            #input()
            filename=filename.strip().split('/')[-1]
            if convet2yoloformat:
                height=img.shape[0]
                width=img.shape[1]
                txtpath=labelsdir+"/"+filename
                txtpath=txtpath[:-3]+"txt"
                ftxt=open(txtpath,'w')
                for i in range(len(bboxes)):
                    bbox=bboxes[i]
                    xcenter=round((bbox[0]+bbox[2]*0.5)/width, 6)
                    ycenter=round((bbox[1]+bbox[3]*0.5)/height, 6)
                    wr=round(bbox[2]*1.0/width, 6)
                    hr=round(bbox[3]*1.0/height, 6)
                    txtline="0 "+str(xcenter)+" "+str(ycenter)+" "+str(wr)+" "+str(hr)+"\n"
                    #print('txtline:',txtline)
                    ftxt.write(txtline)
                ftxt.close()
        index=index+1


#convertimgset(img_set="train")
convertimgset(img_set="val")