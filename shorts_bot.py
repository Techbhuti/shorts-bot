import os
import subprocess

def create_short_video(input_video, output_output="final_short.mp4"):
    """
    Processes a video into a vertical 9:16 format suitable for YouTube Shorts 
    using ffmpeg processing.
    """
    print(f"Processing {input_video} into vertical short format...")
    
    # FFmpeg command to crop/scale to 9:16 vertical video resolution (1080x1920)
    cmd = [
        "ffmpeg", "-i", input_video,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        output_output, "-y"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Success! Short video saved as: {output_output}")
    except subprocess.CalledProcessError as e:
        print(f"Error during ffmpeg processing: {e}")

if __name__ == "__main__":
    print("YouTube Shorts Automation Pipeline Initialized.")
