import moviepy.editor
import analyser.caption
import hashlib
import time


class Spliter:
    @staticmethod
    def split_to_mp3(film_path: str, target_path: str, caption: analyser.caption.Caption):
        audio_file_name = hashlib.md5(str(time.time())) + ".mp3"
        film_clip = moviepy.editor.VideoFileClip(film_path)
        film_clip = film_clip.subclip(t_start=str(caption.start_tick), t_end=str(caption.end_tick))
        audio_clip = film_clip.audio
        audio_clip.write_audiofile(target_path+"\\"+audio_file_name)
        return audio_file_name


