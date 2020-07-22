
python3 -u detect.py \
	--cfg cfg/yolov3-ultra.cfg \
	--weights ../models/person_models/ultra_person_cocowidercity/best.pt \
	--source resource/test_video_1.mp4 \
	--img-size 320 \
	--device 0 \
	--conf-thres 0.3 \
	--iou-thres 0.6

