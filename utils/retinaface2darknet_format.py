import os
import cv2

txt_path = "/usr/src/face/WIDER_Face/r_vallabel.txt"
save_path = "/usr/src/face/WIDER_Face/v_label/"
prefix = "/usr/src/face/WIDER_Face/images"
if not os.path.exists(save_path):
    os.makedirs(save_path)


f2 = open(txt_path, "r")
# lines = f.readlines() + f2.readlines()
lines = f2.readlines()
isFirst = True
labels = []
words = []
imgs_path = []
for line in lines:
    line = line.rstrip()
    if line.startswith('#'):
        if isFirst is True:
            isFirst = False
        else:
            labels_copy = labels.copy()
            words.append(labels_copy)
            labels.clear()
        path = line[1:].strip()
        # path = txt_path.replace('label.txt','images/') + path
        path = os.path.join(txt_path.replace(txt_path.split("/")[-1], "images"), path)

        imgs_path.append(path)
    else:
        line = line.split(' ')
        label = [float(x) for x in line]
        labels.append(label)

words.append(labels)
image_count = 0
for path,word in zip(imgs_path,words):
    path = path.split('/')[-1]
    ima_path = os.path.join(prefix, path)
    img = cv2.imread(ima_path)
    img_height = img.shape[0]
    img_width = img.shape[1]
    rel_bbox_list = []
    for anno in word:
        x1, y1, w, h = anno[:4]
        if w < 10 or h < 10:
            #img[int(y1):int(y1+h),int(x1):int(x1+w),:] = 127
            continue
        # cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)
        rel_cx = str(float((x1 + int(w/2)) / img_width))
        rel_cy = str(float((y1 + int(h/2)) / img_height))
        rel_w = str(float(w / img_width))
        rel_h = str(float(h / img_height))

        string_bbox = "0 " + rel_cx + " " + rel_cy + " " + rel_w + " " + rel_h
        rel_bbox_list.append(string_bbox)
    image_count += 1
    print(image_count)


    #cv2.imwrite( save_path + save_image_name + ".jpg", img)
    with open(save_path + path.split('.')[0] + ".txt", "w") as f:
        for i in rel_bbox_list:
            f.write(i + "\n")