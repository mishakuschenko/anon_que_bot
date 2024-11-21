#import os

class ReadFile:
    def read(self, path) -> str:
        try:
            with open(path) as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File not found")


