from utils import read_video, save_video

def main():
    video_frames = read_video('/Users/lilahu/Desktop/Code/table-tennis-detection/input_videos/fan_vs_lee.mp4')

    save_video(video_frames, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()