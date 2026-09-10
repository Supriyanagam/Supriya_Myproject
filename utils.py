import cv2

FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

EYE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

MOUTH_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

def detect_driver_state(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    result = {
        "face_detected": len(faces) > 0,
        "eyes_closed": False,
        "mouth_open": False
    }

    if len(faces) == 0:
        return result

    # Use the largest detected face as the driver face.
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    face_gray = gray[y:y+h, x:x+w]
    face_color = frame[y:y+h, x:x+w]

    eyes = EYE_CASCADE.detectMultiScale(
        face_gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(20, 20)
    )

    # This simple prototype treats a lack of detected eyes as possible closure.
    result["eyes_closed"] = len(eyes) == 0

    # Search for a mouth/smile in the lower half of the face.
    lower_gray = face_gray[int(h * 0.45):h, :]
    mouths = MOUTH_CASCADE.detectMultiScale(
        lower_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(30, 15)
    )

    result["mouth_open"] = len(mouths) > 0

    # Draw face box and detected eyes.
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for ex, ey, ew, eh in eyes:
        cv2.rectangle(
            frame,
            (x+ex, y+ey),
            (x+ex+ew, y+ey+eh),
            (0, 255, 0),
            2
        )

    return result
