from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioClip, AudioFileClip, concatenate_audioclips
import numpy as np
import librosa
from pydub.effects import speedup
import pydub

def make_blank_frame(t):
  numpy_array = np.array([0,0])
  return numpy_array

def text_to_mp3(text, outfile_name):
    # Create a gTTS object
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("./tmp/temp.mp3")

    # Load audio with librosa
    sound = pydub.AudioSegment.from_file("./tmp/temp.mp3", format="mp3")
    # Calculate speed factor
    desired_duration = 60  # 1 minute
    speed_factor = sound.duration_seconds / desired_duration

    # Adjust speed
    sped_up_sound = speedup(sound, playback_speed=speed_factor)

    # Save adjusted audio
    sped_up_sound.export(outfile_name, format="mp3")

def add_mp3_to_mp4(mp4file, mp3file, outfile):
  vid_clip = VideoFileClip(mp4file)
  audio_clip = AudioFileClip(mp3file)

  if audio_clip.duration < vid_clip.duration:
      # Calculate the duration of the required blank audio clip
      blank_duration = vid_clip.duration - audio_clip.duration
      # Create a blank audio clip with the required duration
      blank_audio = AudioClip(make_blank_frame, duration=blank_duration)
      # Concatenate the generated audio with the blank audio
      final_audio = concatenate_audioclips([audio_clip, blank_audio])
  else:
      # If the audio duration is longer, trim it to match the video duration
      final_audio = audio_clip.subclip(0, vid_clip.duration)

  video_with_audio = vid_clip.set_audio(final_audio)
  video_with_audio.write_videofile(outfile)

def add_ttl_to_video(mp4file, text, outfile):
  tmp_mp3_filename = 'audio.mp3'
  text_to_mp3(text, tmp_mp3_filename)
  add_mp3_to_mp4(mp4file, tmp_mp3_filename, outfile)

  