
python3 -u detect.py \
	--cfg cfg/yolov3-ultra-face.cfg \
	--weights ../models/person_models/ultra_face/best_ultra_face.pt \
	--source resource/test_video_1.mp4 \
	--img-size 320 \
	--device 0 \
	--conf-thres 0.3 \
	--iou-thres 0.6 \
	--names data/face.names

