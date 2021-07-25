class AudioFile():
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("invalid extension format")
        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


# 鸭子类实现了play方法
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))


m = MP3File("file.mp3")
m.play()
