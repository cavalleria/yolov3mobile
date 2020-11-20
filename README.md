# yolov3mobile

This project originated from the excellent [ultralytics/yolov3](https://github.com/ultralytics/yolov3) repository and aims to implement light mobile object detector.

![Imgur](https://raw.githubusercontent.com/sthanhng/yoloface/master/assets/yolo-architecture.png)
Credit: [Ayoosh Kathuria](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)

## Data Preparation

- COCO
- COCO_person, 训练集60000张, 验证集4115张
- WiderPerson, 训练集8000张, 验证集1000张
- Citypersons, 训练集2112张, 验证集487张
- ICCVWider, 包括监控(sur)和自动驾驶(ad), 训练集58026张, 验证集3233张
- WIDERFace, 训练集12881张, 验证集3220张
- AI-Challenger single, 训练集22446张, 验证集1500张
- AI-Challenger, 训练集210000张, 验证集30000张

#### [**Baidu Drive**](https://pan.baidu.com/s/1OZkfYHTCBUPK6q0cW8tSdg)(code:9mjn)

| Type | Dataset | Train data | Val data |
|:---:|:---:|:---:|:---:|
| CC | COCO_person | 60000 | 4115 |
| WP | WiderPerson | 8000  | 1000 |
| CP | City_person | 2112 | 487 |
| Wsur | ICCV_sur | 5563 | 2369 |
| Wad | ICCV_ad | 52436 | 864 |
| ACS | AI-Challenger | 22446 | 1500 |
| AC | AI-Challenger | 210000 | 30000 |
| WF | WIDERFace | 12880 | 3226 |

## Benchmark

## COCO detection

| Network | Input size | FLOPS | Params | COCO mAP@0.5 | Weight size |
|:---:|:---:|:---:|:---:|:---:|:---:|
| MobileNetV2-YOLOv3-Lite | 320 | 1.86G | 1.97M | 40.1 | 7.8MB |
| MobileNetV2-YOLOv3-Nano | 320 | 0.55G | 0.87M | 30.4 | 3.6MB |

### Person detection(single class)

| Network | Input size | Train data | Val data | FLOPS | Params | mAP@0.5 | Weight size |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MobileNetV2-YOLOv3-Nano | 320 | CC+WP+CP | CC+WP+CP | 0.48G | 0.71M | 50.3 | 2.9M |
| MobileNetV2-YOLOv3-Nano-3yolo | 320 | CC+WP+CP | CC+WP+CP | 0.69G | 0.76M | 56.3 | 3.2M |
| YOLOv3-Ultra | 320 | CC+WP+CP | CC+WP+CP | 0.11G | 0.1M | 46.1 |515K |
| YOLOv3-Ultra | 320 | CC+WP+CP+Wsur | CC+WP+CP | 0.11G | 0.1M | 45.4 |515K |
| YOLOv3-Ultra | 320 | CC | CC | 0.11G | 0.1M | 48.1 |515K |
| MobileNetV2-YOLOv3-Nano | 320 | AC | AC | 0.48G | 0.71M | 57.0 | 2.9M |
| YOLOv3-Ultra | 320 | AC | AC | 0.11G | 0.1M | 44.5 | 515K |

### Face detection(single class)

| Network | Input size | Train data | Val data | FLOPS | Params | Weight size | mAP@0.5 | Weight size | Easy | Medium | Hard |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Retinaface-m0.25 | 320 | WF | WF | - | - | 1.68M | - | 1.68M | 74.5 | 55.3 | 23.2 |
| YOLOv3-Ultra | 320 | WF | WF | 110M | 0.1M | 515K | 35.8 | 516K | 75.507 | 71.034 | 43.083 |
| MobileNetV2-YOLOv3-Nano-3yolo | 320 | WF | WF | 0.69G | 0.76M | 3.2M | 39.2 | 3.2M | 83.464 | 79.303 | 47.205 |
