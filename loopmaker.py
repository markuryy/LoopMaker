# -*- coding: utf-8 -*-
"""
LoopMaker Local Script Version

This script is adapted from a Google Colab notebook for local execution.
Ensure you have torch, torchvision, and moviepy installed in your local environment.
"""

# Import necessary libraries
import torch
from torchvision import models, transforms
from moviepy.editor import VideoFileClip, concatenate_videoclips
import numpy as np
from PIL import Image
from scipy.spatial.distance import cosine
from datetime import timedelta
import matplotlib.pyplot as plt

class FeatureExtractor:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = models.resnet50(pretrained=True).to(self.device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def extract_features(self, image):
        image = self.transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            features = self.model(image)
        return features.squeeze().cpu().numpy()

def load_video(video_path):
    return VideoFileClip(video_path)

def get_video_frames(video, every_n_frames=30):
    total_frames = int(video.fps * video.duration)
    frames = [video.get_frame(i / video.fps) for i in range(0, total_frames, every_n_frames)]
    return frames

def extract_features_from_frames(frames, feature_extractor):
    features = []
    for frame in frames:
        pil_image = Image.fromarray(frame.astype('uint8'), 'RGB')
        feature = feature_extractor.extract_features(pil_image)
        features.append(feature)
    return features

def find_potential_loops(features, threshold=0.1):
    loop_candidates = []
    for i in range(len(features)):
        for j in range(i + 1, len(features)):
            similarity = 1 - cosine(features[i], features[j])
            if similarity > threshold:
                loop_candidates.append((i, j, similarity))
    loop_candidates.sort(key=lambda x: x[2], reverse=True)
    return loop_candidates

def display_loops(loops, frames_per_second):
    top_loops = loops[:10]  # Limit to top 10 loops
    for index, (start, end, similarity) in enumerate(top_loops):
        start_time = timedelta(seconds=(start * 30 / frames_per_second))
        end_time = timedelta(seconds=(end * 30 / frames_per_second))
        duration = timedelta(seconds=((end - start) * 30 / frames_per_second))
        print(f"{index}: Start: {start_time}, End: {end_time}, Duration: {duration}, Similarity: {similarity}")

# Main execution starts here
if __name__ == "__main__":
    video_filename = input("Enter the path to your video file: ")
    video = load_video(video_filename)
    frames = get_video_frames(video)
    extractor = FeatureExtractor()
    features = extract_features_from_frames(frames, extractor)

    loops = find_potential_loops(features)
    display_loops(loops, video.fps)

    selected_index = int(input("Enter the index of the best loop: "))
    output_format = input("Enter the desired format (mp4/gif): ").lower()
    filename = input("Enter a filename (without extension): ")

    if output_format not in ['mp4', 'gif']:
        print("Invalid format selected. Defaulting to mp4.")
        output_format = 'mp4'

    selected_loop = loops[selected_index]
    start_frame, end_frame, _ = selected_loop
    start_time, end_time = start_frame * 30 / video.fps, end_frame * 30 / video.fps
    loop_clip = video.subclip(start_time, end_time)

    if output_format == 'mp4':
        output_filename = f"{filename}.mp4"
        loop_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")
    elif output_format == 'gif':
        output_filename = f"{filename}.gif"
        loop_clip.resize(width=800).write_gif(output_filename, fps=20)
