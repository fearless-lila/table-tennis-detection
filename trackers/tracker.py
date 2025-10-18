from ultralytics import YOLO
import supervision as sv
import pickle
import os
import sys
import cv2
sys.path.append('../')
from utils import get_center_of_bbox, get_bbox_width


class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20
        detections = []
        for i in range(0, len(frames), batch_size):
            detections_batch = self.model.predict(frames[i:i + batch_size], conf=0.1)
            detections += detections_batch
        return detections

    def get_object_tracks(self, frames, read_from_stub=False, stub_path=None):
        # load from cache if available
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                tracks = pickle.load(f)
            return tracks

        detections = self.detect_frames(frames)

        # initialize tracks dictionary
        tracks = {
            "player1": [],
            "player2": [],
            "racket1": [],
            "racket2": [],
            "ball": []
        }

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v: k for k, v in cls_names.items()}

            # convert to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)

            # track objects
            detections_with_tracks = self.tracker.update_with_detections(detection_supervision)

            # prepare empty dicts for current frame
            tracks["ball"].append({})
            tracks["player1"].append({})
            tracks["player2"].append({})
            tracks["racket1"].append({})
            tracks["racket2"].append({})

            for frame_detection in detections_with_tracks:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]
                track_id = frame_detection[4]

                # --- Player detection ---
                if cls_id == cls_names_inv.get('player 1'):
                    tracks["player1"][frame_num][track_id] = {"bbox": bbox}
                elif cls_id == cls_names_inv.get('player 2'):
                    tracks["player2"][frame_num][track_id] = {"bbox": bbox}

                # --- Racket detection ---
                if cls_id == cls_names_inv.get('racket 1'):
                    tracks["racket1"][frame_num][track_id] = {"bbox": bbox}
                elif cls_id == cls_names_inv.get('racket 2'):
                    tracks["racket2"][frame_num][track_id] = {"bbox": bbox}

                # --- Ball detection ---
                if cls_id == cls_names_inv.get('ball'):
                    tracks["ball"][frame_num][track_id] = {"bbox": bbox}

        # optionally cache results
        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(tracks, f)

        # Debug: print number of objects detected in first few frames
        for i in range(min(5, len(tracks["ball"]))):
            print(f"Frame {i}: player1={len(tracks['player1'][i])}, player2={len(tracks['player2'][i])}, ball={len(tracks['ball'][i])}")

        return tracks

    # ------------------------------------------------------------
    # Drawing functions
    # ------------------------------------------------------------

    def draw_ellipse(self, frame, bbox, color, track_id):
        y2 = int(bbox[3])
        x_center, _ = get_center_of_bbox(bbox)
        width = get_bbox_width(bbox)

        cv2.ellipse(
            frame,
            center=(x_center, y2),
            axes=(int(width), int(0.35 * width)),
            angle=0,
            startAngle=45,
            endAngle=235,
            color=color,
            thickness=2,
            lineType=cv2.LINE_4
        )
        return frame

    def draw_annotations(self, video_frames, tracks):
        output_video_frames = []
        for frame_num, frame in enumerate(video_frames):
            frame = frame.copy()

            player1_dict = tracks["player1"][frame_num]
            player2_dict = tracks["player2"][frame_num]
            ball_dict = tracks["ball"][frame_num]

            print(f"Frame {frame_num}: player1={player1_dict}, player2={player2_dict}, ball={ball_dict}")


            # draw player1 (red)
            for track_id, player1 in player1_dict.items():
                frame = self.draw_ellipse(frame, player1["bbox"], (0, 0, 255), track_id)

            # draw player2 (blue)
            for track_id, player2 in player2_dict.items():
                frame = self.draw_ellipse(frame, player2["bbox"], (255, 0, 0), track_id)

            # draw ball (green dot)
            for track_id, ball in ball_dict.items():
                bbox = ball["bbox"]
                x_center, y_center = get_center_of_bbox(bbox)
                cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), -1)

            output_video_frames.append(frame)

        return output_video_frames
