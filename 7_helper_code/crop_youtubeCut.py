import cv2
import numpy as np
import mediapipe as mp
from tqdm import tqdm

def calc_bounding_rect(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_array = np.empty((0, 2), int)
    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_point = [np.array((landmark_x, landmark_y))]
        landmark_array = np.append(landmark_array, landmark_point, axis=0)
    x, y, w, h = cv2.boundingRect(landmark_array)
    return [x, y, x + w, y + h]

max_num_faces = 1
refine_landmarks = True
min_detection_confidence = 0.1
min_tracking_confidence = 0.1

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=max_num_faces,
                                  refine_landmarks=refine_landmarks,
                                  min_detection_confidence=min_detection_confidence,
                                  min_tracking_confidence=min_tracking_confidence,)

filepath = "C:/Users/EGAT/Documents/GitHub/corpus_dataset/4_youtube_cut/lebel/files/lasted_version/v1/Club_Friday_Show.csv"
vdopath = "C:/Users/EGAT/Documents/GitHub/corpus_dataset/4_youtube_cut/videos/videos/Club_Friday_Show.mp4"


df = pd.read_csv(filepath)
T_frames, fps = caminfo(vdopath)
frames, labels = [], []

for i in tqdm(range(df.shape[0])):
  for j in range(df['start_frame'][i], df['end_frame'][i]):
    cap = cv2.VideoCapture(vdopath)
    cap.set(cv2.CAP_PROP_POS_FRAMES, j)
    success, image = cap.read()
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    try:
        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
              try:
                brect = calc_bounding_rect(image, face_landmarks)
                image = image[brect[1]:brect[3],brect[0]:brect[2]]
                cropped = cv2.resize(image, (384, 384), interpolation=cv2.INTER_AREA)
                emotion = df['label'][i]
                frames.append(cropped); labels.append(emotion);
              except:
                print('Error')
    except:
        print("error out")
          
frames_ar, labels_ar = np.array(frames), np.array(labels)
np.save('Club_Friday_Show_x.npy', frames_ar)
np.save('Club_Friday_Show_y.npy', labels_ar)