# Object Detection with YOLOv8 (YOLOv8 ile Nesne Tespiti)

This project implements an object detection system using the YOLOv8 model. It includes video playback, object detection, and zone annotation. When a human is detected in a specified area, the system can be extended to trigger a buzzer and LED connected to an Arduino.

(Bu proje, YOLOv8 modelini kullanarak bir nesne tespit sistemi uygular. Video oynatma, nesne tespiti ve bölge açıklaması içerir. Belirli bir alanda insan tespit edildiğinde, sisteme bir Arduino'ya bağlı bir buzzer ve LED'i tetiklemek için genişletilebilir.)

## File Structure (Dosya Yapısı)

- `main.py`: Main script to run the video player and object detector. (Video oynatıcı ve nesne tespit cihazını çalıştırmak için ana betik.)
- `object_detector.py`: Contains the `ObjectDetector` class for detecting and annotating objects and zones. (`ObjectDetector` sınıfını nesneleri ve bölgeleri tespit etmek ve açıklamak için içerir.)
- `video_player.py`: Contains the `VideoPlayer` class for reading and playing video frames. (Video karelerini okumak ve oynatmak için `VideoPlayer` sınıfını içerir.)

## Requirements (Gereksinimler)

- Python 3.x
- OpenCV
- Ultralytics YOLO
- Supervision

## Installation (Kurulum)

1. Clone the repository (Depoyu klonlayın):
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

![image](https://github.com/enescanerkan/YOLOv8_Object_Detection/assets/154825118/845114d2-13ae-4f13-b34a-d8cd7113c40e)
