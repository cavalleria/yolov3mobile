
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/person.data \
	--cfg cfg/yolov3-ultra.cfg \
	--weights "" \
	--wdir ../models/person_models/ultra_person_cocowidercity \
	--img-size 320 \
	--batch-size 64 \
	--single-cls \
	--multi-scale \
	--name ultra_person_cocowidercity \
	--cache-images

#--weights weights/mobilenetv2-nano.conv.57.pt \