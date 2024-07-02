"""
Author: Enes Can Erkan
Date: 2024-06-28
"""

import cv2
from video_player import VideoPlayer
from object_detector import ObjectDetector
from zone_polygons import get_human_zone_polygon

def main():
    """
    Ana fonksiyon, video oynatma ve nesne tespiti işlemlerini yönetir.
    """
    video_path = "video/subway.mp4"
    model_path = "model/yolov8m.pt"
    video_player = VideoPlayer(video_path)

    frame_width = int(video_player.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_player.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    object_detector = ObjectDetector(model_path, get_human_zone_polygon(), (frame_width, frame_height))

    while video_player.is_opened():
        ret, frame = video_player.read_frame()
        if not ret:
            break

        detections = object_detector.detect_objects(frame)
        annotated_frame1 = object_detector.annotate_frame(frame, detections)
        annotated_frame2 = object_detector.annotate_zone(annotated_frame1, detections)

        cv2.imshow("Annotated Frame", annotated_frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_player.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
