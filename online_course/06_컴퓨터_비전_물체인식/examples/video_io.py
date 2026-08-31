"""OpenCV로 카메라 영상을 읽고, s 키로 프레임을 저장하는 예제."""
from pathlib import Path
import cv2


def main():
    output = Path("captures")
    output.mkdir(exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("camera open failed")

    index = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            cv2.imshow("camera", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("s"):
                path = output / f"frame_{index:03d}.jpg"
                cv2.imwrite(str(path), frame)
                print("saved:", path)
                index += 1
            elif key == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
