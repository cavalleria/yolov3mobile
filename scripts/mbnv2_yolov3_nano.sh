
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/coco2017.data \
	--cfg cfg/mbnv2-yolov3-nano.cfg \
	--weights weights/mobilenetv2-nano.conv.57.pt \
	--wdir ../models/person_models/nano_bs256 \
	--img-size 320 \
	--batch-size 256 \
	--name nano_bs256