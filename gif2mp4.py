import os
from moviepy.editor import VideoFileClip

# Get a list of all .gif files in the current directory
gif_files = [file for file in os.listdir() if file.lower().endswith(".gif")]

# Convert each .gif file to .mp4
for gif_file in gif_files:
    mp4_file = gif_file.replace(".gif", ".mp4")
    clip = VideoFileClip(gif_file)
    clip.write_videofile(mp4_file, codec="libx264")

    print(f"{gif_file} was successfully converted to {mp4_file}")
