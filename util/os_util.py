import os


def create_directory(path):
    try:
        os.mkdir(path)
        return True
    except Exception as e:
        print("Error: ", e)
        return False
