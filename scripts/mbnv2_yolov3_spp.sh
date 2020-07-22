
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/coco2017.data \
	--cfg cfg/mbnv2-yolov3-spp.cfg \
	--weights weights/mobilenetv2-spp.conv.57.pt \
	--wdir ../models/person_models/spp_coco \
	--img-size 416 \
	--batch-size 64 \
	--name spp_coco 
