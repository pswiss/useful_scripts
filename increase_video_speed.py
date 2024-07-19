import os
from moviepy.editor import *

def change_video_speed(input_path, output_path, speed_factor):
    video = VideoFileClip(input_path)
    new_video = video.fx(vfx.speedx, speed_factor)
    new_video.write_videofile(output_path)

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    speed_factor = float(input("Enter the speed factor (e.g., 2.0 for 2x speed): "))

    for filename in os.listdir(folder_path):
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            input_path = os.path.join(folder_path, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(folder_path, f"{name}_{speed_factor}x{ext}")
            print(f"Processing {input_path} -> {output_path}")
            change_video_speed(input_path, output_path, speed_factor)
            print(f"Finished {output_path}")

if __name__ == "__main__":
    main()
