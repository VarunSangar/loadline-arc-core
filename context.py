import cv2
import pytesseract

class VisionContext:
    def capture_text(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cam.release()

        if not ret:
            return ""

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return pytesseract.image_to_string(gray)
