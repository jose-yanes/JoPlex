import os, os.path

def get_videos(directory):
    # num_files = len([name for name in os.listdir(directory)])
    available_videos = [name for name in os.listdir(directory)]
    return available_videos
