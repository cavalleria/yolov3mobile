
CUDA_VISIBLE_DEVICES="0" python3 -u train.py \
	--data data/face.data \
	--cfg cfg/mbnv2-yolov3-nano-3yolo-face.cfg \
	--weights weights/mobilenetv2-nano.conv.57.pt \
	--wdir ../models/person_models/nano_face \
	--img-size 320 \
	--batch-size 64 \
	--single-cls \
	--name nano_face \
	--cache-images