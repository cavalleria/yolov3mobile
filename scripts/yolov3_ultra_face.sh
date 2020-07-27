
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/face.data \
	--cfg cfg/yolov3-ultra-face.cfg \
	--weights "" \
	--wdir ../models/person_models/ultra_face_lr \
	--img-size 320 \
	--batch-size 64 \
	--single-cls \
	--multi-scale \
	--name ultra_face_lr \
	--cache-images

#--weights weights/mobilenetv2-nano.conv.57.pt \