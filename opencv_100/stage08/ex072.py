"""예제 72. 히스토그램 평활화

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import matplotlib.pyplot as plt

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])

    cv2.imshow("Original Gray", gray)
    cv2.imshow("Equalized Gray", equalized)

    plt.figure()
    plt.title("Histogram Comparison")
    plt.plot(hist_original, label="Original")
    plt.plot(hist_equalized, label="Equalized")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
