import moviepy.editor
from pathlib import Path


def main(file):
    video = moviepy.editor.VideoFileClip(f'{file}')
    audio = video.audio
    audio.write_audiofile(f'{file.stem}.mp3')


if __name__ == '__main__':
    video_file = Path('clip.mp4')
    main(video_file)

