# yolov3mobile

This project originated from the excellent [ultralytics/yolov3](https://github.com/ultralytics/yolov3) repository and aims to implement light mobile object detector.

![Imgur](https://raw.githubusercontent.com/sthanhng/yoloface/master/assets/yolo-architecture.png)
Credit: [Ayoosh Kathuria](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)


## Data Preparation

- COCO
- COCO_person, 训练集60000张, 验证集4115张
- WiderPerson, 训练集8000张, 验证集1000张
- Citypersons, 训练集2112张, 验证集487张
- WIDERFace, 训练集12881张, 验证集3220张 

| Type | Dataset | Train data | Val data |
|:---:|:---:|:---:|:---:|
| CC | COCO_person | 60000 | 4115 |
| WP | WiderPerson | 8000  | 1000 |
| CP | City_person | 2112 | 487 |
| WF | WIDERFace | 12880 | 3226 |

## Benchmark

| Network | Input size | FLOPS | Params | COCO mAP@0.5 | Weight size |
|:---:|:---:|:---:|:---:|:---:|:---:|
| MobileNetV2-YOLOv3-Lite | 320 | 1.86G | 1.97M | 40.1 | 7.8MB |
| MobileNetV2-YOLOv3-Nano | 320 | 0.55G | 0.87M | 30.4 | 3.6MB |

### Person detection(single class)

| Network | Input size | Train data | Val data | FLOPS | Params | mAP@0.5 | Weight size |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MobileNetV2-YOLOv3-Nano | 320 | CC | CC | 0.48G | 0.71M | 55.9 | 2.9M |
| MobileNetV2-YOLOv3-Nano | 320 | WP | WP | 0.48G | 0.71M | 46.4 | 2.9M |
| MobileNetV2-YOLOv3-Nano | 320 | CC+WP | CC+WP | 0.48G | 0.71M | 53.4 | 2.9M |
| MobileNetV2-YOLOv3-Nano | 320 | CC+WP+CP | CC+WP+CP | 0.48G | 0.71M | 49.1 | 2.9M |
| MobileNetV2-YOLOv3-Nano-Anchor | 320 | CC+WP+CP | CC+WP+CP | 0.48G | 0.71M | 50.3 | 2.9M |
| YOLOv3-Ultra | 320 | CC+WP+CP | CC+WP+CP | 0.11G | 0.1M | 46.1 |515K |
| MobileNetV2-YOLOv3-Nano-3yolo | 320 | CC+WP+CP | CC+WP+CP | 0.69G | 0.76M | 56.3 | 3.2M |

### Face detection(single class)

| Network | Input size | Train data | Val data | FLOPS | Params | mAP@0.5 | Weight size | Easy | Medium | Hard |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Retinaface-m0.25 | 320 | WF | WF |  |  |  | 1.68M | 74.5 | 55.3 | 23.2 |
| YOLOv3-Ultra | 320 | WF | WF | 110M | 0.1M | 35.8 | 516K | 75.507 | 71.034 | 43.083 |
| MobileNetV2-YOLOv3-Nano-3yolo | 320 | WF | WF | 0.69G | 0.76M | 39.2 | 3.2M | 83.464 | 79.303 | 47.205 |
