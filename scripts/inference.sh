
python3 -u ../detect.py \
	--cfg cfg/mbnv2-yolov3-nano.cfg \
	--weights ../models/person_models/nano/best.pt \
	--source resource/test_video_2.mp4 \
	--img-size 320 \
	--conf-thres 0.3 \
	--iou-thres 0.4 \
	--device 0 \

