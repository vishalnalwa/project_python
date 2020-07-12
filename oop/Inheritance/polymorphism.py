class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("invalid format")
        self.filename = filename

class Mp3_File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class Wav_File(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class Ogg_File(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))