import cv2
import time
from config import EYE_CLOSED_SECONDS, MOUTH_OPEN_SECONDS
from utils import detect_driver_state
from alert import play_alert

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    eye_closed_start = None
    mouth_open_start = None
    last_alert = 0
    alert_cooldown = 3

    print("Intelligent Driver Monitoring System started.")
    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        state = detect_driver_state(frame)

        now = time.time()

        if state["eyes_closed"]:
            if eye_closed_start is None:
                eye_closed_start = now
        else:
            eye_closed_start = None

        if state["mouth_open"]:
            if mouth_open_start is None:
                mouth_open_start = now
        else:
            mouth_open_start = None

        drowsy = (
            eye_closed_start is not None
            and now - eye_closed_start >= EYE_CLOSED_SECONDS
        )
        yawning = (
            mouth_open_start is not None
            and now - mouth_open_start >= MOUTH_OPEN_SECONDS
        )

        if (drowsy or yawning) and now - last_alert >= alert_cooldown:
            play_alert()
            last_alert = now

        # Display status
        if drowsy:
            status = "DROWSINESS ALERT!"
        elif yawning:
            status = "YAWNING DETECTED!"
        elif state["face_detected"]:
            status = "Driver Attentive"
        else:
            status = "FACE NOT DETECTED"

        cv2.putText(
            frame, status, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255) if (drowsy or yawning) else (0, 255, 0), 2
        )

        cv2.putText(
            frame,
            f"Eyes: {'Closed' if state['eyes_closed'] else 'Open'}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2
        )

        cv2.putText(
            frame,
            f"Mouth: {'Open' if state['mouth_open'] else 'Closed'}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2
        )

        cv2.imshow("Intelligent Driver Monitoring System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
