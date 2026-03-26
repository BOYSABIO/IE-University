import cv2
import numpy as np
from ultralytics import YOLO
import time
import mediapipe as mp
import logging

# Configure logging to reduce terminal output
logging.basicConfig(level=logging.ERROR)  # Only show errors

# Configure YOLO to be less verbose
YOLO.verbose = False

class GazeDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=4,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Indices for left and right eye landmarks
        self.LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        self.RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        
        # Indices for iris landmarks
        self.LEFT_IRIS = [474, 475, 476, 477]
        self.RIGHT_IRIS = [469, 470, 471, 472]
        
        # Reference points for gaze direction
        self.LEFT_EYE_REF = [362, 263]  # Left eye corners
        self.RIGHT_EYE_REF = [33, 133]  # Right eye corners
        
        # Eye aspect ratio threshold for blink detection
        self.EAR_THRESHOLD = 0.2

    def get_eye_aspect_ratio(self, landmarks, eye_indices):
        points = np.array([landmarks[i] for i in eye_indices])
        vertical_dist = np.linalg.norm(points[1] - points[5]) + np.linalg.norm(points[2] - points[4])
        horizontal_dist = np.linalg.norm(points[0] - points[3])
        ear = vertical_dist / (2.0 * horizontal_dist)
        return ear

    def get_gaze_ratio(self, landmarks, eye_indices, iris_indices, eye_ref_indices):
        eye_points = np.array([landmarks[i] for i in eye_indices])
        iris_points = np.array([landmarks[i] for i in iris_indices])
        ref_points = np.array([landmarks[i] for i in eye_ref_indices])
        
        eye_center = np.mean(eye_points, axis=0)
        iris_center = np.mean(iris_points, axis=0)
        eye_width = np.linalg.norm(ref_points[0] - ref_points[1])
        
        gaze_vector = iris_center - eye_center
        if eye_width > 0:
            gaze_vector = gaze_vector / eye_width
        
        return gaze_vector, eye_center

    def detect_gaze(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_h, frame_w = frame.shape[:2]
        
        results = self.face_mesh.process(frame_rgb)
        
        looking_at_screen = False
        gaze_vectors = []
        face_centers = []
        eyes_closed = False
        gaze_data = []  # Store gaze visualization data
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = np.array([[lm.x * frame_w, lm.y * frame_h] for lm in face_landmarks.landmark])
                
                left_ear = self.get_eye_aspect_ratio(landmarks, self.LEFT_EYE)
                right_ear = self.get_eye_aspect_ratio(landmarks, self.RIGHT_EYE)
                avg_ear = (left_ear + right_ear) / 2
                
                if avg_ear < self.EAR_THRESHOLD:
                    eyes_closed = True
                    continue
                
                left_gaze, left_center = self.get_gaze_ratio(landmarks, self.LEFT_EYE, self.LEFT_IRIS, self.LEFT_EYE_REF)
                right_gaze, right_center = self.get_gaze_ratio(landmarks, self.RIGHT_EYE, self.RIGHT_IRIS, self.RIGHT_EYE_REF)
                
                gaze_vector = (left_gaze + right_gaze) / 2
                gaze_vectors.append(gaze_vector)
                
                face_center = (left_center + right_center) / 2
                face_centers.append(face_center)
                
                # Store gaze visualization data
                gaze_data.append({
                    'left_center': left_center,
                    'right_center': right_center,
                    'face_center': face_center,
                    'left_gaze': left_gaze,
                    'right_gaze': right_gaze,
                    'gaze_vector': gaze_vector
                })
                
                if abs(gaze_vector[0]) < 0.15 and abs(gaze_vector[1]) < 0.15:
                    looking_at_screen = True
        
        return looking_at_screen, gaze_vectors, face_centers, eyes_closed, gaze_data


def calculate_head_pose(keypoints):
    nose = keypoints[0]
    left_eye = keypoints[1]
    right_eye = keypoints[2]
    left_ear = keypoints[3]
    right_ear = keypoints[4]
    
    eye_center = (left_eye + right_eye) / 2
    head_direction = eye_center - nose
    ear_vector = right_ear - left_ear
    head_tilt = np.arctan2(ear_vector[1], ear_vector[0])
    
    return head_direction, head_tilt


def is_looking_at_camera(head_direction, head_tilt, threshold=0.3):
    norm = np.linalg.norm(head_direction)
    if norm == 0:
        return False
    
    normalized_direction = head_direction / norm
    is_facing_forward = abs(normalized_direction[0]) < threshold and normalized_direction[1] > -0.1
    is_not_tilted = abs(head_tilt) < np.pi/4
    
    return is_facing_forward and is_not_tilted


def draw_pose(image, keypoints_xy, keypoints_conf, gaze_data=None, thickness=2):
    if keypoints_xy is None or len(keypoints_xy) == 0 or keypoints_conf is None:
        return image

    skeleton = [
        (0, 1), (0, 2), (1, 3), (2, 4),
        (5, 6), (5, 7), (7, 9), (6, 8),
        (8, 10), (5, 11), (6, 12), (11, 12),
        (11, 13), (13, 15), (12, 14), (14, 16)
    ]

    # Draw pose skeleton
    for person_idx, (kpts, confs) in enumerate(zip(keypoints_xy, keypoints_conf)):
        for i, (x, y) in enumerate(kpts):
            if confs[i] > 0.3:
                cv2.circle(image, (int(x), int(y)), 3, (0, 255, 0), -1)

        for i, j in skeleton:
            if confs[i] > 0.3 and confs[j] > 0.3:
                pt1 = (int(kpts[i][0]), int(kpts[i][1]))
                pt2 = (int(kpts[j][0]), int(kpts[j][1]))
                cv2.line(image, pt1, pt2, (255, 0, 0), thickness)

    # Draw gaze visualization if available
    if gaze_data:
        for gaze in gaze_data:
            arrow_length = min(image.shape[0], image.shape[1]) * 0.2
            
            # Draw left eye gaze
            left_end = gaze['left_center'] + gaze['left_gaze'] * arrow_length
            cv2.arrowedLine(image,
                          (int(gaze['left_center'][0]), int(gaze['left_center'][1])),
                          (int(left_end[0]), int(left_end[1])),
                          (0, 255, 0), 2)
            
            # Draw right eye gaze
            right_end = gaze['right_center'] + gaze['right_gaze'] * arrow_length
            cv2.arrowedLine(image,
                          (int(gaze['right_center'][0]), int(gaze['right_center'][1])),
                          (int(right_end[0]), int(right_end[1])),
                          (0, 255, 0), 2)
            
            # Draw average gaze
            avg_end = gaze['face_center'] + gaze['gaze_vector'] * arrow_length
            cv2.arrowedLine(image,
                          (int(gaze['face_center'][0]), int(gaze['face_center'][1])),
                          (int(avg_end[0]), int(avg_end[1])),
                          (255, 0, 0), 2)

    return image


def main():
    # Load the YOLOv8 detection and pose models
    det_model = YOLO('yolov8n.pt')  # Using smaller model
    pose_model = YOLO('yolov8n-pose.pt')  # Using smaller model
    
    # Initialize the gaze detector
    gaze_detector = GazeDetector()

    # Initialize camera
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Reduced resolution
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    if not camera.isOpened():
        raise IOError("Cannot open camera")

    print("Press 'q' to quit the application")
    
    # Initialize variables for screen watching detection
    looking_at_screen = False
    looking_start_time = None
    total_looking_time = 0
    last_update_time = time.time()
    update_interval = 1.0
    
    # Frame processing variables
    frame_count = 0
    process_every_n_frames = 5  # Process every 5th frame
    last_processed_frame = None
    last_processed_results = None

    while True:
        ret, frame = camera.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        frame_count += 1
        
        # Only process every nth frame
        if frame_count % process_every_n_frames == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Perform detection
            det_results = det_model(frame_rgb)
            bboxes = []
            person_count = 0
            
            for result in det_results:
                for box in result.boxes:
                    if int(box.cls[0]) == 0:  # Class 0 is person
                        bboxes.append(box.xyxy[0].cpu().numpy())
                        person_count += 1
            
            keypoints_xy = []
            keypoints_conf = []
            pose_looking = False
            
            for bbox in bboxes:
                x1, y1, x2, y2 = map(int, bbox)
                person_crop = frame_rgb[y1:y2, x1:x2]
                pose_results = pose_model(person_crop)
                
                for pose in pose_results:
                    if pose.keypoints is not None:
                        kpts = pose.keypoints.xy[0].cpu().numpy()
                        confs = pose.keypoints.conf[0].cpu().numpy()
                        kpts[:, 0] += x1
                        kpts[:, 1] += y1
                        keypoints_xy.append(kpts)
                        keypoints_conf.append(confs)
                        
                        if all(confs[i] > 0.3 for i in range(5)):
                            head_direction, head_tilt = calculate_head_pose(kpts)
                            if is_looking_at_camera(head_direction, head_tilt):
                                pose_looking = True
            
            # Detect gaze using MediaPipe
            gaze_looking, gaze_vectors, face_centers, eyes_closed, gaze_data = gaze_detector.detect_gaze(frame)
            
            # Store results for display
            last_processed_frame = frame.copy()
            last_processed_results = {
                'keypoints_xy': keypoints_xy,
                'keypoints_conf': keypoints_conf,
                'gaze_looking': gaze_looking,
                'pose_looking': pose_looking,
                'eyes_closed': eyes_closed,
                'person_count': person_count,
                'gaze_data': gaze_data
            }
        
        # Use last processed results for display
        if last_processed_frame is not None and last_processed_results is not None:
            annotated_frame = draw_pose(
                last_processed_frame.copy(),
                last_processed_results['keypoints_xy'],
                last_processed_results['keypoints_conf'],
                last_processed_results['gaze_data']
            )
            
            # Update looking time
            current_time = time.time()
            current_looking = (last_processed_results['gaze_looking'] or 
                             last_processed_results['pose_looking']) and not last_processed_results['eyes_closed']
            
            if current_looking:
                if not looking_at_screen:
                    looking_start_time = current_time
                looking_at_screen = True
            else:
                if looking_at_screen:
                    if looking_start_time is not None:
                        total_looking_time += current_time - looking_start_time
                    looking_start_time = None
                looking_at_screen = False
            
            # Update display every second
            if current_time - last_update_time >= update_interval:
                last_update_time = current_time
            
            # Add status text
            if last_processed_results['eyes_closed']:
                status = "Eyes closed"
            else:
                status = "Looking at screen" if looking_at_screen else "Not looking at screen"
                if looking_at_screen:
                    if last_processed_results['gaze_looking'] and last_processed_results['pose_looking']:
                        status += " (Both methods)"
                    elif last_processed_results['gaze_looking']:
                        status += " (Gaze)"
                    else:
                        status += " (Pose)"
            
            cv2.putText(annotated_frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                        (0, 255, 0) if looking_at_screen else (0, 0, 255), 2)
            
            # Add person count
            cv2.putText(annotated_frame, f"People detected: {last_processed_results['person_count']}", 
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Add total looking time
            minutes = int(total_looking_time // 60)
            seconds = int(total_looking_time % 60)
            time_text = f"Total looking time: {minutes:02d}:{seconds:02d}"
            cv2.putText(annotated_frame, time_text, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Display the frame
            cv2.imshow('Optimized Screen Watching Detection', annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main() 