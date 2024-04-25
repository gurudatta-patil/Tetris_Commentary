from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import cv2

# Function to download YouTube video
def download_video(url, output_path, filename):
    yt = YouTube(url)
    yt.streams.filter(res="720p", progressive=True, file_extension='mp4').first().download(output_path,filename)

# Function to extract frames from video
def extract_frames(video_path, output_folder):
    clip = VideoFileClip(video_path)
    fps = clip.fps
    
    duration = int(clip.duration)
    os.makedirs(output_folder, exist_ok=True)
    print("Duration:", duration)
    for i in range(60, 120, 3):
        frame = clip.get_frame(i)
        frame_path = os.path.join(output_folder, f"frame_{i:04d}.jpg")
        cv2.imwrite(frame_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
# Example usage
def extract_video(video_path, output_path, start_time, end_time):
    # Load the video
    clip = VideoFileClip(video_path)

    # Extract the subclip
    subclip = clip.subclip(start_time, end_time)

    # Remove the audio
    subclip = subclip.without_audio()

    # Write the output
    subclip.write_videofile(output_path, codec='libx264')

def downloader(url):
    youtube_url = url
    output_folder = "frames"
    video_path = "./tmp/"
    video_filename = "video.mp4"
    print("Current working directory:", os.getcwd())
    download_video(youtube_url, video_path,video_filename)
    extract_frames("./tmp/video.mp4", output_folder)
    extract_video("./tmp/video.mp4", "./tmp/output.mp4", 60, 120)

