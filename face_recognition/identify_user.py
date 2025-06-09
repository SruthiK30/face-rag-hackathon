import face_recognition
import cv2
import os

KNOWN_FACES_DIR = "known_faces"

def identify_face():
    known_encodings = []
    known_names = []

    # Load all known faces
    for name in os.listdir(KNOWN_FACES_DIR):
        img_path = os.path.join(KNOWN_FACES_DIR, name)
        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(name)[0])

    # Start webcam
    video = cv2.VideoCapture(0)
    print("🎥 Scanning for known face. Press 'q' to exit.")

    while True:
        ret, frame = video.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            if True in matches:
                matched_index = matches.index(True)
                user_name = known_names[matched_index]
                video.release()
                cv2.destroyAllWindows()
                return user_name

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return None
