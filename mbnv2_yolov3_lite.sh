
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/coco2017.data \
	--cfg cfg/mbnv2-yolov3-lite.cfg \
	--weights weights/mobilenetv2-lite.conv.57.pt
	--img-size 320 \
	--batch-size 32
