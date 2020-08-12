import os
import json
from pathlib import Path
import cv2

json_file = '../../persondata/person/ai_challenger_all/keypoint_validation_annotations_20170911.json'
save_path = '../../persondata/person/ai_challenger_all/labels_val'
prefix = '../../persondata/person/ai_challenger_all/keypoint_validation_images_20170911'
if not os.path.exists(save_path):
    os.makedirs(save_path)
with open(json_file,'r') as f:
    data = json.load(f)
    print(type(data))
    print(len(data))

    
    for i, item in enumerate(data):
        #print("item", item)
        file_name = item["image_id"]
        #print("file_name", file_name)
        img = cv2.imread(os.path.join(prefix, file_name)+'.jpg', -1)
        image_h, image_w = img.shape[0], img.shape[1]
        #print('image_h, image_w', image_h, image_w)
        human_ann = item['human_annotations']
        rel_bbox_list = []
        for key, bbox in human_ann.items():
            #print(key, bbox)

            bw = bbox[2]-bbox[0]
            bh = bbox[3]-bbox[1]
            rel_cx = str(float((bbox[0] + bw/2) / image_w))
            rel_cy = str(float((bbox[1] + bh/2) / image_h))
            rel_w = str(float(bw / image_w))
            rel_h = str(float(bh / image_h))
            #print(bw,bh)
            #print(rel_cx, rel_cy, rel_w, rel_h)
            #input()
            string_bbox = "0 " + rel_cx + " " + rel_cy + " " + rel_w + " " + rel_h
            rel_bbox_list.append(string_bbox)
        with open(os.path.join(save_path, file_name + ".txt"), "w") as f:
            for it in rel_bbox_list:
                f.write(it + "\n")
        
        if i % 10000 ==0:
            print('Finished', i)
        

