"""
Author: Enes Can Erkan
Date: 2024-06-28
"""

import supervision as sv
from ultralytics import YOLO
import numpy as np


class ObjectDetector:
    def __init__(self, model_path, zone_polygon, frame_resolution):
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
            color=sv.Color.BLACK,
            thickness=5,
            text_thickness=7,
            text_scale=2,
            text_color=sv.Color.WHITE
        )

    def detect_objects(self, frame):
        result = self.model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_ultralytics(result)
        return detections

    def count_class_0_in_zone(self, detections):
        count = 0
        for _, _, class_id in detections:
            if class_id == 0 and self.zone.contains(detection=(_, _, class_id)):
                count += 1
        return count

    def annotate_frame(self, frame, detections):
        labels = []
        try:
            labels = [
                f"{self.model.model.names[class_id]} {confidence:0.2f}"
                for _, confidence, class_id in detections
            ]
        except ValueError:
            pass

        annotated_frame = self.box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        return annotated_frame

    def annotate_zone(self, frame, detections):
        self.zone.trigger(detections=detections)
        annotated_frame = self.zone_annotator.annotate(scene=frame)
        return annotated_frame

