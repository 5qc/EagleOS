from .colors import *

class error:
    def __init__(self, msg):
        print(f"{color(255, 0, 0, 'ERROR')}| {msg}")

    def preset(msg):
        if msg == "notsupported":
            return "Only .imp files are supported."
        elif msg == "filenotexists":
            return "File does not exist."
        elif msg == "invalidcmd":
            return "Invalid command."
