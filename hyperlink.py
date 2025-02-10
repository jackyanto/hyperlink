import cv2
import os
import ctypes
import numpy as np

class HyperLink:
    def __init__(self, video_path: str):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

    def get_screen_resolution(self):
        user32 = ctypes.windll.user32
        screen_resolution = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screen_resolution

    def enhance_video(self, output_path: str, target_frame_rate: int = 60):
        screen_width, screen_height = self.get_screen_resolution()
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, target_frame_rate, (screen_width, screen_height))

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            
            frame = cv2.resize(frame, (screen_width, screen_height), interpolation=cv2.INTER_LINEAR)
            out.write(frame)

        self.cap.release()
        out.release()
        print(f"Enhanced video saved to {output_path}")

    def optimize_and_play(self):
        enhanced_video_path = "enhanced_video.mp4"
        self.enhance_video(enhanced_video_path)
        os.startfile(enhanced_video_path)

if __name__ == "__main__":
    video_file = "your_video_file.mp4"  # replace with your video file path
    hyperlink = HyperLink(video_file)
    hyperlink.optimize_and_play()