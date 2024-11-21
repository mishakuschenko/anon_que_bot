#import os

class ReadFile:
    def read(self, path):
        try:
            with open(path) as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File not found")


