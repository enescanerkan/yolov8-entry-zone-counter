"""
Author: Enes Can Erkan
Date: 2024-06-28
"""

import cv2


class VideoPlayer:
    def __init__(self, video_path):
        """
        VideoPlayer sınıfının kurucu metodu.

        :param video_path: Oynatılacak video dosyasının yolu
        """
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            print("Video başlatılamadı")
            raise Exception("Video dosyası açılamadı")

    def read_frame(self):
        """
        Bir kare okur.

        :return: Başarı durumunu ve okunan kareyi döndürür.
        """
        ret, frame = self.cap.read()
        if not ret:
            print("Video bitti")
        return ret, frame

    def release(self):
        """
        Video dosyasını serbest bırakır.
        """
        self.cap.release()

    def is_opened(self):
        """
        Video dosyasının açık olup olmadığını kontrol eder.

        :return: Video dosyasının açık olup olmadığını döndürür.
        """
        return self.cap.isOpened()
