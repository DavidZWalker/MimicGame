from pygame import mixer

class MusicController(object):
    def __init__(self):
        self.bg_music_file = "bg_music.mp3"
        self.bg_music_paused_file = "bg_music_paused.mp3"
        self.active_music_file = ""

    def start(self):
        if self.active_music_file is not self.bg_music_file:
            current_music_pos = mixer.music.get_pos() / 1000.0
            mixer.music.stop()
            mixer.music.load(self.bg_music_file)
            mixer.music.play(-1, current_music_pos)
            self.active_music_file = self.bg_music_file

    def pause(self):
        if self.active_music_file is not self.bg_music_paused_file:
            current_music_pos = mixer.music.get_pos() / 1000.0
            mixer.music.stop()
            mixer.music.load(self.bg_music_paused_file)
            mixer.music.play(-1, current_music_pos)
            self.active_music_file = self.bg_music_paused_file
