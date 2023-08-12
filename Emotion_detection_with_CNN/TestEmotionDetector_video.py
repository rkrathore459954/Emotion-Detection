import cv2
import numpy as np
from keras.models import model_from_json

def video_upload(path):
    happy_image = cv2.imread("Emotion_detection_with_CNN/emojis/happy.png")
    sad_image = cv2.imread("Emotion_detection_with_CNN/emojis/sad.png")
    angry_image = cv2.imread("Emotion_detection_with_CNN/emojis/angry.png")
    surprised_image = cv2.imread("Emotion_detection_with_CNN/emojis/surprised.png")
    neutral_image = cv2.imread("Emotion_detection_with_CNN/emojis/neutral.png")
    disgust_image = cv2.imread("Emotion_detection_with_CNN/emojis/disgust.png")
    fearful_image = cv2.imread("Emotion_detection_with_CNN/emojis/fearful.png")

    emotion_dict = {0: angry_image, 1: disgust_image, 2: fearful_image, 3: happy_image, 4: neutral_image, 5: sad_image, 6: surprised_image}

    emotion_dict_text = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    # load json and create model
    json_file = open('Emotion_detection_with_CNN/model/emotion_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    emotion_model = model_from_json(loaded_model_json)

    # load weights into new model
    emotion_model.load_weights("Emotion_detection_with_CNN/model/emotion_model.h5")
    print("Loaded model from disk")

    # start the webcam feed
    # cap = cv2.VideoCapture(0)

    # pass here your video path #"C:\Users\Rohit\Downloads\pexels-gabby-k-5273028.mp4"
    # you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
    cap = cv2.VideoCapture(path)

    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        if not ret:
            break
        face_detector = cv2.CascadeClassifier('Emotion_detection_with_CNN/haarcascades/haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces available on camera
        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        # take each face available on the camera and Preprocess it
        for (x, y, w, h) in num_faces:
            face_region = frame[y:y+h, x:x+w]

            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)

            face_gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)

            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(face_gray, (48, 48)), -1), 0)
            
            # predict the emotions
            emotion_prediction = emotion_model.predict(cropped_img)

            maxindex = int(np.argmax(emotion_prediction))

            emotion_image = emotion_dict[maxindex]

            # Resize the emotion image to match the face region
            emotion_image = cv2.resize(emotion_image, (w, h))

            # Overlay the emotion image on top of the face region
            alpha = 0.5
            beta = 1 - alpha
            gamma = 0
            overlay = cv2.addWeighted(face_region, alpha, emotion_image, beta, gamma)
            cv2.putText(frame, emotion_dict_text[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            frame[y:y+h, x:x+w] = overlay

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
