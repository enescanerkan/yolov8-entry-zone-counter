"""
Author: Enes Can Erkan
Date: 2024-06-28
"""

import supervision as sv
from ultralytics import YOLO
import numpy as np

class ObjectDetector:
    def __init__(self, model_path, zone_polygon, frame_resolution):
        """
        ObjectDetector sınıfının kurucu metodu.

        :param model_path: Model dosyasının yolu
        :param zone_polygon: İzleme bölgesi çokgeni
        :param frame_resolution: Çerçeve çözünürlüğü (genişlik, yükseklik)
        """
        self.model = YOLO(model_path)
        self.box_annotator = sv.BoxAnnotator(
            thickness=2,
            text_thickness=2,
            text_scale=1
        )
        zone_polygon = (zone_polygon * np.array(frame_resolution)).astype(int)
        self.zone = sv.PolygonZone(polygon=zone_polygon)
        self.zone_annotator = sv.PolygonZoneAnnotator(
            zone=self.zone,
            color=sv.Color.BLACK,  # yeşil olarak ayarladık
            thickness=5,
            text_thickness=7,
            text_scale=2,
            text_color=sv.Color.WHITE
        )

    def detect_objects(self, frame):
        """
        Çerçevede nesneleri tespit eder.

        :param frame: Video karesi
        :return: Tespit edilen nesneler
        """
        result = self.model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_ultralytics(result)
        return detections

    def annotate_frame(self, frame, detections):
        """
        Çerçeveyi tespit edilen nesnelerle açıklamalı hale getirir.

        :param frame: Video karesi
        :param detections: Tespit edilen nesneler
        :return: Açıklamalı çerçeve
        """
        try:
            labels = [
                f"{self.model.model.names[class_id]} {confidence:0.2f}"
                for _, confidence, class_id in detections
            ]
        except ValueError:
            labels = []

        annotated_frame = self.box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        return annotated_frame

    def annotate_zone(self, frame, detections):
        """
        Çerçeveyi belirli bir izleme bölgesi ile açıklamalı hale getirir.

        :param frame: Video karesi
        :param detections: Tespit edilen nesneler
        :return: İzleme bölgesi ile açıklamalı çerçeve
        """
        self.zone.trigger(detections=detections)
        annotated_frame = self.zone_annotator.annotate(scene=frame)
        return annotated_frame
