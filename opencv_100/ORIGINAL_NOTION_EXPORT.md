- OpenCV 100제
    - OpenCV 실습 예제 100제 전체 구성
        
        ## 1단계: OpenCV 기본 입출력과 이미지 구조 이해
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 1 | OpenCV 설치 확인 및 버전 출력 |
        | 2 | 이미지 파일 읽기 |
        | 3 | 이미지 화면 출력 |
        | 4 | 이미지 저장 |
        | 5 | 이미지 크기, 채널, 데이터 타입 확인 |
        | 6 | 컬러 이미지와 흑백 이미지 비교 |
        | 7 | BGR 색상 구조 이해 |
        | 8 | 이미지 픽셀 값 읽기 |
        | 9 | 이미지 픽셀 값 수정 |
        | 10 | 관심 영역 R OI 자르기 |
        
        ## 2단계: 색상 변환과 기본 전처리
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 11 | BGR에서 RGB로 변환 |
        | 12 | BGR에서 Grayscale 변환 |
        | 13 | BGR에서 HSV 변환 |
        | 14 | 특정 색상 영역 검출 |
        | 15 | 이미지 밝기 조절 |
        | 16 | 이미지 대비 조절 |
        | 17 | 이미지 반전 |
        | 18 | Threshold 이진화 |
        | 19 | Adaptive Threshold |
        | 20 | Otsu Threshold |
        
        ## 3단계: 이미지 크기 변환과 기하 변환
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 21 | 이미지 Resize |
        | 22 | 비율 유지 Resize |
        | 23 | 이미지 회전 |
        | 24 | 이미지 이동 |
        | 25 | 이미지 뒤집기 |
        | 26 | Affine Transform |
        | 27 | Perspective Transform |
        | 28 | 이미지 패딩 |
        | 29 | 이미지 피라미드 축소 |
        | 30 | 이미지 피라미드 확대 |
        
        ## 4단계: 필터링과 노이즈 제거
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 31 | 평균 블러 |
        | 32 | Gaussian Blur |
        | 33 | Median Blur |
        | 34 | Bilateral Filter |
        | 35 | Sharpening |
        | 36 | 엣지 보존 필터 |
        | 37 | 노이즈 이미지 생성 |
        | 38 | Salt & Pepper 노이즈 제거 |
        | 39 | 이미지 스무딩 비교 |
        | 40 | 실시간 카메라 블러 처리 |
        
        ## 5단계: Edge, Contour, Shape 분석
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 41 | Sobel Edge |
        | 42 | Laplacian Edge |
        | 43 | Canny Edge |
        | 44 | Contour 검출 |
        | 45 | Contour 면적 계산 |
        | 46 | Bounding Box |
        | 47 | 최소 외접 원 |
        | 48 | 다각형 근사 |
        | 49 | 도형 분류 |
        | 50 | 객체 중심점 계산 |
        
        ## 6단계: 카메라와 비디오 처리
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 51 | 웹캠 열기 |
        | 52 | 실시간 프레임 출력 |
        | 53 | 키보드 입력으로 종료 |
        | 54 | 카메라 해상도 설정 |
        | 55 | FPS 확인 |
        | 56 | 비디오 파일 읽기 |
        | 57 | 비디오 저장 |
        | 58 | 실시간 흑백 변환 |
        | 59 | 실시간 Edge 검출 |
        | 60 | 카메라 프레임 캡처 |
        
        ## 7단계: 객체 추적과 색상 기반 인식
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 61 | HSV 색상 마스크 |
        | 62 | 빨간색 객체 검출 |
        | 63 | 파란색 객체 검출 |
        | 64 | 초록색 객체 검출 |
        | 65 | 마스크 노이즈 제거 |
        | 66 | 객체 중심 추적 |
        | 67 | 실시간 원 검출 |
        | 68 | 색상 객체 Bounding Box |
        | 69 | 여러 객체 추적 |
        | 70 | ROS2 Topic 변환 준비 |
        
        ## 8단계: 특징점, 매칭, 템플릿 매칭
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 71 | 이미지 히스토그램 |
        | 72 | 히스토그램 평활화 |
        | 73 | CLAHE |
        | 74 | Template Matching |
        | 75 | ORB 특징점 검출 |
        | 76 | ORB 특징점 매칭 |
        | 77 | 이미지 유사도 비교 |
        | 78 | Feature Matching 시각화 |
        | 79 | 간단한 물체 인식 |
        | 80 | 로봇 비전에서 특징점 활용 |
        
        ## 9단계: ROS2 연계를 위한 실전 OpenCV
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 81 | cv_bridge 개념 |
        | 82 | ROS2 Image 메시지 이해 |
        | 83 | OpenCV 이미지를 ROS2 메시지로 변환 |
        | 84 | ROS2 Image 메시지를 OpenCV로 변환 |
        | 85 | 카메라 노드 구조 설계 |
        | 86 | 이미지 Subscriber 구조 |
        | 87 | 실시간 Edge Publisher |
        | 88 | 객체 중심 좌표 Publisher |
        | 89 | 로봇 추종용 비전 노드 |
        | 90 | OpenCV + ROS2 디버깅 포인트 |
        
        ## 10단계: 로봇 실무 프로젝트형 예제
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 91 | 라인 트레이싱 전처리 |
        | 92 | 차선 중심 계산 |
        | 93 | ArUco Marker 검출 |
        | 94 | QR 코드 검출 |
        | 95 | 장애물 색상 검출 |
        | 96 | 작업물 위치 검출 |
        | 97 | 컨베이어 객체 카운팅 |
        | 98 | 로봇 팔 Pick 위치 계산 |
        | 99 | OpenCV + YOLO 연계 준비 |
        | 100 | ROS2 비전 프로젝트 통합 구조 |
    - 1단계: OpenCV 기본 입출력과 이미지 구조 이해
        
        # 예제 1. OpenCV 설치 확인 및 버전 출력
        
        ## 핵심 주제
        
        OpenCV가 정상 설치되었는지 확인하고, 현재 사용하는 OpenCV 버전을 출력합니다.
        
        ROS2 Humble에서 카메라 영상을 처리할 때 Python OpenCV를 자주 사용합니다.
        
        따라서 가장 먼저 해야 할 일은 **OpenCV가 제대로 import 되는지 확인하는 것**입니다.
        
        ---
        
        ## 실습 목표
        
        이 예제를 통해 다음을 배웁니다.
        
        ```
        1. cv2 모듈 import 방법
        2. OpenCV 버전 확인 방법
        3. Python 실행 환경 점검 방법
        4. ROS2 비전 노드 작성 전 기본 확인 절차
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        print("OpenCV 설치 확인")
        print("OpenCV 버전:", cv2.__version__)
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. opencv-python을 설치하지 않음
        
        ```
        ModuleNotFoundError: No module named 'cv2'
        ```
        
        이 오류가 나오면 OpenCV가 설치되지 않은 것입니다.
        
        일반 Python 환경에서는 다음과 같이 설치합니다.
        
        ```
        pip install opencv-python
        ```
        
        이미지 표시 기능까지 사용하는 일반 실습 환경에서는 보통 `opencv-python`을 사용합니다.
        
        ---
        
        ### 실수 2. 파일 이름을 cv2.py로 저장함
        
        초보자가 자주 하는 실수입니다.
        
        ```
        cv2.py
        ```
        
        이런 파일명으로 저장하면 Python이 실제 OpenCV 모듈이 아니라 사용자가 만든 `cv2.py` 파일을 먼저 읽을 수 있습니다.
        
        권장 파일명은 다음과 같습니다.
        
        ```
        ex01_check_opencv.py
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서 카메라 영상을 다룰 때 보통 다음 흐름을 사용합니다.
        
        ```
        카메라 센서
        → ROS2 Image 메시지
        → cv_bridge
        → OpenCV 이미지
        → 영상 처리
        → 결과 Publish
        ```
        
        따라서 `cv2`가 정상적으로 동작하지 않으면 ROS2 비전 노드도 제대로 동작하지 않습니다.
        
        ---
        
        # 예제 2. 이미지 파일 읽기
        
        ## 핵심 주제
        
        OpenCV의 `cv2.imread()` 함수를 사용하여 이미지 파일을 읽습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 파일을 Python으로 불러오기
        2. cv2.imread() 사용법 이해
        3. 이미지 경로 오류 확인 방법
        4. 이미지가 None인지 검사하는 습관 익히기
        ```
        
        ---
        
        ## 준비 파일
        
        실습 폴더에 다음과 같은 이미지를 준비합니다.
        
        ```
        practice_images/sample.jpg
        ```
        
        폴더 구조 예시는 다음과 같습니다.
        
        ```
        opencv_practice/
        ├─ ex02_read_image.py
        └─ practice_images/
           └─ sample.jpg
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
            print("파일 경로를 확인하세요:", image_path)
        else:
            print("이미지를 성공적으로 읽었습니다.")
            print("이미지 데이터 타입:", type(image))
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 이미지 경로를 잘못 작성함
        
        예를 들어 이미지가 실제로는 다음 위치에 있는데,
        
        ```
        images/sample.jpg
        ```
        
        코드에는 다음처럼 쓰면 실패합니다.
        
        ```python
        image_path = "practice_images/sample.jpg"
        ```
        
        이 경우 `cv2.imread()`는 오류 메시지를 크게 보여주지 않고 `None`을 반환할 수 있습니다.
        
        ---
        
        ### 실수 2. 한글 경로 또는 공백 경로 문제
        
        Windows 환경에서는 다음과 같은 경로가 문제를 일으키는 경우가 있습니다.
        
        ```
        C:/Users/홍길동/바탕 화면/이미지/sample.jpg
        ```
        
        초보자 실습에서는 가능하면 다음처럼 단순한 영문 경로를 권장합니다.
        
        ```
        C:/opencv_practice/images/sample.jpg
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 노드에서는 실제 이미지 파일 대신 카메라 프레임을 받습니다.
        
        하지만 처리 구조는 비슷합니다.
        
        ```
        이미지 파일 읽기
        → NumPy 배열
        → OpenCV 처리
        ```
        
        ROS2에서는 다음 흐름이 됩니다.
        
        ```
        ROS2 Image 메시지 수신
        → cv_bridge로 변환
        → NumPy 배열
        → OpenCV 처리
        ```
        
        즉, `cv2.imread()`는 ROS2 비전 처리의 가장 기초가 되는 이미지 구조를 이해하는 데 좋습니다.
        
        ---
        
        # 예제 3. 이미지 화면 출력
        
        ## 핵심 주제
        
        `cv2.imshow()`를 사용해 이미지를 화면에 출력합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. OpenCV 창 띄우기
        2. 이미지 화면 출력
        3. 키 입력 대기
        4. 창 닫기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            cv2.imshow("Sample Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. waitKey를 빼먹음
        
        다음처럼 작성하면 창이 나타났다가 바로 사라질 수 있습니다.
        
        ```
        cv2.imshow("Sample Image",image)
        cv2.destroyAllWindows()
        ```
        
        반드시 `cv2.waitKey()`가 필요합니다.
        
        ---
        
        ### 실수 2. 원격 Docker 환경에서 imshow 사용
        
        Docker, WSL2, SSH 환경에서는 GUI 창이 바로 뜨지 않을 수 있습니다.
        
        ROS2 Docker 실습에서는 다음 같은 대안이 필요합니다.
        
        ```
        1. X11 설정
        2. VcXsrv 사용
        3. 이미지 파일로 저장 후 확인
        4. Jupyter Notebook에서는 matplotlib 사용
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서 카메라 영상을 디버깅할 때 가장 쉬운 방법 중 하나가 `cv2.imshow()`입니다.
        
        예를 들어 카메라 Subscriber 노드에서 다음처럼 사용할 수 있습니다.
        
        ```python
        cv2.imshow("camera", frame)
        cv2.waitKey(1)
        ```
        
        실시간 카메라에서는 `waitKey(0)`이 아니라 보통 `waitKey(1)`을 사용합니다.
        
        ---
        
        # 예제 4. 이미지 저장
        
        ## 핵심 주제
        
        `cv2.imwrite()`를 사용하여 이미지를 파일로 저장합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 파일 읽기
        2. 이미지 저장하기
        3. 저장 성공 여부 확인
        4. 결과 이미지 파일 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        save_path = "practice_images/output_sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            result = cv2.imwrite(save_path, image)
        
            if result:
                print("이미지 저장 성공:", save_path)
            else:
                print("이미지 저장 실패")
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 저장 폴더가 존재하지 않음
        
        다음 경로로 저장하려고 할 때,
        
        ```
        save_path = "result/output.jpg"
        ```
        
        `result` 폴더가 없으면 저장에 실패할 수 있습니다.
        
        안전하게 하려면 다음처럼 폴더를 먼저 만들어야 합니다.
        
        ```python
        import os
        
        os.makedirs("result", exist_ok=True)
        ```
        
        ---
        
        ### 실수 2. 확장자를 쓰지 않음
        
        다음 코드는 좋지 않습니다.
        
        ```python
        save_path = "output_sample"
        ```
        
        이미지 저장 시에는 확장자를 명확히 써야 합니다.
        
        ```python
        save_path = "output_sample.jpg"
        ```
        
        또는
        
        ```python
        save_path = "output_sample.png"
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 노드에서 특정 순간의 이미지를 저장하는 기능은 자주 필요합니다.
        
        예를 들어 다음 상황에서 사용합니다.
        
        ```
        1. 장애물 인식 실패 장면 저장
        2. 로봇 주행 중 에러 프레임 저장
        3. 모델 학습용 데이터셋 수집
        4. 실험 결과 이미지 기록
        ```
        
        ---
        
        # 예제 5. 이미지 크기, 채널, 데이터 타입 확인
        
        ## 핵심 주제
        
        OpenCV 이미지의 구조를 확인합니다.
        
        OpenCV 이미지는 NumPy 배열이므로 `shape`, `dtype`, `size`를 확인할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지의 높이 확인
        2. 이미지의 너비 확인
        3. 채널 수 확인
        4. 픽셀 데이터 타입 확인
        5. 전체 픽셀 개수 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            print("이미지 shape:", image.shape)
            print("이미지 dtype:", image.dtype)
            print("이미지 size:", image.size)
        
            height, width, channels = image.shape
        
            print("높이:", height)
            print("너비:", width)
            print("채널 수:", channels)
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. width와 height 순서를 헷갈림
        
        OpenCV 이미지의 `shape` 순서는 다음입니다.
        
        ```
        height, width, channels
        ```
        
        하지만 좌표를 다룰 때는 보통 다음 순서를 씁니다.
        
        ```
        x, y
        ```
        
        즉,
        
        ```
        x는 width 방향
        y는 height 방향
        ```
        
        초보자가 매우 자주 헷갈립니다.
        
        ---
        
        ### 실수 2. 흑백 이미지에서 channels를 꺼내려 함
        
        흑백 이미지는 보통 `shape`가 다음처럼 나옵니다.
        
        ```
        (480, 640)
        ```
        
        즉, 채널 값이 없습니다.
        
        그런데 다음처럼 작성하면 오류가 납니다.
        
        ```python
        height, width, channels = gray.shape
        ```
        
        흑백 이미지는 다음처럼 처리해야 합니다.
        
        ```python
        height, width = gray.shape
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 메시지를 처리할 때도 이미지 크기와 채널 수를 확인해야 합니다.
        
        예를 들어 로봇 카메라에서 들어오는 이미지가 다음과 같을 수 있습니다.
        
        ```
        640 × 480 RGB
        1280 × 720 BGR
        320 × 240 Grayscale
        ```
        
        이미지 크기를 모르면 객체 중심 좌표를 계산하거나 주행 제어로 연결할 때 오류가 발생합니다.
        
        ---
        
        # 예제 6. 컬러 이미지와 흑백 이미지 비교
        
        ## 핵심 주제
        
        같은 이미지를 컬러와 흑백으로 읽고 차이를 비교합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 컬러 이미지 읽기
        2. 흑백 이미지 읽기
        3. shape 차이 확인
        4. 화면에 나란히 출력
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if color_image is None or gray_image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            print("컬러 이미지 shape:", color_image.shape)
            print("흑백 이미지 shape:", gray_image.shape)
        
            cv2.imshow("Color Image", color_image)
            cv2.imshow("Gray Image", gray_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 흑백 이미지를 컬러 이미지처럼 처리함
        
        흑백 이미지는 채널이 없으므로 다음 코드는 오류가 날 수 있습니다.
        
        ```python
        height, width, channels = gray_image.shape
        ```
        
        흑백 이미지는 다음처럼 작성해야 합니다.
        
        ```python
        height, width = gray_image.shape
        ```
        
        ---
        
        ### 실수 2. 흑백 이미지인데 색상 검출을 시도함
        
        HSV 색상 검출은 컬러 이미지에서 해야 합니다.
        
        흑백 이미지에는 색상 정보가 없기 때문에 빨간색, 파란색 같은 색상 검출이 불가능합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 비전에서는 모든 처리를 컬러 이미지로 할 필요가 없습니다.
        
        예를 들어 다음 작업은 흑백 이미지로도 충분합니다.
        
        ```
        1. Edge 검출
        2. Threshold 이진화
        3. 라인 트레이싱
        4. 윤곽선 검출
        ```
        
        흑백 이미지를 사용하면 계산량이 줄어들어 실시간 처리에 유리합니다.
        
        ---
        
        # 예제 7. BGR 색상 구조 이해
        
        ## 핵심 주제
        
        OpenCV는 컬러 이미지를 RGB가 아니라 **BGR 순서**로 다룹니다.
        
        일반적으로 사람은 색을 다음 순서로 생각합니다.
        
        ```
        R: Red
        G: Green
        B: Blue
        ```
        
        하지만 OpenCV는 기본적으로 다음 순서를 사용합니다.
        
        ```
        B: Blue
        G: Green
        R: Red
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. OpenCV의 BGR 구조 이해
        2. 빈 이미지 생성
        3. 파란색, 초록색, 빨간색 이미지 만들기
        4. 색상 채널 순서 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        blue_image = np.zeros((300, 300, 3), dtype=np.uint8)
        green_image = np.zeros((300, 300, 3), dtype=np.uint8)
        red_image = np.zeros((300, 300, 3), dtype=np.uint8)
        
        blue_image[:, :] = (255, 0, 0)
        green_image[:, :] = (0, 255, 0)
        red_image[:, :] = (0, 0, 255)
        
        cv2.imshow("Blue Image", blue_image)
        cv2.imshow("Green Image", green_image)
        cv2.imshow("Red Image", red_image)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. RGB 순서로 색을 넣음
        
        초보자가 빨간색을 만들려고 다음처럼 작성하는 경우가 많습니다.
        
        ```python
        image[:, :] = (255, 0, 0)
        ```
        
        하지만 OpenCV에서는 이것이 빨간색이 아니라 파란색입니다.
        
        빨간색은 다음입니다.
        
        ```python
        image[:, :] = (0, 0, 255)
        ```
        
        ---
        
        ### 실수 2. matplotlib에서 색이 이상하게 나옴
        
        OpenCV 이미지를 matplotlib로 출력하면 색상이 이상하게 보일 수 있습니다.
        
        이유는 다음과 같습니다.
        
        ```
        OpenCV: BGR
        matplotlib: RGB
        ```
        
        그래서 matplotlib로 출력하기 전에는 보통 변환이 필요합니다.
        
        ```
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 메시지에는 encoding 정보가 있습니다.
        
        예를 들어 다음과 같은 encoding이 있을 수 있습니다.
        
        ```
        bgr8
        rgb8
        mono8
        ```
        
        OpenCV는 보통 `bgr8`과 잘 맞습니다.
        
        ROS2에서 이미지 색상이 이상하다면 encoding과 BGR/RGB 변환을 먼저 의심해야 합니다.
        
        ---
        
        # 예제 8. 이미지 픽셀 값 읽기
        
        ## 핵심 주제
        
        이미지에서 특정 좌표의 픽셀 값을 읽습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 좌표 개념 이해
        2. 특정 위치 픽셀 접근
        3. BGR 값 확인
        4. 이미지 좌표와 배열 인덱스 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            y = 100
            x = 150
        
            pixel = image[y, x]
        
            print("좌표 x:", x)
            print("좌표 y:", y)
            print("픽셀 BGR 값:", pixel)
        
            blue = pixel[0]
            green = pixel[1]
            red = pixel[2]
        
            print("Blue:", blue)
            print("Green:", green)
            print("Red:", red)
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. image[x, y]로 접근함
        
        좌표를 생각할 때는 보통 `x, y` 순서이지만, NumPy 배열은 `행, 열` 순서입니다.
        
        따라서 이미지 배열에서는 다음이 맞습니다.
        
        ```python
        image[y, x]
        ```
        
        틀린 예:
        
        ```python
        image[x, y]
        ```
        
        ---
        
        ### 실수 2. 이미지 범위를 벗어난 좌표 접근
        
        이미지 크기가 다음과 같다고 가정합니다.
        
        ```
        height = 480
        width = 640
        ```
        
        가능한 좌표 범위는 다음입니다.
        
        ```
        x: 0 ~ 639
        y: 0 ~ 479
        ```
        
        그런데 다음처럼 접근하면 오류가 날 수 있습니다.
        
        ```python
        pixel = image[500, 700]
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 비전에서 픽셀 값 읽기는 다음 작업의 기본입니다.
        
        ```
        1. 특정 위치의 색상 확인
        2. 라인 트레이싱에서 중앙 픽셀 검사
        3. 카메라 영상의 장애물 색상 확인
        4. 객체 중심점 주변 색상 분석
        ```
        
        예를 들어 라인트레이싱 로봇에서는 화면 아래쪽 중앙 픽셀의 색을 확인하여 주행 방향을 결정할 수 있습니다.
        
        ---
        
        # 예제 9. 이미지 픽셀 값 수정
        
        ## 핵심 주제
        
        이미지의 특정 위치 픽셀 값을 바꾸어 색을 변경합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 픽셀 값 수정 방법 이해
        2. 특정 좌표 색상 변경
        3. 작은 영역 색상 변경
        4. 이미지 배열 슬라이싱 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            image[100, 150] = (0, 0, 255)
        
            image[120:170, 200:250] = (255, 0, 0)
        
            cv2.imshow("Modified Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 원본 이미지가 직접 수정된다는 점을 모름
        
        다음 코드는 `image` 자체를 수정합니다.
        
        ```python
        image[120:170, 200:250] = (255, 0, 0)
        ```
        
        원본을 보존하고 싶다면 복사본을 만들어야 합니다.
        
        ```python
        copy_image = image.copy()
        copy_image[120:170, 200:250] = (255, 0, 0)
        ```
        
        ---
        
        ### 실수 2. 슬라이싱 범위를 x, y 순서로 착각함
        
        다음 코드는 `y범위, x범위`입니다.
        
        ```python
        image[120:170, 200:250]
        ```
        
        즉,
        
        ```
        세로 범위 먼저
        가로 범위 나중
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 영상에서 객체 위치를 표시할 때 픽셀을 수정하거나 도형을 그립니다.
        
        예를 들어 다음 작업과 연결됩니다.
        
        ```
        1. 객체 중심점에 점 찍기
        2. 장애물 영역 표시
        3. 라인 트레이싱 기준선 표시
        4. 로봇 팔 Pick 위치 표시
        ```
        
        실무에서는 픽셀을 직접 수정하기보다는 `cv2.circle()`, `cv2.rectangle()` 같은 함수를 더 많이 사용합니다.
        
        하지만 내부 원리는 결국 픽셀 값을 바꾸는 것입니다.
        
        ---
        
        # 예제 10. 관심 영역 ROI 자르기
        
        ## 핵심 주제
        
        이미지에서 필요한 영역만 잘라내는 ROI 개념을 배웁니다.
        
        ROI는 Region Of Interest의 약자입니다.
        
        ```
        ROI = 관심 영역
        ```
        
        로봇 비전에서는 전체 이미지를 모두 처리하지 않고 필요한 부분만 잘라서 처리하는 경우가 많습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ROI 개념 이해
        2. 이미지 일부 영역 자르기
        3. 잘라낸 영역 화면 출력
        4. 잘라낸 영역 저장
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            roi = image[100:300, 200:500]
        
            cv2.imshow("Original Image", image)
            cv2.imshow("ROI Image", roi)
        
            cv2.imwrite("practice_images/roi_output.jpg", roi)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. ROI 범위가 이미지 크기를 넘어감
        
        이미지 크기가 다음과 같다고 가정합니다.
        
        ```
        height = 480
        width = 640
        ```
        
        이때 다음 코드는 위험합니다.
        
        ```python
        roi = image[400:700, 500:900]
        ```
        
        이미지 범위를 넘어서기 때문입니다.
        
        안전하게 하려면 이미지 크기를 먼저 확인해야 합니다.
        
        ```python
        height, width = image.shape[:2]
        ```
        
        ---
        
        ### 실수 2. ROI가 원본 이미지의 view라는 점을 모름
        
        NumPy 슬라이싱으로 만든 ROI는 원본 이미지와 메모리를 공유할 수 있습니다.
        
        예를 들어 다음처럼 하면,
        
        ```python
        roi = image[100:300, 200:500]
        roi[:, :] = (0, 0, 255)
        ```
        
        원본 이미지의 해당 영역도 빨간색으로 바뀔 수 있습니다.
        
        원본과 독립적으로 사용하려면 다음처럼 복사합니다.
        
        ```python
        roi = image[100:300, 200:500].copy()
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROI는 로봇 비전에서 매우 중요합니다.
        
        예를 들어 자율주행 로봇의 카메라 영상 전체는 다음처럼 보일 수 있습니다.
        
        ```
        상단: 벽, 사람, 조명
        중앙: 장애물
        하단: 바닥, 라인
        ```
        
        라인 트레이싱을 할 때는 전체 이미지가 아니라 아래쪽 영역만 보면 됩니다.
        
        ```python
        roi = frame[height//2:height, :]
        ```
        
        이렇게 하면 계산량이 줄고, 불필요한 영역에 의한 오검출도 줄어듭니다.
        
        ---
        
        # 1단계 핵심 정리
        
        이번 1단계에서는 OpenCV의 가장 기본이 되는 이미지 입출력과 이미지 구조를 다뤘습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 1 | OpenCV 설치 확인 |
        | 2 | 이미지 읽기 |
        | 3 | 이미지 화면 출력 |
        | 4 | 이미지 저장 |
        | 5 | 이미지 크기와 데이터 타입 확인 |
        | 6 | 컬러 이미지와 흑백 이미지 비교 |
        | 7 | BGR 색상 구조 이해 |
        | 8 | 픽셀 값 읽기 |
        | 9 | 픽셀 값 수정 |
        | 10 | ROI 자르기 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```python
        import cv2
        ```
        
        OpenCV 사용 시작입니다.
        
        ```python
        image = cv2.imread("sample.jpg")
        ```
        
        이미지 파일을 읽습니다.
        
        ```python
        cv2.imshow("window", image)
        ```
        
        이미지를 화면에 보여줍니다.
        
        ```python
        cv2.waitKey(0)
        ```
        
        키 입력을 기다립니다.
        
        ```python
        cv2.destroyAllWindows()
        ```
        
        OpenCV 창을 닫습니다.
        
        ```python
        cv2.imwrite("output.jpg", image)
        ```
        
        이미지를 저장합니다.
        
        ```python
        image.shape
        ```
        
        이미지 크기와 채널 정보를 확인합니다.
        
        ```python
        image[y, x]
        ```
        
        특정 픽셀 값을 읽습니다.
        
        ```python
        roi = image[y1:y2, x1:x2]
        ```
        
        이미지 일부 영역을 잘라냅니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        OpenCV를 ROS2에서 바로 활용하려면 다음 흐름을 이해해야 합니다.
        
        ```
        카메라 이미지 수신
        → OpenCV 배열 변환
        → 색상 변환
        → 전처리
        → 객체 검출
        → 중심 좌표 계산
        → ROS2 Topic으로 결과 Publish
        → 로봇 제어 노드에서 사용
        ```
        
        이번 1단계는 이 전체 흐름 중에서 가장 앞부분입니다.
        
        ```
        이미지를 읽고
        이미지 구조를 이해하고
        픽셀과 ROI를 다루는 능력
        ```
        
        이 기초가 있어야 이후에 다음 내용을 안정적으로 배울 수 있습니다.
        
        ```
        색상 검출
        Threshold
        Edge 검출
        Contour 분석
        카메라 프레임 처리
        ROS2 Image 메시지 변환
        ```
        
    - 2단계: 색상 변환과 기본 전처리
        
        이번 단계는 ROS2 Humble 비전 처리에서 매우 중요합니다.
        
        카메라 영상은 보통 컬러 이미지로 들어오지만, 실제 로봇 제어에서는 다음과 같은 전처리가 먼저 필요합니다.
        
        ```
        컬러 영상
        → 색상 공간 변환
        → 밝기/대비 조절
        → 이진화
        → 객체 또는 라인 검출
        → 좌표 계산
        → ROS2 Topic 발행
        ```
        
        ---
        
        # 2단계: 색상 변환과 기본 전처리
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 11 | BGR에서 RGB로 변환 |
        | 12 | BGR에서 Grayscale 변환 |
        | 13 | BGR에서 HSV 변환 |
        | 14 | 특정 색상 영역 검출 |
        | 15 | 이미지 밝기 조절 |
        | 16 | 이미지 대비 조절 |
        | 17 | 이미지 반전 |
        | 18 | Threshold 이진화 |
        | 19 | Adaptive Threshold |
        | 20 | Otsu Threshold |
        
        ---
        
        # 예제 11. BGR에서 RGB로 변환
        
        ## 핵심 주제
        
        OpenCV는 이미지를 기본적으로 **BGR 순서**로 읽습니다.
        
        ```
        OpenCV 기본 색상 순서 = B, G, R
        일반적인 이미지 표시 순서 = R, G, B
        ```
        
        그래서 OpenCV 이미지를 `matplotlib`, 딥러닝 모델, 일부 ROS2 이미지 처리 라이브러리와 함께 사용할 때는 RGB 변환이 필요할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. OpenCV의 BGR 구조 복습
        2. cv2.cvtColor() 사용법 이해
        3. BGR 이미지를 RGB 이미지로 변환
        4. 색상 순서가 바뀌면 결과가 달라지는 이유 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        bgr_image = cv2.imread(image_path)
        
        if bgr_image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        
            cv2.imshow("BGR Image - OpenCV Default", bgr_image)
            cv2.imshow("RGB Image - Converted", rgb_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. matplotlib에 BGR 이미지를 그대로 넣음
        
        다음 코드는 색상이 이상하게 보일 수 있습니다.
        
        ```python
        import matplotlib.pyplot as plt
        
        plt.imshow(bgr_image)
        plt.show()
        ```
        
        matplotlib은 RGB 순서로 이미지를 해석하기 때문입니다.
        
        올바른 방식은 다음과 같습니다.
        
        ```python
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        
        plt.imshow(rgb_image)
        plt.show()
        ```
        
        ---
        
        ### 실수 2. 딥러닝 모델 입력 색상 순서를 확인하지 않음
        
        YOLO, PyTorch 모델, TensorFlow 모델을 사용할 때는 입력 이미지가 BGR인지 RGB인지 반드시 확인해야 합니다.
        
        ```
        OpenCV 카메라 프레임: 보통 BGR
        딥러닝 모델 입력: 보통 RGB인 경우가 많음
        ```
        
        색상 순서가 맞지 않으면 객체 인식 정확도가 떨어질 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 Image 메시지에는 `encoding` 정보가 있습니다.
        
        대표적으로 다음이 있습니다.
        
        ```
        bgr8
        rgb8
        mono8
        ```
        
        OpenCV와 자연스럽게 연결하려면 보통 `bgr8`을 많이 사용합니다.
        
        ```python
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        ```
        
        하지만 딥러닝 모델로 넣기 전에는 RGB 변환이 필요할 수 있습니다.
        
        ---
        
        # 예제 12. BGR에서 Grayscale 변환
        
        ## 핵심 주제
        
        컬러 이미지를 흑백 이미지로 변환합니다.
        
        흑백 이미지는 색상 정보는 없지만 밝기 정보만 남습니다.
        
        로봇 비전에서는 흑백 이미지가 매우 자주 사용됩니다.
        
        ```
        Edge 검출
        Threshold 이진화
        라인 트레이싱
        Contour 검출
        SLAM 전처리
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 컬러 이미지를 흑백으로 변환
        2. Grayscale 이미지 구조 이해
        3. 컬러 이미지와 흑백 이미지의 shape 차이 확인
        4. 전처리에서 흑백 변환이 필요한 이유 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        bgr_image = cv2.imread(image_path)
        
        if bgr_image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        
            print("컬러 이미지 shape:", bgr_image.shape)
            print("흑백 이미지 shape:", gray_image.shape)
        
            cv2.imshow("BGR Image", bgr_image)
            cv2.imshow("Gray Image", gray_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 흑백 이미지에 BGR 색상 처리를 적용함
        
        다음 코드는 흑백 이미지에는 적합하지 않습니다.
        
        ```
        hsv = cv2.cvtColor(gray_image, cv2.COLOR_BGR2HSV)
        ```
        
        흑백 이미지는 BGR 3채널이 아니기 때문입니다.
        
        ---
        
        ### 실수 2. shape를 무조건 3개로 받음
        
        컬러 이미지는 다음처럼 받을 수 있습니다.
        
        ```
        height, width, channels = bgr_image.shape
        ```
        
        하지만 흑백 이미지는 다음처럼 해야 합니다.
        
        ```
        height, width = gray_image.shape
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 영상에서 계산량을 줄이고 싶을 때 Grayscale 변환을 자주 사용합니다.
        
        예를 들어 라인트레이싱에서는 색상보다 밝기 차이가 중요합니다.
        
        ```
        카메라 프레임
        → Grayscale
        → Threshold
        → 라인 영역 검출
        → 중심점 계산
        → /cmd_vel 제어
        ```
        
        ---
        
        # 예제 13. BGR에서 HSV 변환
        
        ## 핵심 주제
        
        BGR 이미지를 HSV 색상 공간으로 변환합니다.
        
        HSV는 색상 검출에서 매우 중요합니다.
        
        ```
        H = Hue        색상
        S = Saturation 채도
        V = Value      밝기
        ```
        
        OpenCV에서 빨간색, 파란색, 초록색 같은 객체를 검출할 때는 BGR보다 HSV가 훨씬 편리합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. HSV 색상 공간 이해
        2. BGR 이미지를 HSV로 변환
        3. H, S, V 채널 의미 이해
        4. 색상 기반 객체 검출 준비
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        bgr_image = cv2.imread(image_path)
        
        if bgr_image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        
            print("BGR 이미지 shape:", bgr_image.shape)
            print("HSV 이미지 shape:", hsv_image.shape)
        
            cv2.imshow("BGR Image", bgr_image)
            cv2.imshow("HSV Image", hsv_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Hue 범위를 0~360으로 생각함
        
        OpenCV에서는 Hue가 다음 범위입니다.
        
        ```
        0 ~ 179
        ```
        
        그래서 빨간색, 파란색, 초록색 범위를 지정할 때 이 점을 반드시 기억해야 합니다.
        
        ---
        
        ### 실수 2. HSV 이미지를 그대로 저장하거나 표시하고 색이 이상하다고 생각함
        
        HSV 이미지는 사람이 직접 보기 위한 이미지라기보다 색상 검출 계산을 위한 이미지입니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 로봇 비전에서 HSV는 다음 작업에 자주 사용됩니다.
        
        ```
        1. 특정 색상의 공 추적
        2. 라인트레이싱용 색상 라인 검출
        3. 컨베이어 위 제품 색상 분류
        4. 표식 Marker 색상 검출
        5. 장애물 색상 기반 인식
        ```
        
        ---
        
        # 예제 14. 특정 색상 영역 검출
        
        ## 핵심 주제
        
        HSV 색상 공간에서 특정 색상 범위를 지정하고, 해당 색상 영역만 검출합니다.
        
        이 예제에서는 **파란색 영역 검출**을 기준으로 설명합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. HSV 색상 범위 지정
        2. cv2.inRange() 사용법 이해
        3. 마스크 이미지 생성
        4. 특정 색상 영역만 추출
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        bgr_image = cv2.imread(image_path)
        
        if bgr_image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        
            lower_blue = np.array([100, 100, 100])
            upper_blue = np.array([130, 255, 255])
        
            mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        
            blue_result = cv2.bitwise_and(bgr_image, bgr_image, mask=mask)
        
            cv2.imshow("Original Image", bgr_image)
            cv2.imshow("Blue Mask", mask)
            cv2.imshow("Blue Area Result", blue_result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 색상 범위를 고정값으로만 믿음
        
        조명 환경에 따라 같은 파란색도 HSV 값이 달라질 수 있습니다.
        
        ```
        밝은 조명
        어두운 조명
        그림자
        카메라 자동 화이트밸런스
        ```
        
        이런 조건에 따라 범위를 조정해야 합니다.
        
        ---
        
        ### 실수 2. BGR에서 직접 색상 범위를 잡음
        
        BGR에서도 색상 범위 검출은 가능하지만 조명 변화에 약합니다.
        
        실무에서는 보통 HSV로 변환한 뒤 색상 범위를 잡습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        색상 기반 객체 검출은 ROS2 입문 로봇 프로젝트에서 매우 자주 사용됩니다.
        
        예를 들어 파란 공을 따라가는 로봇은 다음 구조를 가질 수 있습니다.
        
        ```
        /camera/image_raw
        → OpenCV HSV 변환
        → 파란색 마스크 생성
        → Contour 검출
        → 중심 좌표 계산
        → /target_position Publish
        → 주행 제어 노드에서 /cmd_vel Publish
        ```
        
        ---
        
        # 예제 15. 이미지 밝기 조절
        
        ## 핵심 주제
        
        이미지의 밝기를 조절합니다.
        
        밝기 조절은 전체 픽셀 값에 일정 값을 더하거나 빼는 방식으로 이해할 수 있습니다.
        
        ```
        밝게 만들기: 픽셀 값 증가
        어둡게 만들기: 픽셀 값 감소
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 밝기 개념 이해
        2. cv2.convertScaleAbs() 사용법 이해
        3. 밝은 이미지 만들기
        4. 어두운 이미지 만들기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            bright_image = cv2.convertScaleAbs(image, alpha=1.0, beta=50)
            dark_image = cv2.convertScaleAbs(image, alpha=1.0, beta=-50)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Bright Image", bright_image)
            cv2.imshow("Dark Image", dark_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. NumPy 덧셈으로 직접 밝기 조절
        
        다음 코드는 위험할 수 있습니다.
        
        ```
        bright_image = image + 50
        ```
        
        이미지 픽셀은 보통 `uint8`입니다.
        
        `uint8`은 0~255 범위만 표현합니다.
        
        255를 넘으면 값이 이상하게 순환될 수 있습니다.
        
        예를 들어 250에 50을 더하면 300이 되어야 하지만, `uint8`에서는 이상한 값으로 바뀔 수 있습니다.
        
        그래서 OpenCV의 `convertScaleAbs()`를 사용하는 것이 안전합니다.
        
        ---
        
        ### 실수 2. 밝기와 대비를 혼동함
        
        밝기 조절은 보통 `beta`와 관련이 있습니다.
        
        ```
        beta 증가 → 밝아짐
        beta 감소 → 어두워짐
        ```
        
        대비 조절은 `alpha`와 관련이 있습니다.
        
        ```
        alpha 증가 → 대비 증가
        alpha 감소 → 대비 감소
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 카메라는 실내 조명, 햇빛, 그림자에 영향을 많이 받습니다.
        
        밝기 보정은 다음 작업 전에 사용할 수 있습니다.
        
        ```
        1. 라인 검출
        2. 색상 마스크 생성
        3. Edge 검출
        4. 객체 인식 전처리
        ```
        
        하지만 밝기 조절을 너무 강하게 하면 색상 정보가 왜곡될 수 있으므로 주의해야 합니다.
        
        ---
        
        # 예제 16. 이미지 대비 조절
        
        ## 핵심 주제
        
        이미지의 대비를 조절합니다.
        
        대비는 밝은 부분과 어두운 부분의 차이를 의미합니다.
        
        ```
        대비가 낮음: 전체적으로 흐릿함
        대비가 높음: 밝고 어두운 차이가 뚜렷함
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 대비 개념 이해
        2. alpha 값으로 대비 조절
        3. convertScaleAbs() 재사용
        4. 밝기와 대비 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            low_contrast = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
            high_contrast = cv2.convertScaleAbs(image, alpha=1.8, beta=0)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Low Contrast", low_contrast)
            cv2.imshow("High Contrast", high_contrast)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. alpha 값을 너무 크게 설정
        
        예를 들어 다음처럼 하면 이미지가 과도하게 밝아지고 정보가 사라질 수 있습니다.
        
        ```
        high_contrast = cv2.convertScaleAbs(image, alpha=5.0, beta=0)
        ```
        
        실습에서는 보통 다음 범위에서 시작하는 것이 좋습니다.
        
        ```
        alpha: 0.8 ~ 2.0
        beta: -50 ~ 50
        ```
        
        ---
        
        ### 실수 2. 대비 조절만으로 모든 문제를 해결하려고 함
        
        조명 변화가 심한 환경에서는 단순 대비 조절보다 다음 방법이 더 적합할 수 있습니다.
        
        ```
        HSV 변환
        Histogram Equalization
        CLAHE
        Adaptive Threshold
        카메라 노출 고정
        조명 환경 개선
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 카메라에서 입력 영상이 흐릿하거나 라인과 바닥의 차이가 약할 때 대비 조절을 사용할 수 있습니다.
        
        예를 들어 라인트레이싱에서는 다음 흐름을 사용할 수 있습니다.
        
        ```
        카메라 이미지
        → Grayscale
        → 대비 조절
        → Threshold
        → 라인 검출
        ```
        
        ---
        
        # 예제 17. 이미지 반전
        
        ## 핵심 주제
        
        이미지의 픽셀 값을 반전합니다.
        
        흑백 이미지 기준으로 보면 다음과 같습니다.
        
        ```
        검정 ↔ 흰색
        어두운 부분 ↔ 밝은 부분
        ```
        
        컬러 이미지에서는 각 BGR 채널 값이 모두 반전됩니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 반전 개념 이해
        2. cv2.bitwise_not() 사용법 이해
        3. 컬러 이미지 반전
        4. 흑백 이미지 반전
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            inverted_color = cv2.bitwise_not(image)
            inverted_gray = cv2.bitwise_not(gray_image)
        
            cv2.imshow("Original Color", image)
            cv2.imshow("Inverted Color", inverted_color)
            cv2.imshow("Original Gray", gray_image)
            cv2.imshow("Inverted Gray", inverted_gray)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 반전 후 Threshold 조건을 그대로 사용함
        
        예를 들어 원래는 흰색 라인을 찾고 있었는데 이미지를 반전하면 라인이 검정색이 됩니다.
        
        따라서 Threshold 조건도 바꿔야 합니다.
        
        ---
        
        ### 실수 2. 반전이 꼭 성능 향상을 의미한다고 생각함
        
        반전은 상황에 따라 유용하지만 항상 좋은 것은 아닙니다.
        
        예를 들어 검정 라인을 흰색 배경에서 찾을 때 반전하면 라인이 흰색이 되어 이진화가 쉬워질 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        라인 트레이싱에서 검정색 라인을 추적할 때 반전을 사용하면 처리 흐름이 단순해질 수 있습니다.
        
        ```
        원본 영상
        → Grayscale
        → Threshold
        → 반전
        → 흰색 라인으로 검출
        ```
        
        Contour 검출은 보통 흰색 영역을 객체로 보기 때문에, 검정색 객체를 찾을 때 반전이 유용합니다.
        
        ---
        
        # 예제 18. Threshold 이진화
        
        ## 핵심 주제
        
        Threshold는 이미지를 흰색과 검은색으로 나누는 처리입니다.
        
        ```
        기준값보다 크면 흰색
        기준값보다 작으면 검은색
        ```
        
        이진화는 로봇 비전에서 매우 중요합니다.
        
        ```
        라인 검출
        객체 영역 분리
        마스크 생성
        Contour 검출
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. Threshold 개념 이해
        2. cv2.threshold() 사용법 이해
        3. Grayscale 이미지 이진화
        4. 기준값 변화에 따른 결과 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            threshold_value = 127
        
            ret, binary_image = cv2.threshold(
                gray_image,
                threshold_value,
                255,
                cv2.THRESH_BINARY
            )
        
            print("사용된 Threshold 값:", ret)
        
            cv2.imshow("Gray Image", gray_image)
            cv2.imshow("Binary Image", binary_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 컬러 이미지에 바로 Threshold 적용
        
        Threshold는 보통 Grayscale 이미지에 적용하는 것이 기본입니다.
        
        ```
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ```
        
        ---
        
        ### 실수 2. 기준값을 고정하고 모든 환경에서 사용
        
        조명이 바뀌면 적절한 Threshold 값도 바뀝니다.
        
        실내에서는 127이 적절할 수 있지만, 야외에서는 전혀 맞지 않을 수 있습니다.
        
        이때는 Adaptive Threshold나 Otsu Threshold가 필요합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        라인 트레이싱에서 가장 기본적인 흐름은 다음과 같습니다.
        
        ```
        카메라 프레임
        → Grayscale
        → Threshold
        → 라인 영역 검출
        → 중심 좌표 계산
        → 주행 제어
        ```
        
        Threshold 결과는 이후 Contour 검출의 입력으로 자주 사용됩니다.
        
        ---
        
        # 예제 19. Adaptive Threshold
        
        ## 핵심 주제
        
        Adaptive Threshold는 이미지 전체에 하나의 기준값을 적용하지 않고, 주변 영역을 기준으로 픽셀마다 다른 기준값을 적용합니다.
        
        조명이 고르지 않은 환경에서 유용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 일반 Threshold 한계 이해
        2. Adaptive Threshold 사용법 이해
        3. 조명 변화에 강한 이진화 적용
        4. blockSize와 C 값 의미 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            adaptive_binary = cv2.adaptiveThreshold(
                gray_image,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,
                2
            )
        
            cv2.imshow("Gray Image", gray_image)
            cv2.imshow("Adaptive Threshold", adaptive_binary)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. blockSize를 짝수로 설정
        
        다음 코드는 오류가 날 수 있습니다.
        
        ```
        adaptive_binary = cv2.adaptiveThreshold(
            gray_image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            10,
            2
        )
        ```
        
        `blockSize`는 반드시 홀수여야 합니다.
        
        ---
        
        ### 실수 2. 노이즈가 많은 이미지에 바로 적용
        
        Adaptive Threshold는 주변 영역을 기준으로 계산하므로 노이즈에도 민감할 수 있습니다.
        
        실무에서는 보통 먼저 블러 처리를 합니다.
        
        ```
        gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        ```
        
        그 후 Adaptive Threshold를 적용하면 결과가 더 안정적일 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇이 실내를 이동할 때 조명이 고르지 않은 경우가 많습니다.
        
        ```
        창가 근처는 밝음
        책상 아래는 어두움
        복도는 조명이 일정하지 않음
        ```
        
        이때 일반 Threshold보다 Adaptive Threshold가 라인 검출이나 바닥 패턴 검출에 더 유리할 수 있습니다.
        
        ---
        
        # 예제 20. Otsu Threshold
        
        ## 핵심 주제
        
        Otsu Threshold는 사람이 기준값을 직접 정하지 않고, 이미지의 밝기 분포를 보고 자동으로 적절한 기준값을 찾아주는 방법입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 자동 Threshold 개념 이해
        2. Otsu Threshold 사용법 이해
        3. 일반 Threshold와 차이 이해
        4. ret 값이 실제 자동 기준값이라는 점 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            ret, otsu_binary = cv2.threshold(
                gray_image,
                0,
                255,
                cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
        
            print("Otsu가 자동으로 찾은 Threshold 값:", ret)
        
            cv2.imshow("Gray Image", gray_image)
            cv2.imshow("Otsu Threshold", otsu_binary)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Otsu에 임의 기준값을 의미 있게 넣으려 함
        
        Otsu를 사용할 때는 기준값 자리에 보통 `0`을 넣습니다.
        
        ```
        cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ```
        
        기준값은 Otsu가 자동으로 계산합니다.
        
        ---
        
        ### 실수 2. 조명이 심하게 불균일한 이미지에 Otsu만 사용
        
        Otsu는 이미지 전체의 밝기 분포를 보고 하나의 기준값을 찾습니다.
        
        그래서 조명이 고르지 않은 경우에는 Adaptive Threshold가 더 나을 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Otsu Threshold는 카메라 환경이 비교적 일정하고, 객체와 배경의 밝기 차이가 분명할 때 좋습니다.
        
        예를 들어 다음 상황에 적합합니다.
        
        ```
        1. 흰색 바탕 위 검은색 라인
        2. 검은색 컨베이어 위 밝은 물체
        3. 일정한 조명 아래 부품 윤곽 검출
        ```
        
        ROS2 비전 노드에서는 Threshold 값을 매번 수동 조절하기 어렵기 때문에, Otsu 방식이 초기 프로토타입에 유용합니다.
        
        ---
        
        # 2단계 핵심 정리
        
        이번 2단계에서는 OpenCV 전처리의 핵심을 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 11 | BGR 이미지를 RGB로 변환 |
        | 12 | BGR 이미지를 Grayscale로 변환 |
        | 13 | BGR 이미지를 HSV로 변환 |
        | 14 | HSV 기반 특정 색상 검출 |
        | 15 | 밝기 조절 |
        | 16 | 대비 조절 |
        | 17 | 이미지 반전 |
        | 18 | 일반 Threshold 이진화 |
        | 19 | Adaptive Threshold |
        | 20 | Otsu Threshold |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        ```
        
        BGR 이미지를 RGB로 바꿉니다.
        
        ```
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        ```
        
        컬러 이미지를 흑백으로 바꿉니다.
        
        ```
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        ```
        
        컬러 이미지를 HSV로 바꿉니다.
        
        ```
        mask = cv2.inRange(hsv_image, lower_color, upper_color)
        ```
        
        특정 색상 범위에 해당하는 영역을 마스크로 만듭니다.
        
        ```
        result = cv2.bitwise_and(image, image, mask=mask)
        ```
        
        마스크 영역만 원본 이미지에서 남깁니다.
        
        ```
        bright = cv2.convertScaleAbs(image, alpha=1.0, beta=50)
        ```
        
        이미지를 밝게 만듭니다.
        
        ```
        contrast = cv2.convertScaleAbs(image, alpha=1.8, beta=0)
        ```
        
        이미지 대비를 높입니다.
        
        ```
        inverted = cv2.bitwise_not(image)
        ```
        
        이미지를 반전합니다.
        
        ```
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        ```
        
        일반 이진화를 수행합니다.
        
        ```
        adaptive = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )
        ```
        
        Adaptive Threshold를 수행합니다.
        
        ```
        ret, otsu = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        ```
        
        Otsu Threshold를 수행합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        ROS2에서 카메라 데이터를 처리할 때 가장 흔한 흐름은 다음과 같습니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → OpenCV BGR 이미지
        → Grayscale 또는 HSV 변환
        → Threshold 또는 색상 마스크
        → 객체 영역 검출
        → 중심 좌표 계산
        → ROS2 Topic 발행
        ```
        
        즉, 이번 2단계에서 배운 내용은 다음 로봇 비전 기능의 기반입니다.
        
        ```
        라인 트레이싱
        색상 공 추적
        장애물 색상 검출
        컨베이어 객체 분리
        로봇 팔 Pick 위치 계산
        카메라 기반 주행 보정
        ```
        
        ---
        
        # 실무 기준으로 기억할 점
        
        초보자에게 가장 중요한 판단 기준은 다음입니다.
        
        | 상황 | 추천 처리 |
        | --- | --- |
        | 색상 객체를 찾고 싶다 | HSV 변환 + inRange |
        | 밝고 어두운 차이로 나누고 싶다 | Grayscale + Threshold |
        | 조명이 일정하다 | 일반 Threshold 또는 Otsu |
        | 조명이 불균일하다 | Adaptive Threshold |
        | 색상이 이상하게 보인다 | BGR/RGB 순서 확인 |
        | 검정 객체를 흰색 객체처럼 찾고 싶다 | 반전 처리 |
        | 영상이 너무 어둡다 | beta로 밝기 보정 |
        | 영상이 흐릿하고 차이가 약하다 | alpha로 대비 보정 |
    - 3단계: 이미지 크기 변환과 기하 변환
        
        이번 단계는 ROS2 Humble 로봇 비전에서 매우 중요합니다.
        
        카메라 영상은 항상 원하는 크기, 각도, 위치로 들어오지 않습니다.
        
        예를 들어 실무에서는 다음 상황이 자주 발생합니다.
        
        ```
        카메라 해상도가 너무 큼
        로봇 카메라가 기울어져 있음
        ROI 영역만 확대해서 보고 싶음
        바닥 라인을 위에서 내려다본 것처럼 변환하고 싶음
        모델 입력 크기에 맞게 이미지를 줄여야 함
        ```
        
        그래서 이번 단계에서는 이미지의 **크기, 위치, 방향, 시점**을 다루는 핵심 문법을 학습합니다.
        
        ---
        
        # 3단계: 이미지 크기 변환과 기하 변환
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 21 | 이미지 Resize |
        | 22 | 비율 유지 Resize |
        | 23 | 이미지 회전 |
        | 24 | 이미지 이동 |
        | 25 | 이미지 뒤집기 |
        | 26 | Affine Transform |
        | 27 | Perspective Transform |
        | 28 | 이미지 패딩 |
        | 29 | 이미지 피라미드 축소 |
        | 30 | 이미지 피라미드 확대 |
        
        ---
        
        # 예제 21. 이미지 Resize
        
        ## 핵심 주제
        
        `cv2.resize()`를 사용하여 이미지 크기를 변경합니다.
        
        ROS2 카메라 영상은 해상도가 클 수 있습니다.
        
        예를 들어 1920×1080 이미지를 그대로 처리하면 계산량이 많아집니다.
        
        그래서 실시간 로봇 비전에서는 이미지를 줄여서 처리하는 경우가 많습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.resize() 사용법 이해
        2. 이미지 너비와 높이 변경
        3. 해상도 변경 결과 확인
        4. 실시간 처리에서 Resize가 필요한 이유 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            resized_image = cv2.resize(image, (320, 240))
        
            print("원본 이미지 크기:", image.shape)
            print("변경 이미지 크기:", resized_image.shape)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Resized Image", resized_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. width와 height 순서를 반대로 넣음
        
        다음처럼 쓰면 의도와 다른 크기가 됩니다.
        
        ```
        resized_image = cv2.resize(image, (240, 320))
        ```
        
        이 코드는 너비 240, 높이 320입니다.
        
        OpenCV의 `resize()`는 반드시 다음 순서를 사용합니다.
        
        ```
        cv2.resize(image, (width, height))
        ```
        
        ---
        
        ### 실수 2. 너무 작은 크기로 줄여서 정보 손실
        
        예를 들어 객체가 작은데 이미지를 너무 줄이면 객체가 사라질 수 있습니다.
        
        ```
        원본: 1280×720
        변경: 160×90
        ```
        
        실시간 처리는 빨라지지만 작은 장애물, 라인, 표식 검출 성능이 떨어질 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 노드에서는 해상도 조절이 매우 중요합니다.
        
        ```
        고해상도 이미지
        장점: 정보가 많음
        단점: 처리 속도 느림
        
        저해상도 이미지
        장점: 처리 속도 빠름
        단점: 작은 객체 검출 어려움
        ```
        
        실무에서는 보통 다음처럼 균형을 잡습니다.
        
        ```
        실시간 주행 제어: 320×240 또는 640×480
        정밀 검사: 1280×720 이상
        딥러닝 입력: 모델이 요구하는 크기, 예: 640×640
        ```
        
        ---
        
        # 예제 22. 비율 유지 Resize
        
        ## 핵심 주제
        
        이미지를 줄이거나 키울 때 원본의 가로세로 비율을 유지합니다.
        
        단순히 원하는 크기로 강제 변경하면 이미지가 찌그러질 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 원본 비율 유지 개념 이해
        2. 비율 기반 Resize 구현
        3. width 기준으로 height 자동 계산
        4. 이미지 왜곡 방지
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            original_height, original_width = image.shape[:2]
        
            target_width = 320
            ratio = target_width / original_width
            target_height = int(original_height * ratio)
        
            resized_image = cv2.resize(image, (target_width, target_height))
        
            print("원본 크기:", image.shape)
            print("비율 유지 Resize 크기:", resized_image.shape)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Aspect Ratio Resized Image", resized_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 비율을 유지하지 않고 강제 Resize
        
        다음처럼 하면 이미지가 찌그러질 수 있습니다.
        
        ```
        resized_image = cv2.resize(image, (640, 640))
        ```
        
        원본이 16:9 영상인데 1:1로 바꾸면 사람, 라인, 객체의 형태가 왜곡됩니다.
        
        ---
        
        ### 실수 2. int 변환을 하지 않음
        
        `cv2.resize()`의 크기 값은 정수여야 합니다.
        
        다음처럼 실수 값이 들어가면 오류가 날 수 있습니다.
        
        ```
        target_height = original_height * ratio
        ```
        
        안전하게 다음처럼 작성합니다.
        
        ```
        target_height = int(original_height * ratio)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        딥러닝 모델은 고정 입력 크기를 요구하는 경우가 많습니다.
        
        예를 들어 YOLO 계열 모델은 보통 다음과 같은 입력 크기를 사용합니다.
        
        ```
        640×640
        ```
        
        하지만 카메라 원본이 1280×720이면 비율이 다릅니다.
        
        무작정 640×640으로 바꾸면 객체가 찌그러집니다.
        
        이때는 보통 다음 방법을 사용합니다.
        
        ```
        1. 비율 유지 Resize
        2. 부족한 부분 Padding
        3. 모델 입력 크기 맞춤
        ```
        
        이 방식은 이후 예제 28의 이미지 패딩과 연결됩니다.
        
        ---
        
        # 예제 23. 이미지 회전
        
        ## 핵심 주제
        
        이미지를 원하는 각도로 회전합니다.
        
        로봇 카메라가 약간 기울어져 장착되어 있거나, 이미지를 정렬해야 할 때 사용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 회전 중심점 설정
        2. cv2.getRotationMatrix2D() 이해
        3. cv2.warpAffine() 사용
        4. 이미지 회전 결과 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            height, width = image.shape[:2]
        
            center = (width // 2, height // 2)
            angle = 30
            scale = 1.0
        
            rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        
            rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Rotated Image", rotated_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 회전 후 이미지가 잘림
        
        이미지를 회전하면 모서리 부분이 잘릴 수 있습니다.
        
        이유는 출력 크기를 원본과 동일하게 지정했기 때문입니다.
        
        ```
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        ```
        
        정확히 모든 영역을 보존하려면 회전 후 필요한 출력 크기를 다시 계산해야 합니다.
        
        ---
        
        ### 실수 2. center 좌표 순서를 헷갈림
        
        회전 중심점은 다음 순서입니다.
        
        ```
        center = (x, y)
        ```
        
        이미지 shape는 다음 순서입니다.
        
        ```
        height, width = image.shape[:2]
        ```
        
        따라서 중앙점은 다음처럼 써야 합니다.
        
        ```
        center = (width // 2, height // 2)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 카메라가 실제 장착 과정에서 약간 비뚤어지는 경우가 있습니다.
        
        ```
        카메라가 왼쪽으로 5도 기울어짐
        카메라가 오른쪽으로 10도 기울어짐
        ```
        
        이때 소프트웨어적으로 회전 보정을 할 수 있습니다.
        
        ```
        카메라 프레임
        → 회전 보정
        → 라인 검출
        → 중심 좌표 계산
        ```
        
        하지만 가능하면 하드웨어 장착을 먼저 정확히 맞추는 것이 좋습니다.
        
        소프트웨어 보정은 추가 계산량과 이미지 손실을 만들 수 있습니다.
        
        ---
        
        # 예제 24. 이미지 이동
        
        ## 핵심 주제
        
        이미지를 x축, y축 방향으로 이동합니다.
        
        OpenCV에서는 이동도 Affine 변환의 한 종류입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 이동 개념 이해
        2. Translation Matrix 생성
        3. cv2.warpAffine() 재사용
        4. x, y 방향 이동 결과 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            height, width = image.shape[:2]
        
            move_x = 100
            move_y = 50
        
            translation_matrix = np.float32([
                [1, 0, move_x],
                [0, 1, move_y]
            ])
        
            moved_image = cv2.warpAffine(image, translation_matrix, (width, height))
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Moved Image", moved_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 이동 후 빈 영역이 생기는 것을 오류로 생각함
        
        이미지를 오른쪽이나 아래로 이동하면 왼쪽 또는 위쪽에 빈 영역이 생깁니다.
        
        이것은 정상입니다.
        
        새로 생긴 영역은 기본적으로 검은색으로 채워집니다.
        
        ---
        
        ### 실수 2. y축 방향을 수학 좌표계처럼 생각함
        
        일반 수학 좌표계에서는 y가 위로 증가합니다.
        
        하지만 이미지 좌표계에서는 다음과 같습니다.
        
        ```
        x 증가 → 오른쪽
        y 증가 → 아래쪽
        ```
        
        따라서 `move_y = 50`은 위가 아니라 아래로 이동입니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이미지 이동은 로봇 비전에서 직접 자주 쓰이기보다는, Affine 변환과 Perspective 변환을 이해하기 위한 기초입니다.
        
        하지만 다음 상황에서 사용될 수 있습니다.
        
        ```
        카메라 영상 정렬
        두 이미지 간 위치 보정
        센서 캘리브레이션 전처리
        이미지 증강 데이터 생성
        ```
        
        ---
        
        # 예제 25. 이미지 뒤집기
        
        ## 핵심 주제
        
        `cv2.flip()`을 사용하여 이미지를 좌우, 상하, 또는 상하좌우로 뒤집습니다.
        
        카메라 설치 방향이 반대로 되어 있거나, 웹캠 영상이 거울처럼 보일 때 사용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.flip() 사용법 이해
        2. 좌우 반전
        3. 상하 반전
        4. 상하좌우 반전
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            flip_horizontal = cv2.flip(image, 1)
            flip_vertical = cv2.flip(image, 0)
            flip_both = cv2.flip(image, -1)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Flip Horizontal", flip_horizontal)
            cv2.imshow("Flip Vertical", flip_vertical)
            cv2.imshow("Flip Both", flip_both)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. flipCode 값을 헷갈림
        
        반드시 다음 표를 기억합니다.
        
        | flipCode | 의미 |
        | --- | --- |
        | 1 | 좌우 반전 |
        | 0 | 상하 반전 |
        | -1 | 상하좌우 반전 |
        
        ---
        
        ### 실수 2. 카메라 좌표계와 로봇 좌표계를 혼동함
        
        이미지를 좌우 반전하면 화면에서 객체가 보이는 위치가 달라집니다.
        
        예를 들어 원래 객체가 화면 왼쪽에 있었는데, 좌우 반전 후에는 오른쪽에 보입니다.
        
        로봇 제어에 연결할 때는 다음 관계를 반드시 확인해야 합니다.
        
        ```
        이미지 좌표의 왼쪽/오른쪽
        로봇 기준 좌회전/우회전
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        웹캠이나 USB 카메라를 사용할 때 영상이 거울처럼 보이는 경우가 있습니다.
        
        그럴 때 다음처럼 보정할 수 있습니다.
        
        ```
        frame = cv2.flip(frame, 1)
        ```
        
        하지만 로봇 주행 제어에 사용할 때는 무조건 반전하면 안 됩니다.
        
        화면에서의 좌우와 실제 로봇의 좌우가 바뀌기 때문입니다.
        
        ---
        
        # 예제 26. Affine Transform
        
        ## 핵심 주제
        
        Affine Transform은 이미지의 점 3개를 기준으로 이미지를 변형하는 방법입니다.
        
        Affine 변환으로 할 수 있는 대표 작업은 다음과 같습니다.
        
        ```
        이동
        회전
        확대/축소
        기울이기
        ```
        
        단, 평행한 선은 변환 후에도 평행 관계가 유지됩니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Affine Transform 개념 이해
        2. 원본 점 3개 지정
        3. 변환 후 점 3개 지정
        4. cv2.getAffineTransform() 사용
        5. cv2.warpAffine() 적용
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            height, width = image.shape[:2]
        
            src_points = np.float32([
                [50, 50],
                [200, 50],
                [50, 200]
            ])
        
            dst_points = np.float32([
                [70, 80],
                [220, 50],
                [80, 230]
            ])
        
            affine_matrix = cv2.getAffineTransform(src_points, dst_points)
        
            affine_image = cv2.warpAffine(image, affine_matrix, (width, height))
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Affine Transform", affine_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 점 좌표 개수를 잘못 지정함
        
        Affine Transform은 반드시 원본 점 3개, 결과 점 3개가 필요합니다.
        
        ```
        src_points = np.float32([[x1, y1], [x2, y2], [x3, y3]])
        dst_points = np.float32([[x1, y1], [x2, y2], [x3, y3]])
        ```
        
        점이 2개 또는 4개이면 Affine 변환에 맞지 않습니다.
        
        ---
        
        ### 실수 2. 좌표 타입을 float32로 지정하지 않음
        
        OpenCV 변환 함수는 보통 `np.float32` 좌표를 요구합니다.
        
        다음처럼 작성하는 것이 안전합니다.
        
        ```
        src_points = np.float32([...])
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Affine Transform은 로봇 비전에서 이미지 정렬이나 데이터 증강에 사용할 수 있습니다.
        
        예를 들어 다음 상황입니다.
        
        ```
        카메라가 약간 기울어진 영상 보정
        학습 데이터에서 이미지를 조금씩 변형하여 데이터 증가
        작업물 위치를 정렬해 검사하기
        ```
        
        하지만 바닥을 위에서 내려다보는 것처럼 바꾸는 작업에는 보통 Perspective Transform을 더 많이 사용합니다.
        
        ---
        
        # 예제 27. Perspective Transform
        
        ## 핵심 주제
        
        Perspective Transform은 이미지의 점 4개를 기준으로 시점을 변환하는 방법입니다.
        
        예를 들어 비스듬히 보이는 바닥 이미지를 위에서 내려다본 것처럼 바꿀 수 있습니다.
        
        로봇 비전에서는 다음 작업에 매우 중요합니다.
        
        ```
        차선 검출
        라인 트레이싱
        바닥 좌표 추정
        작업대 위 물체 위치 계산
        Bird's-eye View 변환
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. Perspective Transform 개념 이해
        2. 원본 점 4개 지정
        3. 변환 후 점 4개 지정
        4. cv2.getPerspectiveTransform() 사용
        5. cv2.warpPerspective() 적용
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            src_points = np.float32([
                [100, 100],
                [500, 100],
                [550, 400],
                [50, 400]
            ])
        
            dst_points = np.float32([
                [0, 0],
                [400, 0],
                [400, 300],
                [0, 300]
            ])
        
            perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        
            perspective_image = cv2.warpPerspective(image, perspective_matrix, (400, 300))
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Perspective Transform", perspective_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 점 순서가 뒤섞임
        
        Perspective Transform에서 점 순서가 매우 중요합니다.
        
        예를 들어 원본 점은 다음 순서인데,
        
        ```
        왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래
        ```
        
        결과 점은 다른 순서로 쓰면 이미지가 꼬이거나 뒤집힙니다.
        
        ---
        
        ### 실수 2. 원본 좌표가 이미지 범위를 벗어남
        
        예를 들어 이미지 크기가 640×480인데 다음 좌표를 넣으면 문제가 생깁니다.
        
        ```
        [800, 600]
        ```
        
        항상 이미지 크기를 확인해야 합니다.
        
        ```
        height, width = image.shape[:2]
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Perspective Transform은 ROS2 로봇 주행에서 매우 유용합니다.
        
        예를 들어 카메라가 바닥을 비스듬히 보고 있을 때, 라인은 사다리꼴처럼 보입니다.
        
        ```
        카메라 원본 영상
        → 바닥 영역 4점 선택
        → Perspective Transform
        → 위에서 내려다본 이미지 생성
        → 라인 중심 계산
        → /cmd_vel 제어
        ```
        
        이 방식은 차선 검출, 라인트레이싱, 바닥 마커 검출에서 자주 사용됩니다.
        
        ---
        
        # 예제 28. 이미지 패딩
        
        ## 핵심 주제
        
        이미지 주변에 여백을 추가합니다.
        
        이미지를 모델 입력 크기에 맞추거나, 비율 유지 Resize 후 부족한 영역을 채울 때 사용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 패딩 개념 이해
        2. cv2.copyMakeBorder() 사용법 이해
        3. 검은색 여백 추가
        4. 비율 유지 Resize와 패딩의 관계 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            padded_image = cv2.copyMakeBorder(
                image,
                top=50,
                bottom=50,
                left=100,
                right=100,
                borderType=cv2.BORDER_CONSTANT,
                value=(0, 0, 0)
            )
        
            print("원본 크기:", image.shape)
            print("패딩 후 크기:", padded_image.shape)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Padded Image", padded_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 패딩 색상 순서를 RGB로 넣음
        
        OpenCV는 BGR입니다.
        
        빨간 패딩을 만들고 싶으면 다음처럼 해야 합니다.
        
        ```
        value=(0, 0, 255)
        ```
        
        RGB 기준으로 생각해서 `(255, 0, 0)`을 넣으면 파란색이 됩니다.
        
        ---
        
        ### 실수 2. 패딩 후 좌표계를 보정하지 않음
        
        이미지 왼쪽에 100픽셀 패딩을 추가하면 원본 객체의 x좌표도 100만큼 이동한 것처럼 보입니다.
        
        예를 들어 원본 객체 중심이 다음 좌표였다면,
        
        ```
        x = 200
        y = 150
        ```
        
        왼쪽 100픽셀, 위쪽 50픽셀 패딩 후에는 다음 좌표가 됩니다.
        
        ```
        x = 300
        y = 200
        ```
        
        좌표 기반 로봇 제어에서는 반드시 이 보정을 고려해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        YOLO 같은 딥러닝 모델에서는 입력 크기를 맞추기 위해 비율 유지 Resize + Padding을 자주 사용합니다.
        
        ```
        카메라 원본 1280×720
        → 비율 유지 Resize
        → 640×360
        → 위아래 Padding
        → 640×640
        → 모델 입력
        ```
        
        이런 방식을 흔히 Letterbox 처리라고 부릅니다.
        
        ---
        
        # 예제 29. 이미지 피라미드 축소
        
        ## 핵심 주제
        
        `cv2.pyrDown()`을 사용하여 이미지를 단계적으로 축소합니다.
        
        이미지 피라미드는 같은 이미지를 여러 해상도로 만들어 처리하는 기법입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 피라미드 개념 이해
        2. pyrDown() 사용법 이해
        3. 이미지 해상도 절반 축소
        4. 다중 해상도 처리 개념 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            down1 = cv2.pyrDown(image)
            down2 = cv2.pyrDown(down1)
        
            print("원본 크기:", image.shape)
            print("1단계 축소:", down1.shape)
            print("2단계 축소:", down2.shape)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Pyramid Down 1", down1)
            cv2.imshow("Pyramid Down 2", down2)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. pyrDown이 단순 resize와 완전히 같다고 생각함
        
        `pyrDown()`은 단순히 크기만 줄이는 것이 아니라 내부적으로 블러링과 다운샘플링을 함께 수행합니다.
        
        즉, 이미지 피라미드 처리를 위한 함수입니다.
        
        ---
        
        ### 실수 2. 너무 많이 축소함
        
        이미지를 여러 번 축소하면 작은 객체가 사라집니다.
        
        예를 들어 10픽셀 크기의 작은 물체가 있다면 축소 후에는 거의 보이지 않을 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 비전에서 이미지 피라미드는 다음 상황에 활용됩니다.
        
        ```
        1. 빠른 객체 탐색
        2. 다중 크기 객체 검출
        3. Optical Flow
        4. 특징점 매칭
        5. SLAM 전처리
        ```
        
        고해상도에서 바로 처리하기보다 낮은 해상도에서 후보를 찾고, 필요한 영역만 고해상도로 다시 분석하는 방식도 가능합니다.
        
        ---
        
        # 예제 30. 이미지 피라미드 확대
        
        ## 핵심 주제
        
        `cv2.pyrUp()`을 사용하여 이미지를 단계적으로 확대합니다.
        
        이미지 피라미드에서 축소된 이미지를 다시 키울 때 사용할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. pyrUp() 사용법 이해
        2. 이미지 확대 결과 확인
        3. 축소 후 확대 시 정보 손실 이해
        4. 원본과 복원 이미지 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            down_image = cv2.pyrDown(image)
            up_image = cv2.pyrUp(down_image)
        
            print("원본 크기:", image.shape)
            print("축소 이미지 크기:", down_image.shape)
            print("다시 확대한 이미지 크기:", up_image.shape)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Pyramid Down", down_image)
            cv2.imshow("Pyramid Up After Down", up_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 축소 후 확대하면 원본이 완벽히 복원된다고 생각함
        
        한 번 줄어든 이미지에는 이미 정보 손실이 있습니다.
        
        다시 키워도 원본의 세부 정보는 돌아오지 않습니다.
        
        ```
        원본 이미지
        → 축소
        → 일부 세부 정보 손실
        → 확대
        → 크기는 비슷하지만 디테일은 부족
        ```
        
        ---
        
        ### 실수 2. pyrUp을 고화질 확대 방법으로 오해함
        
        `pyrUp()`은 이미지 피라미드 처리용 확대 함수입니다.
        
        저해상도 이미지를 고해상도처럼 복원하는 슈퍼해상도 기술이 아닙니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서 이미지 피라미드는 직접 주행 제어보다 SLAM, 특징점 추적, 시각적 위치 추정 쪽에서 더 중요합니다.
        
        예를 들어 다음 알고리즘에서 피라미드 개념이 사용됩니다.
        
        ```
        Optical Flow
        Feature Tracking
        Visual Odometry
        Visual SLAM
        ```
        
        로봇이 움직이는 동안 이전 프레임과 현재 프레임의 특징점을 추적할 때, 여러 해상도에서 점진적으로 추적하면 더 안정적입니다.
        
        ---
        
        # 3단계 핵심 정리
        
        이번 3단계에서는 이미지의 크기와 기하 구조를 다루었습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 21 | 이미지 크기 변경 |
        | 22 | 비율 유지 Resize |
        | 23 | 이미지 회전 |
        | 24 | 이미지 이동 |
        | 25 | 이미지 뒤집기 |
        | 26 | Affine Transform |
        | 27 | Perspective Transform |
        | 28 | 이미지 패딩 |
        | 29 | 이미지 피라미드 축소 |
        | 30 | 이미지 피라미드 확대 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        resized = cv2.resize(image, (width, height))
        ```
        
        이미지 크기를 변경합니다.
        
        ```
        height, width = image.shape[:2]
        ```
        
        이미지 높이와 너비를 가져옵니다.
        
        ```
        center = (width // 2, height // 2)
        matrix = cv2.getRotationMatrix2D(center, 30, 1.0)
        rotated = cv2.warpAffine(image, matrix, (width, height))
        ```
        
        이미지를 회전합니다.
        
        ```
        translation_matrix = np.float32([
            [1, 0, move_x],
            [0, 1, move_y]
        ])
        moved = cv2.warpAffine(image, translation_matrix, (width, height))
        ```
        
        이미지를 이동합니다.
        
        ```
        flip_horizontal = cv2.flip(image, 1)
        ```
        
        이미지를 좌우 반전합니다.
        
        ```
        affine_matrix = cv2.getAffineTransform(src_points, dst_points)
        affine_image = cv2.warpAffine(image, affine_matrix, (width, height))
        ```
        
        Affine 변환을 적용합니다.
        
        ```
        perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        perspective_image = cv2.warpPerspective(image, perspective_matrix, (400, 300))
        ```
        
        Perspective 변환을 적용합니다.
        
        ```
        padded = cv2.copyMakeBorder(
            image,
            top=50,
            bottom=50,
            left=100,
            right=100,
            borderType=cv2.BORDER_CONSTANT,
            value=(0, 0, 0)
        )
        ```
        
        이미지에 패딩을 추가합니다.
        
        ```
        down = cv2.pyrDown(image)
        ```
        
        이미지를 피라미드 방식으로 축소합니다.
        
        ```
        up = cv2.pyrUp(image)
        ```
        
        이미지를 피라미드 방식으로 확대합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        ROS2 비전 노드에서는 카메라 영상이 그대로 사용되기보다 대부분 전처리됩니다.
        
        대표 흐름은 다음과 같습니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → OpenCV 이미지
        → Resize
        → ROI 자르기
        → 회전 또는 시점 보정
        → Threshold / HSV / Edge 처리
        → 객체 좌표 계산
        → ROS2 Topic 발행
        ```
        
        이번 단계의 핵심은 다음입니다.
        
        ```
        이미지를 빠르게 처리하기 위해 줄인다.
        카메라 각도 문제를 보정한다.
        로봇이 보기 쉬운 시점으로 변환한다.
        딥러닝 모델 입력 크기에 맞춘다.
        좌표 변환 후 로봇 제어에 연결한다.
        ```
        
        ---
        
        # 실무 기준으로 기억할 점
        
        | 상황 | 추천 처리 |
        | --- | --- |
        | 영상 처리 속도가 느림 | Resize로 해상도 축소 |
        | 이미지가 찌그러짐 | 비율 유지 Resize |
        | 카메라가 기울어짐 | Rotation 보정 |
        | 영상이 거울처럼 보임 | Flip 처리 |
        | 바닥을 위에서 본 것처럼 만들고 싶음 | Perspective Transform |
        | YOLO 입력 크기에 맞추고 싶음 | Resize + Padding |
        | 작은 객체도 보고 싶음 | 너무 많이 축소하지 않기 |
        | SLAM/특징점 추적 준비 | 이미지 피라미드 개념 이해 |
    - 4단계: 필터링과 노이즈 제거
        
        이번 단계는 ROS2 Humble 로봇 비전에서 **카메라 영상 품질을 안정화하는 핵심 전처리**입니다.
        
        실제 로봇 카메라는 항상 깨끗한 영상을 주지 않습니다.
        
        ```
        조명이 흔들림
        카메라 센서 노이즈가 있음
        바닥 반사가 있음
        영상이 거칠게 보임
        Edge 검출 전에 잡음이 많음
        색상 마스크에 작은 점 노이즈가 생김
        ```
        
        그래서 필터링과 노이즈 제거를 알아야 이후 단계의 **Edge, Contour, 객체 추적, ROS2 카메라 노드**를 안정적으로 구현할 수 있습니다.
        
        ---
        
        # 4단계: 필터링과 노이즈 제거
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 31 | 평균 블러 |
        | 32 | Gaussian Blur |
        | 33 | Median Blur |
        | 34 | Bilateral Filter |
        | 35 | Sharpening |
        | 36 | 엣지 보존 필터 |
        | 37 | 노이즈 이미지 생성 |
        | 38 | Salt & Pepper 노이즈 제거 |
        | 39 | 이미지 스무딩 비교 |
        | 40 | 실시간 카메라 블러 처리 |
        
        ---
        
        # 예제 31. 평균 블러
        
        ## 핵심 주제
        
        평균 블러는 주변 픽셀들의 평균값으로 현재 픽셀 값을 바꾸는 가장 기본적인 필터입니다.
        
        쉽게 말하면 이미지의 거친 부분을 부드럽게 만드는 처리입니다.
        
        ```
        주변 픽셀 평균 계산
        → 현재 픽셀 값 대체
        → 이미지가 부드러워짐
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 평균 블러 개념 이해
        2. cv2.blur() 사용법 이해
        3. 커널 크기 의미 이해
        4. 블러가 강해질수록 이미지가 흐려지는 이유 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            blur_3 = cv2.blur(image, (3, 3))
            blur_7 = cv2.blur(image, (7, 7))
            blur_15 = cv2.blur(image, (15, 15))
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Average Blur 3x3", blur_3)
            cv2.imshow("Average Blur 7x7", blur_7)
            cv2.imshow("Average Blur 15x15", blur_15)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 커널 크기를 너무 크게 설정함
        
        예를 들어 다음처럼 하면 이미지가 너무 흐려질 수 있습니다.
        
        ```
        blur = cv2.blur(image, (51, 51))
        ```
        
        객체 경계, 라인, 작은 부품이 사라질 수 있습니다.
        
        ---
        
        ### 실수 2. Edge 검출 전에 무조건 큰 블러 적용
        
        Edge 검출 전에 약한 블러는 노이즈 제거에 도움이 됩니다.
        
        하지만 너무 강한 블러는 Edge 자체를 약하게 만듭니다.
        
        ```
        적당한 블러: 잡음 감소
        과도한 블러: 경계 정보 손실
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 영상에서 평균 블러는 다음 상황에 사용할 수 있습니다.
        
        ```
        1. 영상이 너무 거칠 때
        2. Threshold 전에 작은 밝기 변화 제거
        3. 색상 마스크의 작은 점 노이즈 완화
        4. Edge 검출 전 약한 노이즈 제거
        ```
        
        다만 실시간 로봇 제어에서는 계산량과 정보 손실을 함께 고려해야 합니다.
        
        ---
        
        # 예제 32. Gaussian Blur
        
        ## 핵심 주제
        
        Gaussian Blur는 주변 픽셀을 단순 평균내는 것이 아니라, 중심 픽셀에 가까운 값에 더 큰 가중치를 주는 블러입니다.
        
        평균 블러보다 자연스러운 흐림 효과를 만들며, Edge 검출 전 노이즈 제거에 많이 사용됩니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Gaussian Blur 개념 이해
        2. cv2.GaussianBlur() 사용법 이해
        3. 커널 크기와 sigma 값 이해
        4. Canny Edge 전처리와의 관계 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gaussian_3 = cv2.GaussianBlur(image, (3, 3), 0)
            gaussian_7 = cv2.GaussianBlur(image, (7, 7), 0)
            gaussian_15 = cv2.GaussianBlur(image, (15, 15), 0)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Gaussian Blur 3x3", gaussian_3)
            cv2.imshow("Gaussian Blur 7x7", gaussian_7)
            cv2.imshow("Gaussian Blur 15x15", gaussian_15)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Gaussian 커널 크기를 짝수로 넣음
        
        Gaussian Blur의 커널 크기는 보통 양의 홀수여야 합니다.
        
        올바른 예:
        
        ```
        cv2.GaussianBlur(image, (5, 5), 0)
        ```
        
        잘못된 예:
        
        ```
        cv2.GaussianBlur(image, (4, 4), 0)
        ```
        
        ---
        
        ### 실수 2. 무조건 Gaussian Blur가 평균 블러보다 좋다고 생각함
        
        Gaussian Blur는 자연스럽고 안정적이지만, 모든 상황에서 최고의 선택은 아닙니다.
        
        ```
        일반 노이즈 완화: Gaussian Blur
        Salt & Pepper 노이즈: Median Blur
        Edge 보존 필요: Bilateral Filter
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Canny Edge 검출 전에는 보통 Gaussian Blur를 먼저 적용합니다.
        
        ```
        카메라 프레임
        → Grayscale
        → Gaussian Blur
        → Canny Edge
        → Contour 또는 라인 검출
        ```
        
        노이즈가 많은 상태에서 바로 Canny를 적용하면 작은 점까지 Edge로 검출될 수 있습니다.
        
        ---
        
        # 예제 33. Median Blur
        
        ## 핵심 주제
        
        Median Blur는 주변 픽셀의 평균이 아니라 **중간값**을 사용합니다.
        
        특히 Salt & Pepper 노이즈, 즉 이미지에 검은 점과 흰 점이 튀는 노이즈를 제거할 때 매우 유용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Median Blur 개념 이해
        2. cv2.medianBlur() 사용법 이해
        3. Salt & Pepper 노이즈 제거 원리 이해
        4. 평균 블러와 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            median_3 = cv2.medianBlur(image, 3)
            median_5 = cv2.medianBlur(image, 5)
            median_9 = cv2.medianBlur(image, 9)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Median Blur 3", median_3)
            cv2.imshow("Median Blur 5", median_5)
            cv2.imshow("Median Blur 9", median_9)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 커널 크기를 짝수로 넣음
        
        Median Blur의 커널 크기도 일반적으로 1보다 큰 홀수여야 합니다.
        
        올바른 예:
        
        ```
        median = cv2.medianBlur(image, 5)
        ```
        
        잘못된 예:
        
        ```
        median = cv2.medianBlur(image, 4)
        ```
        
        ---
        
        ### 실수 2. 모든 노이즈에 Median Blur만 사용
        
        Median Blur는 점 형태 노이즈에는 강하지만, 일반적인 흐림 보정이나 자연스러운 스무딩에는 Gaussian Blur가 더 적합할 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        카메라 영상에서 흰 점, 검은 점처럼 튀는 노이즈가 생기면 Median Blur가 효과적입니다.
        
        특히 다음 작업 전처리에 사용할 수 있습니다.
        
        ```
        1. Threshold 이진화
        2. 색상 마스크 생성
        3. Contour 검출
        4. 라인 검출
        ```
        
        ---
        
        # 예제 34. Bilateral Filter
        
        ## 핵심 주제
        
        Bilateral Filter는 이미지를 부드럽게 하면서도 경계선은 최대한 유지하려는 필터입니다.
        
        일반 블러는 노이즈를 줄이지만 객체 경계도 흐리게 만듭니다.
        
        Bilateral Filter는 다음 목적에 사용됩니다.
        
        ```
        노이즈는 줄이고
        객체 경계는 보존한다
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. Bilateral Filter 개념 이해
        2. cv2.bilateralFilter() 사용법 이해
        3. Edge 보존 필터의 필요성 이해
        4. 일반 블러와 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            bilateral = cv2.bilateralFilter(
                image,
                d=9,
                sigmaColor=75,
                sigmaSpace=75
            )
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Bilateral Filter", bilateral)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Bilateral Filter를 실시간 영상에 과도하게 사용
        
        Bilateral Filter는 품질이 좋지만 Gaussian Blur보다 계산량이 큽니다.
        
        실시간 ROS2 카메라 노드에서는 FPS가 떨어질 수 있습니다.
        
        ---
        
        ### 실수 2. sigma 값을 무작정 크게 설정
        
        값을 크게 하면 노이즈는 줄어들 수 있지만, 이미지가 비현실적으로 뭉개질 수 있습니다.
        
        처음에는 다음 정도로 시작하는 것이 좋습니다.
        
        ```
        cv2.bilateralFilter(image, 9, 75, 75)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Bilateral Filter는 객체 경계를 유지해야 하는 작업에서 유용합니다.
        
        ```
        1. 물체 윤곽 검출
        2. 부품 경계선 유지
        3. 사람/장애물 영역 보존
        4. Edge 기반 객체 검출 전처리
        ```
        
        다만 로봇 주행처럼 빠른 반응이 필요한 경우에는 Gaussian Blur가 더 현실적인 선택일 수 있습니다.
        
        ---
        
        # 예제 35. Sharpening
        
        ## 핵심 주제
        
        Sharpening은 이미지를 더 선명하게 만드는 필터입니다.
        
        흐릿한 이미지에서 경계와 세부 정보를 강조할 때 사용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Sharpening 개념 이해
        2. 커널 기반 필터 이해
        3. cv2.filter2D() 사용법 이해
        4. 이미지 선명화 결과 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            sharpening_kernel = np.array([
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ])
        
            sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Sharpened Image", sharpened_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 노이즈가 많은 이미지에 Sharpening을 바로 적용
        
        Sharpening은 경계뿐 아니라 노이즈도 함께 강조할 수 있습니다.
        
        따라서 노이즈가 많은 이미지에는 먼저 약한 블러를 적용하는 것이 좋습니다.
        
        ```
        노이즈 많은 이미지
        → Gaussian Blur
        → Sharpening
        ```
        
        ---
        
        ### 실수 2. 선명화를 과도하게 적용
        
        선명화를 너무 강하게 하면 이미지가 인위적으로 보이고, Edge나 Contour 검출에서 오히려 오류가 늘어날 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Sharpening은 다음 상황에서 제한적으로 사용할 수 있습니다.
        
        ```
        1. 카메라 초점이 약간 흐릴 때
        2. 부품 경계를 더 뚜렷하게 보고 싶을 때
        3. 검사 이미지에서 결함 경계를 강조할 때
        ```
        
        하지만 실시간 주행 제어에서는 노이즈까지 커질 수 있으므로 조심해서 사용해야 합니다.
        
        ---
        
        # 예제 36. 엣지 보존 필터
        
        ## 핵심 주제
        
        엣지 보존 필터는 이미지의 세부 경계를 유지하면서 표면의 노이즈를 줄이는 필터입니다.
        
        OpenCV에서는 `cv2.edgePreservingFilter()`를 사용할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 엣지 보존 필터 개념 이해
        2. cv2.edgePreservingFilter() 사용법 이해
        3. 일반 블러와 차이 이해
        4. 경계를 유지하면서 부드럽게 만드는 효과 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            edge_preserved = cv2.edgePreservingFilter(
                image,
                flags=1,
                sigma_s=60,
                sigma_r=0.4
            )
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Edge Preserving Filter", edge_preserved)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 실시간 처리에 무조건 사용
        
        엣지 보존 필터는 일반 Blur보다 계산량이 클 수 있습니다.
        
        실시간 카메라 노드에서 사용하면 FPS가 떨어질 수 있습니다.
        
        ---
        
        ### 실수 2. 필터 결과가 좋아 보인다고 검출 성능도 좋아진다고 생각함
        
        사람 눈에 보기 좋은 이미지와 알고리즘이 처리하기 좋은 이미지는 다를 수 있습니다.
        
        객체 검출에서는 오히려 단순한 Gaussian Blur + Threshold가 더 안정적일 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        엣지 보존 필터는 로봇 비전에서 다음처럼 사용할 수 있습니다.
        
        ```
        1. 경계가 중요한 물체 검출
        2. 작업물 외곽선 유지
        3. 표면 노이즈 제거
        4. 검사 영상 전처리
        ```
        
        다만 주행 제어보다는 검사, 인식, 시각화 목적에 더 적합합니다.
        
        ---
        
        # 예제 37. 노이즈 이미지 생성
        
        ## 핵심 주제
        
        노이즈 제거를 제대로 배우려면 먼저 노이즈가 있는 이미지를 만들어 볼 필요가 있습니다.
        
        이 예제에서는 원본 이미지에 랜덤 노이즈를 추가합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 이미지 노이즈 개념 이해
        2. NumPy로 랜덤 노이즈 생성
        3. cv2.add() 사용법 이해
        4. 노이즈 추가 이미지 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            noise = np.random.normal(
                loc=0,
                scale=25,
                size=image.shape
            ).astype(np.int16)
        
            noisy_image = image.astype(np.int16) + noise
            noisy_image = np.clip(noisy_image, 0, 255)
            noisy_image = noisy_image.astype(np.uint8)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Noisy Image", noisy_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. uint8 이미지에 바로 음수 노이즈를 더함
        
        `uint8`은 0~255 범위만 표현합니다.
        
        음수나 255 초과 값이 생기면 의도하지 않은 값으로 변할 수 있습니다.
        
        그래서 계산할 때는 `int16` 또는 `float32`로 바꾼 뒤, 마지막에 다시 `uint8`로 변환하는 것이 안전합니다.
        
        ---
        
        ### 실수 2. clip 처리를 하지 않음
        
        노이즈를 더하면 픽셀 값이 범위를 벗어날 수 있습니다.
        
        반드시 다음 처리가 필요합니다.
        
        ```
        np.clip(noisy_image, 0, 255)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        노이즈 이미지는 실제 로봇 실습에서 데이터 증강에 사용할 수 있습니다.
        
        ```
        1. 카메라 노이즈에 강한 알고리즘 테스트
        2. 조명 변화 대응 실험
        3. 딥러닝 학습 데이터 증강
        4. 필터 성능 비교
        ```
        
        실제 로봇 환경은 항상 이상적이지 않기 때문에, 노이즈를 일부러 넣고 알고리즘을 테스트하는 것이 중요합니다.
        
        ---
        
        # 예제 38. Salt & Pepper 노이즈 제거
        
        ## 핵심 주제
        
        Salt & Pepper 노이즈는 이미지에 소금과 후추처럼 흰 점과 검은 점이 튀는 노이즈입니다.
        
        이런 노이즈는 Median Blur로 제거하는 것이 효과적입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Salt & Pepper 노이즈 개념 이해
        2. 흰 점과 검은 점 노이즈 생성
        3. Median Blur로 제거
        4. 제거 전후 비교
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            noisy_image = image.copy()
        
            noise_ratio = 0.02
            height, width = image.shape[:2]
            noise_count = int(height * width * noise_ratio)
        
            for _ in range(noise_count):
                y = np.random.randint(0, height)
                x = np.random.randint(0, width)
        
                if np.random.rand() < 0.5:
                    noisy_image[y, x] = (0, 0, 0)
                else:
                    noisy_image[y, x] = (255, 255, 255)
        
            denoised_image = cv2.medianBlur(noisy_image, 5)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Salt and Pepper Noise", noisy_image)
            cv2.imshow("Denoised by Median Blur", denoised_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 평균 블러로 Salt & Pepper 노이즈를 제거하려 함
        
        평균 블러도 어느 정도 부드럽게 만들지만, 흰 점과 검은 점이 주변으로 퍼질 수 있습니다.
        
        Salt & Pepper 노이즈에는 보통 Median Blur가 더 적합합니다.
        
        ---
        
        ### 실수 2. Median 커널을 너무 크게 설정
        
        커널이 너무 크면 노이즈는 줄지만 이미지의 디테일도 사라집니다.
        
        처음에는 다음 정도부터 시작합니다.
        
        ```
        cv2.medianBlur(image, 3)
        cv2.medianBlur(image, 5)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        실제 카메라 영상에서 센서 이상, 전송 오류, 압축 문제 등으로 점 형태 노이즈가 생길 수 있습니다.
        
        특히 Threshold 이후 마스크에 작은 점들이 많이 생기면 Contour 검출 결과가 불안정해집니다.
        
        ```
        카메라 프레임
        → 색상 마스크
        → 작은 점 노이즈 발생
        → Median Blur 또는 Morphology
        → Contour 검출 안정화
        ```
        
        ---
        
        # 예제 39. 이미지 스무딩 비교
        
        ## 핵심 주제
        
        평균 블러, Gaussian Blur, Median Blur, Bilateral Filter를 한 번에 비교합니다.
        
        필터마다 장단점이 다르므로 상황에 맞게 선택해야 합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 여러 필터 결과 비교
        2. 각 필터의 특징 이해
        3. 노이즈 종류별 적합한 필터 선택
        4. 실무에서 필터 선택 기준 만들기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            average_blur = cv2.blur(image, (7, 7))
            gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
            median_blur = cv2.medianBlur(image, 7)
            bilateral = cv2.bilateralFilter(image, 9, 75, 75)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Average Blur", average_blur)
            cv2.imshow("Gaussian Blur", gaussian_blur)
            cv2.imshow("Median Blur", median_blur)
            cv2.imshow("Bilateral Filter", bilateral)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 필터 선택 기준
        
        | 상황 | 추천 필터 |
        | --- | --- |
        | 가장 단순한 스무딩 | Average Blur |
        | Edge 검출 전 노이즈 완화 | Gaussian Blur |
        | 흰 점/검은 점 노이즈 제거 | Median Blur |
        | 경계를 유지하며 부드럽게 처리 | Bilateral Filter |
        | 실시간 성능 중요 | Gaussian Blur 또는 작은 커널 Average Blur |
        | 품질 중요, 속도 덜 중요 | Bilateral Filter |
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 필터를 많이 적용할수록 좋다고 생각함
        
        필터를 여러 번 적용하면 이미지 정보가 점점 사라질 수 있습니다.
        
        ```
        원본
        → Blur
        → Blur
        → Blur
        → 객체 경계 약화
        → 검출 실패
        ```
        
        필터는 필요한 만큼만 적용해야 합니다.
        
        ---
        
        ### 실수 2. 필터 성능을 눈으로만 판단함
        
        사람 눈에 보기 좋아진 이미지가 알고리즘 성능도 좋아진다는 보장은 없습니다.
        
        다음 기준으로 판단해야 합니다.
        
        ```
        Contour 개수가 안정적인가?
        객체 중심 좌표가 덜 흔들리는가?
        FPS가 충분한가?
        오검출이 줄었는가?
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 비전 노드에서는 필터 선택이 곧 실시간 성능과 연결됩니다.
        
        ```
        필터 강함
        → 노이즈 감소
        → 검출 안정 가능
        → 계산량 증가
        → FPS 감소 가능
        ```
        
        실무에서는 항상 다음 균형을 봐야 합니다.
        
        ```
        정확도 vs 속도
        안정성 vs 지연시간
        화질 vs 제어 반응성
        ```
        
        ---
        
        # 예제 40. 실시간 카메라 블러 처리
        
        ## 핵심 주제
        
        웹캠 영상을 실시간으로 읽고, 각 프레임에 Gaussian Blur를 적용합니다.
        
        ROS2 카메라 노드와 거의 같은 구조를 갖는 실습입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.VideoCapture() 기본 사용법 복습
        2. 실시간 프레임 처리 구조 이해
        3. Gaussian Blur 실시간 적용
        4. q 키로 종료하는 구조 구현
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0)
        
                cv2.imshow("Original Camera", frame)
                cv2.imshow("Blurred Camera", blurred_frame)
        
                key = cv2.waitKey(1)
        
                if key == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. waitKey(0)을 사용함
        
        실시간 영상에서는 다음 코드를 쓰면 안 됩니다.
        
        ```
        cv2.waitKey(0)
        ```
        
        프레임마다 멈춰버립니다.
        
        실시간 영상에서는 보통 다음처럼 씁니다.
        
        ```
        cv2.waitKey(1)
        ```
        
        ---
        
        ### 실수 2. cap.release()를 빼먹음
        
        카메라 사용이 끝나면 반드시 해제해야 합니다.
        
        ```
        cap.release()
        ```
        
        ---
        
        ### 실수 3. Docker/WSL2에서 카메라가 바로 열린다고 생각함
        
        Windows 10/11 + Docker 또는 WSL2 환경에서는 카메라 접근이 일반 Python 실행보다 복잡할 수 있습니다.
        
        실무 교육에서는 다음을 따로 확인해야 합니다.
        
        ```
        Windows 장치 권한
        Docker 장치 매핑
        WSL2 USB 장치 연결
        VcXsrv 또는 GUI 표시 설정
        카메라 번호 0, 1, 2 테스트
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 ROS2 카메라 Subscriber 노드와 매우 비슷합니다.
        
        일반 OpenCV 구조:
        
        ```
        VideoCapture
        → frame 읽기
        → OpenCV 처리
        → imshow
        ```
        
        ROS2 구조:
        
        ```
        /camera/image_raw Subscribe
        → cv_bridge로 frame 변환
        → OpenCV 처리
        → 결과 Publish 또는 imshow
        ```
        
        즉, 이 예제를 이해하면 이후 ROS2에서 다음 노드를 만들 수 있습니다.
        
        ```
        카메라 이미지 Subscriber
        Gaussian Blur 처리
        Edge 검출
        객체 중심 좌표 계산
        처리 결과 이미지 Publisher
        ```
        
        ---
        
        # 4단계 핵심 정리
        
        이번 4단계에서는 필터링과 노이즈 제거를 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 31 | 평균 블러 |
        | 32 | Gaussian Blur |
        | 33 | Median Blur |
        | 34 | Bilateral Filter |
        | 35 | Sharpening |
        | 36 | 엣지 보존 필터 |
        | 37 | 노이즈 이미지 생성 |
        | 38 | Salt & Pepper 노이즈 제거 |
        | 39 | 스무딩 필터 비교 |
        | 40 | 실시간 카메라 블러 처리 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        blur = cv2.blur(image, (7, 7))
        ```
        
        평균 블러입니다.
        
        ```
        gaussian = cv2.GaussianBlur(image, (7, 7), 0)
        ```
        
        Gaussian Blur입니다.
        
        Edge 검출 전처리에 자주 사용합니다.
        
        ```
        median = cv2.medianBlur(image, 5)
        ```
        
        Median Blur입니다.
        
        Salt & Pepper 노이즈 제거에 좋습니다.
        
        ```
        bilateral = cv2.bilateralFilter(image, 9, 75, 75)
        ```
        
        Bilateral Filter입니다.
        
        경계를 유지하면서 노이즈를 줄입니다.
        
        ```
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])
        sharpened = cv2.filter2D(image, -1, kernel)
        ```
        
        이미지 선명화입니다.
        
        ```
        edge_preserved = cv2.edgePreservingFilter(
            image,
            flags=1,
            sigma_s=60,
            sigma_r=0.4
        )
        ```
        
        엣지 보존 필터입니다.
        
        ```
        noisy_image = image.astype(np.int16) + noise
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
        ```
        
        노이즈 이미지를 안전하게 만드는 방식입니다.
        
        ```
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        ```
        
        실시간 카메라 프레임을 읽습니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        ROS2에서 카메라 영상을 처리할 때 필터링은 거의 필수입니다.
        
        대표적인 흐름은 다음과 같습니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → OpenCV frame
        → Resize
        → Grayscale 또는 HSV
        → Blur 또는 Median Filter
        → Threshold / Edge / Contour
        → 객체 좌표 계산
        → ROS2 Topic Publish
        ```
        
        특히 다음 작업에서는 필터링이 매우 중요합니다.
        
        ```
        라인 트레이싱
        장애물 색상 검출
        공 추적
        작업물 외곽선 검출
        로봇 팔 Pick 위치 계산
        Visual SLAM 전처리
        ```
        
        ---
        
        # 실무 기준 필터 선택표
        
        | 상황 | 추천 처리 |
        | --- | --- |
        | 일반적인 영상 노이즈 완화 | Gaussian Blur |
        | 빠르고 단순한 스무딩 | Average Blur |
        | 흰 점/검은 점 노이즈 제거 | Median Blur |
        | 객체 경계를 유지하고 싶음 | Bilateral Filter |
        | 이미지가 약간 흐림 | Sharpening |
        | 보기 좋은 전처리 이미지 필요 | Edge Preserving Filter |
        | 실시간 주행 제어 | 작은 커널 Gaussian Blur |
        | 정밀 검사 이미지 | Bilateral 또는 Edge Preserving 검토 |
        | Threshold 전에 노이즈가 많음 | Gaussian 또는 Median |
        | Contour가 너무 많이 잡힘 | Blur 후 Threshold 또는 Morphology |
        
        ---
        
        # 실무에서 가장 중요한 판단 기준
        
        필터링은 “많이 할수록 좋은 것”이 아닙니다.
        
        로봇 비전에서는 항상 다음 균형을 봐야 합니다.
        
        ```
        노이즈 제거가 충분한가?
        객체 경계가 유지되는가?
        FPS가 충분한가?
        제어 지연이 커지지 않는가?
        검출 좌표가 안정적인가?
        ```
        
        초보자는 처음에 다음 조합부터 실습하는 것이 좋습니다.
        
        ```
        Grayscale
        → Gaussian Blur
        → Threshold
        → Contour
        ```
        
        색상 기반 검출에서는 다음 조합이 좋습니다.
        
        ```
        BGR
        → HSV
        → inRange
        → Median Blur
        → Contour
        ```
        
    - 5단계: Edge, Contour, Shape 분석
        
        이번 단계는 ROS2 Humble 로봇 비전에서 **객체의 외곽선, 위치, 크기, 중심점**을 계산하기 위한 핵심입니다.
        
        실제 로봇에서는 단순히 이미지를 보는 것이 아니라 다음 정보를 뽑아야 합니다.
        
        ```
        객체가 어디에 있는가?
        객체의 크기는 어느 정도인가?
        라인 중심이 화면의 왼쪽인가 오른쪽인가?
        장애물 외곽선은 어디인가?
        로봇 팔이 집어야 할 중심 좌표는 어디인가?
        ```
        
        ---
        
        # 5단계: Edge, Contour, Shape 분석
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 41 | Sobel Edge |
        | 42 | Laplacian Edge |
        | 43 | Canny Edge |
        | 44 | Contour 검출 |
        | 45 | Contour 면적 계산 |
        | 46 | Bounding Box |
        | 47 | 최소 외접 원 |
        | 48 | 다각형 근사 |
        | 49 | 도형 분류 |
        | 50 | 객체 중심점 계산 |
        
        ---
        
        # 예제 41. Sobel Edge
        
        ## 핵심 주제
        
        Sobel Edge는 이미지에서 밝기 변화가 큰 부분을 찾아 Edge를 검출하는 방법입니다.
        
        Edge는 쉽게 말하면 **경계선**입니다.
        
        ```
        밝은 영역과 어두운 영역이 급격히 바뀌는 부분
        색 또는 밝기가 갑자기 변하는 부분
        객체와 배경이 만나는 부분
        ```
        
        Sobel은 특히 x방향, y방향 변화량을 따로 계산할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Sobel Edge 개념 이해
        2. x방향 Edge 검출
        3. y방향 Edge 검출
        4. x/y Edge 합성 결과 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
            sobel_x_abs = cv2.convertScaleAbs(sobel_x)
            sobel_y_abs = cv2.convertScaleAbs(sobel_y)
        
            sobel_combined = cv2.addWeighted(
                sobel_x_abs,
                0.5,
                sobel_y_abs,
                0.5,
                0
            )
        
            cv2.imshow("Gray Image", gray)
            cv2.imshow("Sobel X", sobel_x_abs)
            cv2.imshow("Sobel Y", sobel_y_abs)
            cv2.imshow("Sobel Combined", sobel_combined)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Sobel 결과를 바로 imshow에 넣음
        
        Sobel 결과는 음수나 255를 넘는 값을 포함할 수 있습니다.
        
        그래서 다음 변환이 필요합니다.
        
        ```
        sobel_abs = cv2.convertScaleAbs(sobel)
        ```
        
        ---
        
        ### 실수 2. 노이즈 제거 없이 바로 Edge 검출
        
        노이즈가 많은 이미지에 Sobel을 적용하면 작은 잡음도 Edge로 검출됩니다.
        
        보통 다음 흐름이 안정적입니다.
        
        ```
        Grayscale
        → Gaussian Blur
        → Sobel
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Sobel은 다음 작업에 활용할 수 있습니다.
        
        ```
        1. 라인 방향성 분석
        2. 객체 경계 검출
        3. 바닥 패턴 변화 감지
        4. 차선 후보 검출
        ```
        
        다만 실제 객체 외곽선 추출에는 Canny Edge와 Contour 조합을 더 자주 사용합니다.
        
        ---
        
        # 예제 42. Laplacian Edge
        
        ## 핵심 주제
        
        Laplacian Edge는 x방향과 y방향의 변화량을 한 번에 계산하여 Edge를 검출합니다.
        
        Sobel이 방향별 Edge를 따로 볼 수 있다면, Laplacian은 전체 경계 변화를 한 번에 강조합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Laplacian Edge 개념 이해
        2. Grayscale 변환
        3. Gaussian Blur 후 Edge 검출
        4. 출력 가능한 형태로 변환
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
        
            laplacian_abs = cv2.convertScaleAbs(laplacian)
        
            cv2.imshow("Gray Image", gray)
            cv2.imshow("Blurred Image", blurred)
            cv2.imshow("Laplacian Edge", laplacian_abs)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Blur 없이 Laplacian 적용
        
        Laplacian은 작은 잡음도 강하게 반응할 수 있습니다.
        
        실무에서는 보통 다음 흐름이 좋습니다.
        
        ```
        Grayscale
        → Gaussian Blur
        → Laplacian
        ```
        
        ---
        
        ### 실수 2. Sobel과 Laplacian의 차이를 모름
        
        | 구분 | 특징 |
        | --- | --- |
        | Sobel | x/y 방향 Edge를 따로 볼 수 있음 |
        | Laplacian | 전체 방향의 Edge를 한 번에 강조 |
        | Canny | 실제 실무에서 가장 널리 쓰이는 Edge 검출 |
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Laplacian은 객체 외곽선 강조나 영상 선명도 확인에 사용할 수 있습니다.
        
        예를 들어 카메라 초점이 맞지 않으면 Edge가 약하게 나옵니다.
        
        Laplacian 결과를 이용해 초점 상태를 간단히 평가하는 방식도 가능합니다.
        
        ---
        
        # 예제 43. Canny Edge
        
        ## 핵심 주제
        
        Canny Edge는 OpenCV에서 가장 많이 사용되는 Edge 검출 방법 중 하나입니다.
        
        Canny는 잡음 제거, 밝기 변화 계산, 얇은 Edge 추출, 임계값 처리를 포함한 실용적인 Edge 검출 방식입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Canny Edge 개념 이해
        2. Gaussian Blur 전처리
        3. cv2.Canny() 사용법 이해
        4. threshold1, threshold2 의미 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            edges = cv2.Canny(blurred, 50, 150)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Blurred Gray", blurred)
            cv2.imshow("Canny Edge", edges)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Canny 임계값을 고정값으로만 사용
        
        조명과 카메라 환경에 따라 적절한 임계값은 달라집니다.
        
        ```
        edges = cv2.Canny(blurred, 50, 150)
        ```
        
        이 값은 시작점일 뿐입니다.
        
        실무에서는 다음 값을 실험합니다.
        
        ```
        30, 100
        50, 150
        100, 200
        ```
        
        ---
        
        ### 실수 2. 컬러 이미지에 바로 Canny 적용
        
        Canny는 1채널 이미지에서 사용하는 것이 일반적입니다.
        
        다음 흐름을 권장합니다.
        
        ```
        BGR
        → Grayscale
        → Gaussian Blur
        → Canny
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Canny Edge는 ROS2 로봇 비전에서 다음 작업에 많이 사용됩니다.
        
        ```
        1. 라인 후보 검출
        2. 장애물 외곽선 검출
        3. 작업물 경계 추출
        4. Contour 검출 전처리
        ```
        
        특히 다음 예제의 Contour 검출과 자주 연결됩니다.
        
        ```
        Canny Edge
        → findContours
        → Bounding Box
        → 중심 좌표 계산
        ```
        
        ---
        
        # 예제 44. Contour 검출
        
        ## 핵심 주제
        
        Contour는 이미지에서 같은 값으로 이어진 외곽선입니다.
        
        쉽게 말하면 **객체의 테두리 선**입니다.
        
        Contour를 사용하면 객체의 위치, 크기, 모양, 중심점을 계산할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Contour 개념 이해
        2. Threshold로 이진 이미지 생성
        3. cv2.findContours() 사용법 이해
        4. cv2.drawContours()로 외곽선 그리기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            ret, binary = cv2.threshold(
                gray,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
        
            cv2.drawContours(
                result,
                contours,
                -1,
                (0, 0, 255),
                2
            )
        
            print("검출된 Contour 개수:", len(contours))
        
            cv2.imshow("Binary Image", binary)
            cv2.imshow("Contour Result", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 이진화 없이 Contour 검출
        
        `findContours()`는 일반적으로 이진 이미지에서 사용해야 합니다.
        
        권장 흐름은 다음입니다.
        
        ```
        BGR
        → Grayscale
        → Threshold 또는 Canny
        → findContours
        ```
        
        ---
        
        ### 실수 2. 너무 많은 작은 Contour가 검출됨
        
        노이즈가 많으면 작은 Contour가 많이 생깁니다.
        
        이때는 다음 처리가 필요합니다.
        
        ```
        Blur
        Threshold 조정
        Morphology
        면적 기준 필터링
        ```
        
        면적 기준 필터링은 다음 예제에서 다룹니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Contour는 로봇 비전에서 매우 중요합니다.
        
        ```
        색상 마스크
        → Contour 검출
        → 가장 큰 Contour 선택
        → Bounding Box 계산
        → 중심 좌표 계산
        → ROS2 Topic 발행
        ```
        
        예를 들어 파란 공을 추적하는 로봇은 파란색 마스크에서 Contour를 검출한 뒤 가장 큰 Contour를 목표 객체로 선택합니다.
        
        ---
        
        # 예제 45. Contour 면적 계산
        
        ## 핵심 주제
        
        검출된 Contour의 면적을 계산하고, 너무 작은 노이즈 Contour를 제거합니다.
        
        실무에서는 모든 Contour가 의미 있는 객체가 아닙니다.
        
        작은 점, 그림자, 반사, 노이즈도 Contour로 검출될 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.contourArea() 사용법 이해
        2. Contour 면적 기준 필터링
        3. 작은 노이즈 제거
        4. 의미 있는 객체만 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            ret, binary = cv2.threshold(
                blurred,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
        
            min_area = 500
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    cv2.drawContours(
                        result,
                        [contour],
                        -1,
                        (0, 255, 0),
                        2
                    )
                    print("검출된 객체 면적:", area)
        
            cv2.imshow("Binary Image", binary)
            cv2.imshow("Filtered Contours", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 면적 기준을 상황에 맞게 조정하지 않음
        
        카메라 해상도에 따라 적절한 면적 기준은 달라집니다.
        
        ```
        320×240 영상에서 area 500은 꽤 큰 객체
        1920×1080 영상에서 area 500은 작은 노이즈일 수 있음
        ```
        
        ---
        
        ### 실수 2. 가장 큰 Contour를 무조건 목표 객체로 봄
        
        색상 검출에서는 가장 큰 Contour가 목표일 가능성이 높지만, 항상 그런 것은 아닙니다.
        
        예를 들어 배경에 같은 색의 큰 물체가 있으면 잘못 선택할 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 비전에서는 면적 기준 필터링이 매우 중요합니다.
        
        ```
        색상 마스크
        → Contour 검출
        → 면적이 너무 작은 것 제거
        → 가장 큰 객체 선택
        → 중심 좌표 계산
        ```
        
        이렇게 해야 로봇이 작은 노이즈를 목표로 잘못 추적하지 않습니다.
        
        ---
        
        # 예제 46. Bounding Box
        
        ## 핵심 주제
        
        Bounding Box는 객체를 둘러싸는 사각형입니다.
        
        Contour를 검출한 뒤 Bounding Box를 구하면 객체의 위치와 크기를 쉽게 알 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.boundingRect() 사용법 이해
        2. 객체의 x, y, width, height 계산
        3. cv2.rectangle()로 박스 그리기
        4. 객체 위치 정보 추출
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            ret, binary = cv2.threshold(
                blurred,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
            min_area = 500
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    x, y, w, h = cv2.boundingRect(contour)
        
                    cv2.rectangle(
                        result,
                        (x, y),
                        (x + w, y + h),
                        (255, 0, 0),
                        2
                    )
        
                    print("Bounding Box:", x, y, w, h)
        
            cv2.imshow("Bounding Box Result", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Bounding Box 중심 좌표 계산을 빼먹음
        
        Bounding Box가 있으면 중심 좌표는 다음처럼 계산할 수 있습니다.
        
        ```
        center_x = x + w // 2
        center_y = y + h // 2
        ```
        
        이 중심 좌표가 로봇 제어에 매우 중요합니다.
        
        ---
        
        ### 실수 2. Bounding Box 크기만 보고 실제 객체 크기라고 오해
        
        Bounding Box는 객체를 감싸는 사각형입니다.
        
        객체가 기울어져 있거나 둥글면 실제 객체 면적과 Bounding Box 면적은 다릅니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Bounding Box는 객체 인식 결과를 표현할 때 매우 많이 사용합니다.
        
        ```
        객체 검출
        → Bounding Box
        → 중심 좌표 계산
        → 화면 중앙과 비교
        → 로봇 회전 방향 결정
        ```
        
        예를 들어 객체 중심이 화면 왼쪽에 있으면 로봇이 왼쪽으로 회전하도록 제어할 수 있습니다.
        
        ---
        
        # 예제 47. 최소 외접 원
        
        ## 핵심 주제
        
        최소 외접 원은 Contour를 포함하는 가장 작은 원입니다.
        
        공, 원형 마커, 둥근 부품을 검출할 때 유용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.minEnclosingCircle() 사용법 이해
        2. 객체 중심 좌표 계산
        3. 반지름 계산
        4. 원형 객체 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            ret, binary = cv2.threshold(
                blurred,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
            min_area = 500
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    (x, y), radius = cv2.minEnclosingCircle(contour)
        
                    center = (int(x), int(y))
                    radius = int(radius)
        
                    cv2.circle(
                        result,
                        center,
                        radius,
                        (0, 255, 255),
                        2
                    )
        
                    cv2.circle(
                        result,
                        center,
                        5,
                        (0, 0, 255),
                        -1
                    )
        
                    print("중심:", center, "반지름:", radius)
        
            cv2.imshow("Min Enclosing Circle", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 모든 객체에 원을 적용
        
        최소 외접 원은 원형 객체에 특히 적합합니다.
        
        사각형이나 길쭉한 물체에 적용하면 실제 모양과 맞지 않을 수 있습니다.
        
        ---
        
        ### 실수 2. 반지름이 작은 객체를 노이즈로 제거하지 않음
        
        작은 점도 원으로 검출될 수 있습니다.
        
        면적 또는 반지름 기준으로 필터링하는 것이 좋습니다.
        
        ```
        ifradius>10:
        # 의미 있는 원형 객체로 처리
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        공 추적 로봇에서는 최소 외접 원을 자주 사용합니다.
        
        ```
        색상 마스크
        → Contour 검출
        → 최소 외접 원 계산
        → 중심 좌표와 반지름 발행
        → 로봇이 공을 따라감
        ```
        
        반지름은 객체가 카메라에 얼마나 가까운지 추정하는 데도 사용할 수 있습니다.
        
        ```
        반지름 큼 → 가까움
        반지름 작음 → 멀리 있음
        ```
        
        ---
        
        # 예제 48. 다각형 근사
        
        ## 핵심 주제
        
        다각형 근사는 복잡한 Contour를 단순한 점들의 집합으로 줄이는 방법입니다.
        
        예를 들어 사각형 물체의 외곽선은 많은 점으로 구성될 수 있지만, 다각형 근사를 하면 꼭짓점 4개로 표현할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.arcLength() 사용법 이해
        2. cv2.approxPolyDP() 사용법 이해
        3. 꼭짓점 개수 확인
        4. 단순화된 도형 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            edges = cv2.Canny(blurred, 50, 150)
        
            contours, hierarchy = cv2.findContours(
                edges,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
            min_area = 500
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    perimeter = cv2.arcLength(contour, True)
        
                    approx = cv2.approxPolyDP(
                        contour,
                        0.02 * perimeter,
                        True
                    )
        
                    cv2.drawContours(
                        result,
                        [approx],
                        -1,
                        (0, 255, 0),
                        2
                    )
        
                    print("꼭짓점 개수:", len(approx))
        
            cv2.imshow("Edges", edges)
            cv2.imshow("Polygon Approximation", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 근사 계수를 고정하고 모든 이미지에 사용
        
        ```
        0.02*perimeter
        ```
        
        이 값은 좋은 시작점이지만, 객체 크기나 노이즈에 따라 조정이 필요합니다.
        
        ---
        
        ### 실수 2. 꼭짓점 개수만으로 도형을 무조건 판단
        
        사각형처럼 보이는 물체도 노이즈 때문에 꼭짓점이 5개 이상 나올 수 있습니다.
        
        도형 분류에서는 꼭짓점 개수뿐 아니라 면적, 비율, 원형도 등을 함께 봐야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        다각형 근사는 다음 작업에 유용합니다.
        
        ```
        1. 사각형 마커 검출
        2. 작업물 형태 분류
        3. 박스형 장애물 검출
        4. ArUco/QR 후보 영역 탐색
        ```
        
        ROS2 로봇 팔 프로젝트에서는 작업대 위 사각형 부품 후보를 찾는 데 사용할 수 있습니다.
        
        ---
        
        # 예제 49. 도형 분류
        
        ## 핵심 주제
        
        Contour와 다각형 근사를 이용해 도형을 분류합니다.
        
        이번 예제에서는 단순하게 꼭짓점 개수로 다음 도형을 분류합니다.
        
        ```
        삼각형
        사각형
        원 또는 기타 도형
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. Contour 기반 도형 분류 흐름 이해
        2. 꼭짓점 개수 기반 분류
        3. Bounding Box와 텍스트 표시
        4. cv2.putText() 사용법 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/shapes.png"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            ret, binary = cv2.threshold(
                gray,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
            min_area = 300
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    perimeter = cv2.arcLength(contour, True)
        
                    approx = cv2.approxPolyDP(
                        contour,
                        0.02 * perimeter,
                        True
                    )
        
                    vertices = len(approx)
        
                    if vertices == 3:
                        shape_name = "Triangle"
                    elif vertices == 4:
                        shape_name = "Rectangle"
                    else:
                        shape_name = "Circle or Other"
        
                    x, y, w, h = cv2.boundingRect(approx)
        
                    cv2.drawContours(
                        result,
                        [approx],
                        -1,
                        (0, 255, 0),
                        2
                    )
        
                    cv2.putText(
                        result,
                        shape_name,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2
                    )
        
            cv2.imshow("Binary Image", binary)
            cv2.imshow("Shape Classification", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 준비 파일
        
        이 예제는 여러 도형이 들어 있는 이미지가 있으면 좋습니다.
        
        ```
        practice_images/shapes.png
        ```
        
        예를 들어 흰 배경에 검은색 삼각형, 사각형, 원이 있는 이미지를 사용하면 이해하기 쉽습니다.
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 도형 색과 배경 색을 고려하지 않음
        
        검은 도형이 흰 배경에 있으면 이진화 결과에서 배경이 흰색이 되어 Contour가 이상하게 잡힐 수 있습니다.
        
        이때는 다음을 사용합니다.
        
        ```
        cv2.THRESH_BINARY_INV
        ```
        
        ---
        
        ### 실수 2. 원을 꼭짓점 개수만으로 판단
        
        원도 다각형 근사 결과에 따라 꼭짓점이 8개, 10개, 20개 등으로 나올 수 있습니다.
        
        정확한 원 판단에는 원형도 계산을 추가하는 것이 좋습니다.
        
        ```
        원형도 = 4π × 면적 / 둘레²
        ```
        
        초보 단계에서는 꼭짓점 개수 기반 분류만 익혀도 충분합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        도형 분류는 로봇 비전의 기초 규칙 기반 인식입니다.
        
        ```
        카메라 이미지
        → 이진화
        → Contour
        → 다각형 근사
        → 도형 분류
        → ROS2 메시지로 shape_name 발행
        ```
        
        예를 들어 교육용 로봇 팔이 다음처럼 동작할 수 있습니다.
        
        ```
        삼각형이면 왼쪽 박스에 분류
        사각형이면 오른쪽 박스에 분류
        원형이면 중앙 박스에 분류
        ```
        
        ---
        
        # 예제 50. 객체 중심점 계산
        
        ## 핵심 주제
        
        객체 중심점은 로봇 비전에서 가장 중요한 정보 중 하나입니다.
        
        로봇은 이미지 전체를 이해하는 것이 아니라, 보통 다음 좌표가 필요합니다.
        
        ```
        객체 중심 x좌표
        객체 중심 y좌표
        화면 중앙과 객체 중심의 차이
        ```
        
        이 정보를 이용해 로봇이 왼쪽으로 돌지, 오른쪽으로 돌지, 앞으로 갈지 결정할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.moments() 사용법 이해
        2. Contour 중심점 계산
        3. 중심점 화면 표시
        4. 로봇 제어와 연결되는 오차 계산
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
            ret, binary = cv2.threshold(
                blurred,
                127,
                255,
                cv2.THRESH_BINARY
            )
        
            contours, hierarchy = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
            min_area = 500
        
            height, width = image.shape[:2]
            image_center_x = width // 2
        
            cv2.line(
                result,
                (image_center_x, 0),
                (image_center_x, height),
                (255, 0, 0),
                2
            )
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > min_area:
                    moments = cv2.moments(contour)
        
                    if moments["m00"] != 0:
                        center_x = int(moments["m10"] / moments["m00"])
                        center_y = int(moments["m01"] / moments["m00"])
        
                        error_x = center_x - image_center_x
        
                        cv2.drawContours(
                            result,
                            [contour],
                            -1,
                            (0, 255, 0),
                            2
                        )
        
                        cv2.circle(
                            result,
                            (center_x, center_y),
                            6,
                            (0, 0, 255),
                            -1
                        )
        
                        cv2.putText(
                            result,
                            f"Center: ({center_x}, {center_y})",
                            (center_x + 10, center_y),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 0, 255),
                            2
                        )
        
                        cv2.putText(
                            result,
                            f"Error X: {error_x}",
                            (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 255, 255),
                            2
                        )
        
                        print("객체 중심:", center_x, center_y)
                        print("화면 중앙 대비 x 오차:", error_x)
        
            cv2.imshow("Binary Image", binary)
            cv2.imshow("Object Center", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. moments["m00"] 확인 없이 나눗셈
        
        다음 코드는 위험합니다.
        
        ```
        center_x = int(moments["m10"] / moments["m00"])
        ```
        
        반드시 다음 조건을 확인해야 합니다.
        
        ```
        if moments["m00"] != 0:
        ```
        
        ---
        
        ### 실수 2. 여러 객체가 있을 때 모두 중심을 계산함
        
        목표 객체가 하나라면 보통 가장 큰 Contour만 선택합니다.
        
        ```
        largest_contour = max(contours, key=cv2.contourArea)
        ```
        
        그 후 중심점을 계산하면 더 안정적입니다.
        
        ---
        
        ### 실수 3. 이미지 좌표와 로봇 좌표를 바로 같다고 생각함
        
        이미지 좌표계는 다음과 같습니다.
        
        ```
        x 증가 → 오른쪽
        y 증가 → 아래쪽
        ```
        
        로봇 좌표계는 보통 다음과 다릅니다.
        
        ```
        x축 → 전방
        y축 → 좌우
        z축 → 위
        ```
        
        따라서 이미지 중심 좌표를 로봇 실제 좌표로 바꾸려면 카메라 캘리브레이션과 좌표 변환이 필요합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        객체 중심점 계산은 ROS2 비전 제어의 핵심입니다.
        
        예를 들어 객체 추종 로봇은 다음 흐름을 사용합니다.
        
        ```
        /camera/image_raw
        → OpenCV 처리
        → 객체 중심 center_x 계산
        → 화면 중앙 image_center_x와 비교
        → error_x 계산
        → error_x가 음수면 왼쪽 회전
        → error_x가 양수면 오른쪽 회전
        → /cmd_vel Publish
        ```
        
        간단한 제어 로직은 다음과 같이 생각할 수 있습니다.
        
        ```
        if error_x < -30:
            print("왼쪽으로 회전")
        elif error_x > 30:
            print("오른쪽으로 회전")
        else:
            print("정면으로 이동")
        ```
        
        ---
        
        # 5단계 핵심 정리
        
        이번 5단계에서는 이미지에서 객체의 경계와 모양을 분석하는 핵심 문법을 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 41 | Sobel Edge |
        | 42 | Laplacian Edge |
        | 43 | Canny Edge |
        | 44 | Contour 검출 |
        | 45 | Contour 면적 계산 |
        | 46 | Bounding Box |
        | 47 | 최소 외접 원 |
        | 48 | 다각형 근사 |
        | 49 | 도형 분류 |
        | 50 | 객체 중심점 계산 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ```
        
        Edge와 Contour 전처리를 위해 흑백 이미지로 변환합니다.
        
        ```
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        ```
        
        Edge 검출 전에 노이즈를 줄입니다.
        
        ```
        edges = cv2.Canny(blurred, 50, 150)
        ```
        
        Canny Edge를 검출합니다.
        
        ```
        contours, hierarchy = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        ```
        
        Contour를 검출합니다.
        
        ```
        area = cv2.contourArea(contour)
        ```
        
        Contour 면적을 계산합니다.
        
        ```
        x, y, w, h = cv2.boundingRect(contour)
        ```
        
        Bounding Box를 계산합니다.
        
        ```
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        ```
        
        사각형 박스를 그립니다.
        
        ```
        (x, y), radius = cv2.minEnclosingCircle(contour)
        ```
        
        최소 외접 원을 계산합니다.
        
        ```
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        ```
        
        Contour를 다각형으로 근사합니다.
        
        ```
        moments = cv2.moments(contour)
        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])
        ```
        
        객체 중심점을 계산합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        이번 단계는 OpenCV가 ROS2 로봇 제어로 연결되는 핵심 구간입니다.
        
        ```
        카메라 영상
        → 전처리
        → Edge 또는 Threshold
        → Contour 검출
        → 객체 위치 계산
        → 중심점 계산
        → ROS2 Topic 발행
        → 로봇 제어
        ```
        
        특히 다음 기능을 만들기 위한 기반입니다.
        
        ```
        라인 트레이싱
        색상 공 추적
        장애물 외곽선 검출
        작업물 중심 좌표 계산
        로봇 팔 Pick 위치 추정
        컨베이어 객체 카운팅
        ```
        
        ---
        
        # 실무 기준 처리 흐름 예시
        
        ## 색상 객체 추적
        
        ```
        BGR 이미지
        → HSV 변환
        → inRange 색상 마스크
        → Median Blur
        → Contour 검출
        → 면적 기준 필터링
        → 가장 큰 Contour 선택
        → 중심 좌표 계산
        ```
        
        ## 라인 트레이싱
        
        ```
        BGR 이미지
        → ROI 자르기
        → Grayscale
        → Gaussian Blur
        → Threshold
        → Contour 검출
        → 가장 큰 라인 영역 선택
        → 중심 x좌표 계산
        → 화면 중앙과 비교
        ```
        
        ## 작업물 위치 검출
        
        ```
        카메라 이미지
        → Perspective Transform
        → Threshold 또는 Edge
        → Contour 검출
        → Bounding Box
        → 중심 좌표 계산
        → 로봇 팔 좌표 변환 준비
        ```
        
        ---
        
        # 실무에서 가장 중요한 판단 기준
        
        | 상황 | 추천 처리 |
        | --- | --- |
        | 경계선만 보고 싶음 | Canny Edge |
        | 객체 외곽선을 분석하고 싶음 | Contour |
        | 작은 노이즈가 많음 | 면적 기준 필터링 |
        | 객체 위치와 크기가 필요함 | Bounding Box |
        | 원형 객체를 추적함 | 최소 외접 원 |
        | 도형 종류를 나누고 싶음 | 다각형 근사 |
        | 로봇 제어에 연결하고 싶음 | 중심점 계산 |
        | 화면 중앙 기준 제어가 필요함 | error_x 계산 |
    - 6단계: 카메라와 비디오 처리
        
        이번 단계는 ROS2 Humble 비전 노드로 넘어가기 직전에 반드시 익혀야 하는 부분입니다.
        
        이미지 파일 처리는 정적인 입력이지만, 로봇에서는 대부분 **카메라 영상처럼 계속 들어오는 프레임**을 처리합니다.
        
        ```
        카메라 열기
        → 프레임 반복 읽기
        → OpenCV 처리
        → 화면 출력
        → 필요하면 저장
        → ROS2 Topic으로 연결
        ```
        
        ---
        
        # 6단계: 카메라와 비디오 처리
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 51 | 웹캠 열기 |
        | 52 | 실시간 프레임 출력 |
        | 53 | 키보드 입력으로 종료 |
        | 54 | 카메라 해상도 설정 |
        | 55 | FPS 확인 |
        | 56 | 비디오 파일 읽기 |
        | 57 | 비디오 저장 |
        | 58 | 실시간 흑백 변환 |
        | 59 | 실시간 Edge 검출 |
        | 60 | 카메라 프레임 캡처 |
        
        ---
        
        # 예제 51. 웹캠 열기
        
        ## 핵심 주제
        
        `cv2.VideoCapture()`를 사용하여 웹캠을 엽니다.
        
        OpenCV에서 카메라를 사용할 때 가장 먼저 하는 작업입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.VideoCapture() 사용법 이해
        2. 기본 카메라 번호 이해
        3. 카메라 열기 성공 여부 확인
        4. 카메라 자원 해제 습관 익히기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            print("카메라가 정상적으로 열렸습니다.")
        
        cap.release()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 카메라 번호를 무조건 0으로만 사용
        
        USB 카메라가 여러 개 연결되어 있으면 `0`이 원하는 카메라가 아닐 수 있습니다.
        
        ```
        cap = cv2.VideoCapture(1)
        ```
        
        또는
        
        ```
        cap = cv2.VideoCapture(2)
        ```
        
        로 테스트해야 할 수 있습니다.
        
        ---
        
        ### 실수 2. 카메라 해제를 하지 않음
        
        `cap.release()`를 하지 않으면 다른 프로그램에서 카메라를 사용하지 못하는 경우가 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서는 보통 카메라 드라이버 노드가 카메라를 엽니다.
        
        ```
        일반 OpenCV:
        VideoCapture → frame
        
        ROS2:
        camera driver node → /camera/image_raw
        ```
        
        하지만 ROS2 카메라 노드를 직접 만들 때는 `VideoCapture()` 구조를 이해하고 있어야 합니다.
        
        ---
        
        # 예제 52. 실시간 프레임 출력
        
        ## 핵심 주제
        
        카메라에서 프레임을 반복적으로 읽어 실시간 영상으로 출력합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. while 반복문으로 프레임 계속 읽기
        2. cap.read() 사용법 이해
        3. cv2.imshow()로 실시간 영상 출력
        4. waitKey(1)의 의미 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                cv2.imshow("Camera Frame", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. waitKey를 빼먹음
        
        `imshow()`만 쓰고 `waitKey()`를 빼면 창이 제대로 갱신되지 않을 수 있습니다.
        
        ---
        
        ### 실수 2. 무한 루프 종료 조건이 없음
        
        종료 조건이 없으면 창을 닫아도 프로그램이 계속 실행될 수 있습니다.
        
        ```
        if cv2.waitKey(1) == ord('q'):
            break
        ```
        
        같은 종료 조건이 필요합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 Subscriber 노드에서는 `while True` 대신 콜백 함수가 프레임을 받습니다.
        
        ```
        OpenCV:
        while True:
            cap.read()
        
        ROS2:
        def image_callback(msg):
            frame = bridge.imgmsg_to_cv2(msg)
        ```
        
        즉, 구조는 다르지만 프레임을 받아 처리한다는 핵심은 같습니다.
        
        ---
        
        # 예제 53. 키보드 입력으로 종료
        
        ## 핵심 주제
        
        실시간 영상 처리 프로그램에서 키보드 입력을 받아 종료하거나 기능을 전환합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.waitKey() 반환값 이해
        2. q 키로 종료
        3. s 키로 상태 메시지 출력
        4. 키 입력 기반 제어 구조 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                cv2.imshow("Keyboard Control Camera", frame)
        
                key = cv2.waitKey(1)
        
                if key == ord('q'):
                    print("q 키 입력: 프로그램 종료")
                    break
        
                elif key == ord('s'):
                    print("s 키 입력: 현재 프레임 표시 중")
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. key 값을 저장하지 않고 여러 번 waitKey 호출
        
        다음 방식은 좋지 않습니다.
        
        ```
        if cv2.waitKey(1) == ord('q'):
            break
        
        if cv2.waitKey(1) == ord('s'):
            print("save")
        ```
        
        `waitKey()`를 여러 번 호출하면 키 입력 처리가 꼬일 수 있습니다.
        
        권장 방식은 한 번만 호출하고 변수에 저장하는 것입니다.
        
        ```
        key = cv2.waitKey(1)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 노드에서는 보통 키보드 입력보다 파라미터, 서비스, 토픽으로 상태를 제어합니다.
        
        하지만 OpenCV 실습 단계에서는 키 입력으로 다음 기능을 테스트하기 좋습니다.
        
        ```
        q: 종료
        s: 이미지 저장
        g: Grayscale 모드
        e: Edge 모드
        ```
        
        ---
        
        # 예제 54. 카메라 해상도 설정
        
        ## 핵심 주제
        
        카메라 입력 해상도를 설정합니다.
        
        실시간 로봇 비전에서는 해상도가 매우 중요합니다.
        
        ```
        해상도 높음 → 정보 많음, 처리 느림
        해상도 낮음 → 정보 적음, 처리 빠름
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. cap.set() 사용법 이해
        2. 프레임 너비 설정
        3. 프레임 높이 설정
        4. 실제 적용된 해상도 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
            actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
            print("설정된 카메라 너비:", actual_width)
            print("설정된 카메라 높이:", actual_height)
        
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                cv2.imshow("Resolution Camera", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 설정한 해상도가 반드시 적용된다고 생각함
        
        카메라가 지원하지 않는 해상도는 적용되지 않을 수 있습니다.
        
        그래서 반드시 `cap.get()`으로 확인해야 합니다.
        
        ---
        
        ### 실수 2. 고해상도만 선호함
        
        로봇 주행 제어에서는 1920×1080보다 640×480 또는 320×240이 더 적합할 수 있습니다.
        
        중요한 것은 화질이 아니라 **제어에 필요한 정보를 충분히 빠르게 얻는 것**입니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 드라이버에서도 해상도는 파라미터로 설정하는 경우가 많습니다.
        
        ```
        width: 640
        height: 480
        fps: 30
        ```
        
        OpenCV에서 해상도와 처리 속도의 관계를 이해하면 ROS2 카메라 파라미터 튜닝도 쉬워집니다.
        
        ---
        
        # 예제 55. FPS 확인
        
        ## 핵심 주제
        
        카메라 영상 처리 속도인 FPS를 확인합니다.
        
        FPS는 Frames Per Second의 약자입니다.
        
        ```
        FPS = 1초에 처리하는 프레임 수
        ```
        
        로봇 비전에서는 FPS가 낮으면 제어 반응이 늦어집니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. time 모듈로 처리 시간 측정
        2. FPS 계산
        3. 화면에 FPS 표시
        4. 처리량과 실시간성 관계 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import time
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            prev_time = time.time()
        
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                current_time = time.time()
                elapsed_time = current_time - prev_time
                prev_time = current_time
        
                if elapsed_time > 0:
                    fps = 1.0 / elapsed_time
                else:
                    fps = 0
        
                cv2.putText(
                    frame,
                    f"FPS: {fps:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 255, 0),
                    2
                )
        
                cv2.imshow("FPS Camera", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. FPS만 높으면 좋다고 생각함
        
        FPS가 높아도 검출 정확도가 낮으면 의미가 없습니다.
        
        실무에서는 다음 균형이 중요합니다.
        
        ```
        FPS
        정확도
        지연시간
        CPU/GPU 사용량
        제어 안정성
        ```
        
        ---
        
        ### 실수 2. FPS 계산 위치가 잘못됨
        
        영상 처리 전후 어디에서 시간을 재는지에 따라 FPS가 달라집니다.
        
        실제 처리 성능을 보려면 전처리, 검출, 표시까지 포함한 전체 루프 시간을 재는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 비전 노드에서는 FPS가 곧 메시지 발행 주기와 연결됩니다.
        
        ```
        30 FPS → 약 33ms마다 한 프레임
        10 FPS → 약 100ms마다 한 프레임
        5 FPS  → 약 200ms마다 한 프레임
        ```
        
        로봇 주행 제어에서는 너무 낮은 FPS가 흔들림이나 반응 지연으로 이어질 수 있습니다.
        
        ---
        
        # 예제 56. 비디오 파일 읽기
        
        ## 핵심 주제
        
        웹캠 대신 저장된 비디오 파일을 읽어 프레임 단위로 처리합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. VideoCapture로 비디오 파일 열기
        2. 프레임 반복 읽기
        3. 비디오 끝 처리
        4. 파일 기반 영상 분석 구조 이해
        ```
        
        ---
        
        ## 준비 파일
        
        다음 경로에 실습용 영상을 준비합니다.
        
        ```
        practice_videos/sample.mp4
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        video_path = "practice_videos/sample.mp4"
        
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("비디오 파일을 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("비디오가 끝났거나 프레임을 읽을 수 없습니다.")
                    break
        
                cv2.imshow("Video File", frame)
        
                if cv2.waitKey(30) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 영상 파일 경로 오류
        
        이미지와 마찬가지로 비디오도 경로가 틀리면 열리지 않습니다.
        
        가능하면 영문 경로를 권장합니다.
        
        ```
        C:/opencv_practice/practice_videos/sample.mp4
        ```
        
        ---
        
        ### 실수 2. 코덱 문제를 코드 오류로 착각함
        
        특정 mp4 파일이 OpenCV에서 열리지 않을 수 있습니다.
        
        이 경우 다른 mp4 파일로 테스트하거나 코덱을 변환해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        비디오 파일 읽기는 ROS2 카메라 없이 알고리즘을 테스트할 때 유용합니다.
        
        ```
        저장된 주행 영상
        → OpenCV로 프레임 읽기
        → 라인 검출 알고리즘 테스트
        → 안정화 후 ROS2 카메라 노드에 적용
        ```
        
        실제 로봇 없이도 영상 기반 알고리즘을 반복 테스트할 수 있습니다.
        
        ---
        
        # 예제 57. 비디오 저장
        
        ## 핵심 주제
        
        카메라 또는 비디오 프레임을 처리한 뒤 결과를 새 비디오 파일로 저장합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.VideoWriter() 사용법 이해
        2. 코덱 설정
        3. 영상 크기와 FPS 설정
        4. 처리 결과 영상 저장
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = 20.0
        
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        
            out = cv2.VideoWriter(
                "output_camera.mp4",
                fourcc,
                fps,
                (width, height)
            )
        
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                out.write(frame)
        
                cv2.imshow("Recording Camera", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 저장 프레임 크기와 실제 프레임 크기가 다름
        
        `VideoWriter`에 설정한 크기와 실제 `frame` 크기가 다르면 저장이 제대로 안 될 수 있습니다.
        
        ---
        
        ### 실수 2. out.release()를 빼먹음
        
        비디오 저장 후 반드시 호출해야 합니다.
        
        ```
        out.release()
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 로봇 실험에서는 결과 영상을 저장하는 기능이 매우 유용합니다.
        
        ```
        주행 실험 기록
        객체 검출 실패 장면 분석
        알고리즘 개선 전후 비교
        학습 데이터 수집
        ```
        
        ROS2에서는 rosbag으로 토픽을 저장할 수도 있지만, OpenCV로 처리 결과 영상을 저장하면 시각적으로 바로 확인하기 좋습니다.
        
        ---
        
        # 예제 58. 실시간 흑백 변환
        
        ## 핵심 주제
        
        카메라 프레임을 실시간으로 Grayscale 이미지로 변환합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 실시간 프레임 처리 구조 복습
        2. cv2.cvtColor() 실시간 적용
        3. 컬러 영상과 흑백 영상 동시 출력
        4. ROS2 비전 전처리 흐름 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
                cv2.imshow("Original Camera", frame)
                cv2.imshow("Gray Camera", gray)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 흑백 이미지에 색상 검출을 하려고 함
        
        흑백 이미지에는 색상 정보가 없습니다.
        
        색상 검출은 HSV 변환을 사용해야 합니다.
        
        ---
        
        ### 실수 2. 흑백 변환 후 shape를 3개로 받음
        
        흑백 이미지는 보통 2차원입니다.
        
        ```
        height, width = gray.shape
        ```
        
        컬러 이미지처럼 다음을 쓰면 오류가 날 수 있습니다.
        
        ```
        height, width, channels = gray.shape
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 Subscriber에서 가장 흔한 전처리 중 하나가 흑백 변환입니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → BGR frame
        → Grayscale
        → Threshold / Edge
        ```
        
        라인 트레이싱, Edge 검출, Contour 분석의 시작점입니다.
        
        ---
        
        # 예제 59. 실시간 Edge 검출
        
        ## 핵심 주제
        
        카메라 프레임에 실시간으로 Canny Edge를 적용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 실시간 Grayscale 변환
        2. 실시간 Gaussian Blur
        3. 실시간 Canny Edge 검출
        4. Edge 결과 화면 출력
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
                edges = cv2.Canny(blurred, 50, 150)
        
                cv2.imshow("Original Camera", frame)
                cv2.imshow("Canny Edge Camera", edges)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Canny 임계값을 상황에 맞게 조정하지 않음
        
        조명이 어두우면 Edge가 적게 나오고, 노이즈가 많으면 Edge가 너무 많이 나올 수 있습니다.
        
        다음 값들을 실험해 봅니다.
        
        ```
        edges = cv2.Canny(blurred, 30, 100)
        edges = cv2.Canny(blurred, 50, 150)
        edges = cv2.Canny(blurred, 100, 200)
        ```
        
        ---
        
        ### 실수 2. 실시간 처리 속도 확인을 하지 않음
        
        Edge 처리를 넣으면 FPS가 떨어질 수 있습니다.
        
        실무에서는 예제 55의 FPS 표시와 함께 사용해 성능을 확인하는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 비전 노드에서 Edge 결과를 별도 이미지 토픽으로 발행할 수 있습니다.
        
        ```
        /camera/image_raw
        → OpenCV Canny 처리
        → /camera/edge_image Publish
        ```
        
        RViz2나 rqt_image_view에서 처리 결과를 확인하면 디버깅이 쉬워집니다.
        
        ---
        
        # 예제 60. 카메라 프레임 캡처
        
        ## 핵심 주제
        
        실시간 카메라 영상에서 특정 키를 눌렀을 때 현재 프레임을 이미지 파일로 저장합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 실시간 프레임 저장
        2. s 키로 캡처
        3. 파일 이름 자동 증가
        4. 데이터셋 수집 기초 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import os
        
        save_dir = "captured_images"
        os.makedirs(save_dir, exist_ok=True)
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            count = 0
        
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                cv2.imshow("Capture Camera", frame)
        
                key = cv2.waitKey(1)
        
                if key == ord('s'):
                    file_path = os.path.join(save_dir, f"capture_{count:04d}.jpg")
                    cv2.imwrite(file_path, frame)
                    print("이미지 저장:", file_path)
                    count += 1
        
                elif key == ord('q'):
                    print("프로그램 종료")
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 저장 폴더를 만들지 않음
        
        저장 경로의 폴더가 없으면 `cv2.imwrite()`가 실패할 수 있습니다.
        
        ```
        os.makedirs(save_dir, exist_ok=True)
        ```
        
        를 반드시 사용합니다.
        
        ---
        
        ### 실수 2. 같은 파일명으로 계속 덮어씀
        
        다음처럼 쓰면 매번 같은 파일을 덮어씁니다.
        
        ```
        cv2.imwrite("capture.jpg", frame)
        ```
        
        데이터셋 수집에서는 번호나 시간 기반 파일명을 사용해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        카메라 프레임 캡처는 ROS2 실습에서 매우 자주 필요합니다.
        
        ```
        1. 라인트레이싱 학습 이미지 수집
        2. 객체 인식 학습 데이터셋 수집
        3. 장애물 검출 실패 장면 저장
        4. 로봇 팔 Pick 위치 샘플 이미지 저장
        5. 알고리즘 디버깅용 프레임 저장
        ```
        
        ROS2 카메라 노드에서도 같은 개념으로 특정 조건에서 프레임을 저장할 수 있습니다.
        
        ```
        객체 검출 실패
        → 현재 프레임 저장
        → 나중에 원인 분석
        ```
        
        ---
        
        # 6단계 핵심 정리
        
        이번 6단계에서는 카메라와 비디오 처리의 핵심 문법을 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 51 | 웹캠 열기 |
        | 52 | 실시간 프레임 출력 |
        | 53 | 키보드 입력 처리 |
        | 54 | 카메라 해상도 설정 |
        | 55 | FPS 확인 |
        | 56 | 비디오 파일 읽기 |
        | 57 | 비디오 저장 |
        | 58 | 실시간 흑백 변환 |
        | 59 | 실시간 Edge 검출 |
        | 60 | 카메라 프레임 캡처 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        cap = cv2.VideoCapture(0)
        ```
        
        기본 웹캠을 엽니다.
        
        ```
        ret, frame = cap.read()
        ```
        
        카메라에서 한 프레임을 읽습니다.
        
        ```
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        ```
        
        카메라 열기 성공 여부를 확인합니다.
        
        ```
        cv2.imshow("Camera", frame)
        ```
        
        프레임을 화면에 출력합니다.
        
        ```
        key = cv2.waitKey(1)
        ```
        
        실시간 영상에서 키 입력을 받습니다.
        
        ```
        if key == ord('q'):
            break
        ```
        
        `q` 키로 종료합니다.
        
        ```
        cap.release()
        cv2.destroyAllWindows()
        ```
        
        카메라와 창을 정리합니다.
        
        ```
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ```
        
        카메라 해상도를 설정합니다.
        
        ```
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ```
        
        실시간 프레임을 흑백으로 변환합니다.
        
        ```
        edges = cv2.Canny(blurred, 50, 150)
        ```
        
        실시간 Edge를 검출합니다.
        
        ```
        cv2.imwrite(file_path, frame)
        ```
        
        현재 프레임을 이미지로 저장합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        이번 단계는 OpenCV 단독 실습에서 ROS2 비전 노드로 넘어가는 연결 다리입니다.
        
        OpenCV 실시간 구조는 다음과 같습니다.
        
        ```
        VideoCapture
        → frame 읽기
        → OpenCV 처리
        → imshow
        ```
        
        ROS2 구조는 다음과 같습니다.
        
        ```
        /camera/image_raw Subscribe
        → cv_bridge
        → OpenCV frame 변환
        → OpenCV 처리
        → 결과 Publish
        ```
        
        즉, 이번 단계에서 배운 `frame` 처리 방식은 ROS2에서도 거의 그대로 사용됩니다.
        
        ---
        
        # 실무 기준 처리 흐름 예시
        
        ## 실시간 라인 트레이싱 준비
        
        ```
        카메라 프레임 읽기
        → ROI 자르기
        → Grayscale
        → Gaussian Blur
        → Threshold
        → Contour
        → 중심점 계산
        ```
        
        ## 실시간 객체 외곽선 검출
        
        ```
        카메라 프레임 읽기
        → Grayscale
        → Gaussian Blur
        → Canny Edge
        → Contour
        → Bounding Box
        ```
        
        ## 학습 데이터 수집
        
        ```
        카메라 프레임 읽기
        → s 키 입력
        → 이미지 저장
        → 라벨링 도구로 이동
        → YOLO 학습 데이터셋 구성
        ```
        
        ---
        
        # 실무에서 가장 중요한 판단 기준
        
        | 상황 | 확인할 것 |
        | --- | --- |
        | 카메라가 안 열림 | 카메라 번호, 권한, 다른 프로그램 사용 여부 |
        | 영상이 느림 | 해상도, 필터 크기, FPS |
        | 영상이 너무 큼 | 해상도 낮추기 또는 Resize |
        | 저장 영상이 깨짐 | VideoWriter 크기, 코덱, out.release() |
        | 프레임 저장 실패 | 저장 폴더 존재 여부 |
        | Docker/WSL2에서 카메라 안 됨 | 장치 매핑, USB 연결, GUI 설정 |
        | ROS2로 넘어갈 예정 | frame 처리 코드를 함수화하기 |
    - 7단계: 객체 추적과 색상 기반 인식
        
        이번 단계는 ROS2 Humble 로봇 비전에서 가장 실전적인 입문 주제입니다.
        
        로봇은 카메라 영상에서 다음과 같은 정보를 찾아야 합니다.
        
        ```
        빨간 공이 어디에 있는가?
        파란색 표식이 화면 중앙에서 얼마나 벗어났는가?
        초록색 라인을 따라가야 하는가?
        객체가 여러 개일 때 어느 것을 따라가야 하는가?
        검출 결과를 ROS2 Topic으로 보낼 준비가 되었는가?
        ```
        
        이번 단계의 핵심 흐름은 다음입니다.
        
        ```
        BGR 카메라 프레임
        → HSV 변환
        → 색상 범위 마스크 생성
        → 노이즈 제거
        → Contour 검출
        → Bounding Box / 중심점 계산
        → 추적 결과 표시
        → ROS2 Topic 발행 준비
        ```
        
        ---
        
        # 7단계: 객체 추적과 색상 기반 인식
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 61 | HSV 색상 마스크 |
        | 62 | 빨간색 객체 검출 |
        | 63 | 파란색 객체 검출 |
        | 64 | 초록색 객체 검출 |
        | 65 | 마스크 노이즈 제거 |
        | 66 | 객체 중심 추적 |
        | 67 | 실시간 원 검출 |
        | 68 | 색상 객체 Bounding Box |
        | 69 | 여러 객체 추적 |
        | 70 | ROS2 Topic 변환 준비 |
        
        ---
        
        # 예제 61. HSV 색상 마스크
        
        ## 핵심 주제
        
        HSV 색상 공간에서 특정 색상 범위에 해당하는 픽셀만 흰색으로 만들고, 나머지는 검은색으로 만드는 마스크를 생성합니다.
        
        색상 기반 객체 검출의 시작점입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. BGR 이미지를 HSV로 변환
        2. 특정 HSV 범위 지정
        3. cv2.inRange()로 마스크 생성
        4. 원본 이미지에서 해당 색상만 추출
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_color = np.array([100, 100, 100])
            upper_color = np.array([130, 255, 255])
        
            mask = cv2.inRange(hsv, lower_color, upper_color)
        
            result = cv2.bitwise_and(image, image, mask=mask)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("HSV Mask", mask)
            cv2.imshow("Color Extract Result", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. HSV 범위를 RGB 기준으로 생각함
        
        OpenCV의 HSV 범위는 다음과 같습니다.
        
        ```
        H: 0 ~ 179
        S: 0 ~ 255
        V: 0 ~ 255
        ```
        
        Hue를 0~360으로 생각하면 범위 설정이 틀어집니다.
        
        ---
        
        ### 실수 2. 조명 변화 고려 없이 범위를 고정함
        
        같은 물체라도 조명이 바뀌면 HSV 값이 달라집니다.
        
        실무에서는 다음 조건을 테스트해야 합니다.
        
        ```
        밝은 조명
        어두운 조명
        그림자
        햇빛
        카메라 자동 화이트밸런스
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 색상 객체 추적 노드는 보통 다음 구조를 가집니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → BGR frame
        → HSV 변환
        → inRange 마스크
        → Contour 검출
        → 중심 좌표 계산
        → /target_position 발행
        ```
        
        ---
        
        # 예제 62. 빨간색 객체 검출
        
        ## 핵심 주제
        
        HSV에서 빨간색 객체를 검출합니다.
        
        빨간색은 HSV Hue 값에서 특이한 점이 있습니다.
        
        OpenCV Hue 범위가 0~179이기 때문에 빨간색은 양 끝에 걸쳐 있습니다.
        
        ```
        빨간색 범위 1: H 0 ~ 10
        빨간색 범위 2: H 170 ~ 179
        ```
        
        그래서 빨간색은 마스크를 두 개 만든 뒤 합치는 방식이 일반적입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 빨간색 HSV 범위 이해
        2. 빨간색 마스크 2개 생성
        3. 두 마스크 합치기
        4. 빨간색 객체만 추출
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/red_object.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_red1 = np.array([0, 100, 100])
            upper_red1 = np.array([10, 255, 255])
        
            lower_red2 = np.array([170, 100, 100])
            upper_red2 = np.array([179, 255, 255])
        
            mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        
            red_mask = cv2.bitwise_or(mask1, mask2)
        
            red_result = cv2.bitwise_and(image, image, mask=red_mask)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Red Mask", red_mask)
            cv2.imshow("Red Object Result", red_result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 준비 파일
        
        빨간색 물체가 포함된 이미지를 준비합니다.
        
        ```
        practice_images/red_object.jpg
        ```
        
        예를 들어 빨간 공, 빨간 컵, 빨간 표식이 있는 이미지가 좋습니다.
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 빨간색 범위를 하나만 사용함
        
        다음처럼 하나만 쓰면 일부 빨간색이 검출되지 않을 수 있습니다.
        
        ```
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        ```
        
        빨간색은 Hue 양 끝에 걸치므로 보통 두 범위를 사용합니다.
        
        ---
        
        ### 실수 2. S, V 최소값을 너무 낮게 설정
        
        S와 V 최소값이 너무 낮으면 회색, 어두운 그림자, 노이즈까지 빨간색으로 잡힐 수 있습니다.
        
        ```
        S: 채도
        V: 밝기
        ```
        
        초기값은 보통 100 정도에서 시작한 뒤 조정합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        빨간 공 추적 로봇은 다음 흐름으로 만들 수 있습니다.
        
        ```
        카메라 프레임
        → HSV 변환
        → 빨간색 마스크
        → Contour 검출
        → 가장 큰 Contour 선택
        → 중심점 계산
        → 화면 중앙과 비교
        → /cmd_vel 제어
        ```
        
        ---
        
        # 예제 63. 파란색 객체 검출
        
        ## 핵심 주제
        
        HSV 색상 공간에서 파란색 객체를 검출합니다.
        
        파란색은 빨간색보다 범위 설정이 비교적 단순합니다.
        
        일반적으로 OpenCV HSV 기준으로 다음 범위에서 시작할 수 있습니다.
        
        ```
        H: 100 ~ 130
        S: 100 ~ 255
        V: 100 ~ 255
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 파란색 HSV 범위 설정
        2. 파란색 마스크 생성
        3. 파란색 영역 추출
        4. 색상 객체 검출 흐름 반복 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/blue_object.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_blue = np.array([100, 100, 100])
            upper_blue = np.array([130, 255, 255])
        
            blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
            blue_result = cv2.bitwise_and(image, image, mask=blue_mask)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Blue Mask", blue_mask)
            cv2.imshow("Blue Object Result", blue_result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 준비 파일
        
        파란색 물체가 포함된 이미지를 준비합니다.
        
        ```
        practice_images/blue_object.jpg
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 파란색 계열 차이를 고려하지 않음
        
        파란색도 여러 종류가 있습니다.
        
        ```
        하늘색
        진한 파랑
        남색
        청록색에 가까운 파랑
        ```
        
        각 색은 HSV Hue 범위가 다를 수 있습니다.
        
        ---
        
        ### 실수 2. 조명 때문에 검출이 흔들림
        
        밝기 값 V가 낮으면 같은 파란색도 검출되지 않을 수 있습니다.
        
        어두운 환경에서는 `lower_blue`의 V 값을 낮춰야 할 수 있습니다.
        
        ```
        lower_blue = np.array([100, 80, 50])
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        파란색 마커 추적은 교육용 로봇에서 많이 사용합니다.
        
        ```
        파란색 표식 검출
        → 중심 좌표 계산
        → 화면 중앙 기준 error_x 계산
        → 로봇 회전 제어
        ```
        
        ---
        
        # 예제 64. 초록색 객체 검출
        
        ## 핵심 주제
        
        HSV 색상 공간에서 초록색 객체를 검출합니다.
        
        일반적인 초록색 HSV 범위는 다음에서 시작할 수 있습니다.
        
        ```
        H: 40 ~ 80
        S: 80 ~ 255
        V: 80 ~ 255
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 초록색 HSV 범위 설정
        2. 초록색 마스크 생성
        3. 초록색 객체 추출
        4. 색상별 범위 설정 감각 익히기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/green_object.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_green = np.array([40, 80, 80])
            upper_green = np.array([80, 255, 255])
        
            green_mask = cv2.inRange(hsv, lower_green, upper_green)
        
            green_result = cv2.bitwise_and(image, image, mask=green_mask)
        
            cv2.imshow("Original Image", image)
            cv2.imshow("Green Mask", green_mask)
            cv2.imshow("Green Object Result", green_result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 준비 파일
        
        초록색 물체가 포함된 이미지를 준비합니다.
        
        ```
        practice_images/green_object.jpg
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 초록색과 노란색 경계를 혼동함
        
        연두색이나 노란빛이 강한 초록색은 Hue 값이 예상보다 낮을 수 있습니다.
        
        필요하면 범위를 넓힙니다.
        
        ```
        lower_green = np.array([35, 60, 60])
        upper_green = np.array([85, 255, 255])
        ```
        
        ---
        
        ### 실수 2. 배경에 같은 색이 있는 경우
        
        초록색 객체를 찾으려는데 배경에도 초록색이 많으면 잘못 검출됩니다.
        
        이때는 색상만 보지 말고 다음 조건을 추가해야 합니다.
        
        ```
        면적
        위치
        모양
        ROI
        움직임
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        초록색 라인 기반 주행은 라인트레이싱 교육에서 자주 사용됩니다.
        
        ```
        카메라 프레임
        → HSV 변환
        → 초록색 마스크
        → ROI 하단 영역만 사용
        → Contour 중심 계산
        → /cmd_vel 제어
        ```
        
        ---
        
        # 예제 65. 마스크 노이즈 제거
        
        ## 핵심 주제
        
        색상 마스크에는 작은 점 노이즈가 생길 수 있습니다.
        
        이런 노이즈를 제거하지 않으면 Contour가 너무 많이 검출되고 객체 추적이 흔들립니다.
        
        이번 예제에서는 Morphology 연산을 사용해 마스크를 정리합니다.
        
        대표 연산은 다음과 같습니다.
        
        ```
        Opening: 작은 흰 점 제거
        Closing: 객체 내부의 작은 구멍 메우기
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 색상 마스크의 노이즈 문제 이해
        2. cv2.morphologyEx() 사용법 이해
        3. Opening으로 작은 점 제거
        4. Closing으로 구멍 메우기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/blue_object.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_blue = np.array([100, 100, 100])
            upper_blue = np.array([130, 255, 255])
        
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
            kernel = np.ones((5, 5), np.uint8)
        
            opened_mask = cv2.morphologyEx(
                mask,
                cv2.MORPH_OPEN,
                kernel
            )
        
            cleaned_mask = cv2.morphologyEx(
                opened_mask,
                cv2.MORPH_CLOSE,
                kernel
            )
        
            result = cv2.bitwise_and(image, image, mask=cleaned_mask)
        
            cv2.imshow("Original Mask", mask)
            cv2.imshow("Opened Mask", opened_mask)
            cv2.imshow("Cleaned Mask", cleaned_mask)
            cv2.imshow("Cleaned Result", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 커널 크기를 너무 크게 설정
        
        커널이 너무 크면 작은 객체까지 사라질 수 있습니다.
        
        ```
        kernel = np.ones((15, 15), np.uint8)
        ```
        
        처음에는 3×3 또는 5×5로 시작하는 것이 좋습니다.
        
        ---
        
        ### 실수 2. Opening과 Closing 순서를 이해하지 못함
        
        일반적인 색상 마스크 정리 흐름은 다음과 같습니다.
        
        ```
        마스크 생성
        → Opening으로 작은 흰 점 제거
        → Closing으로 객체 내부 구멍 메우기
        ```
        
        하지만 이미지 상태에 따라 순서를 바꿔야 할 수도 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 객체 추적에서 마스크 노이즈 제거는 매우 중요합니다.
        
        ```
        마스크 노이즈 많음
        → Contour가 많이 생김
        → 중심 좌표가 흔들림
        → 로봇 제어가 흔들림
        ```
        
        마스크를 정리하면 객체 중심이 안정되어 로봇 제어도 안정됩니다.
        
        ---
        
        # 예제 66. 객체 중심 추적
        
        ## 핵심 주제
        
        색상 마스크에서 Contour를 찾고, 가장 큰 객체의 중심 좌표를 계산합니다.
        
        이 예제는 색상 기반 객체 추적의 핵심입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 색상 마스크 생성
        2. Contour 검출
        3. 가장 큰 Contour 선택
        4. 중심 좌표 계산
        5. 화면 중앙 대비 오차 계산
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_blue = np.array([100, 100, 100])
                upper_blue = np.array([130, 255, 255])
        
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, hierarchy = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                height, width = frame.shape[:2]
                image_center_x = width // 2
        
                cv2.line(
                    frame,
                    (image_center_x, 0),
                    (image_center_x, height),
                    (255, 0, 0),
                    2
                )
        
                if len(contours) > 0:
                    largest_contour = max(contours, key=cv2.contourArea)
                    area = cv2.contourArea(largest_contour)
        
                    if area > 500:
                        moments = cv2.moments(largest_contour)
        
                        if moments["m00"] != 0:
                            center_x = int(moments["m10"] / moments["m00"])
                            center_y = int(moments["m01"] / moments["m00"])
        
                            error_x = center_x - image_center_x
        
                            cv2.drawContours(
                                frame,
                                [largest_contour],
                                -1,
                                (0, 255, 0),
                                2
                            )
        
                            cv2.circle(
                                frame,
                                (center_x, center_y),
                                8,
                                (0, 0, 255),
                                -1
                            )
        
                            cv2.putText(
                                frame,
                                f"Center: ({center_x}, {center_y})",
                                (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7,
                                (0, 0, 255),
                                2
                            )
        
                            cv2.putText(
                                frame,
                                f"Error X: {error_x}",
                                (20, 70),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7,
                                (0, 255, 255),
                                2
                            )
        
                cv2.imshow("Object Tracking", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 가장 큰 Contour가 항상 목표 객체라고 가정함
        
        배경에 같은 색의 큰 영역이 있으면 잘못 추적할 수 있습니다.
        
        실무에서는 다음 조건을 함께 봅니다.
        
        ```
        면적
        위치
        가로세로 비율
        ROI 영역
        이전 프레임 위치
        움직임 연속성
        ```
        
        ---
        
        ### 실수 2. error_x를 바로 로봇 속도로 사용함
        
        `error_x`는 픽셀 단위입니다.
        
        로봇 회전 속도로 바꾸려면 적절한 비례 계수가 필요합니다.
        
        ```
        angular_z = -0.002 * error_x
        ```
        
        단, 실제 로봇에서는 최대 속도 제한을 반드시 적용해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 ROS2 객체 추적 노드의 핵심 로직입니다.
        
        ```
        center_x, center_y, error_x
        ```
        
        이 값을 ROS2 메시지로 발행하면 주행 제어 노드에서 사용할 수 있습니다.
        
        ---
        
        # 예제 67. 실시간 원 검출
        
        ## 핵심 주제
        
        실시간 카메라 영상에서 색상 기반으로 객체를 검출한 뒤, 최소 외접 원을 그립니다.
        
        공처럼 둥근 물체를 추적할 때 적합합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 색상 마스크 생성
        2. Contour 검출
        3. 최소 외접 원 계산
        4. 중심점과 반지름 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_red1 = np.array([0, 100, 100])
                upper_red1 = np.array([10, 255, 255])
                lower_red2 = np.array([170, 100, 100])
                upper_red2 = np.array([179, 255, 255])
        
                mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
                mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
                mask = cv2.bitwise_or(mask1, mask2)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, hierarchy = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                if len(contours) > 0:
                    largest_contour = max(contours, key=cv2.contourArea)
                    area = cv2.contourArea(largest_contour)
        
                    if area > 500:
                        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        
                        if radius > 10:
                            center = (int(x), int(y))
                            radius = int(radius)
        
                            cv2.circle(
                                frame,
                                center,
                                radius,
                                (0, 255, 255),
                                2
                            )
        
                            cv2.circle(
                                frame,
                                center,
                                5,
                                (0, 0, 255),
                                -1
                            )
        
                            cv2.putText(
                                frame,
                                f"Radius: {radius}",
                                (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7,
                                (0, 255, 255),
                                2
                            )
        
                cv2.imshow("Circle Tracking", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 원형이 아닌 객체에도 외접 원을 사용함
        
        사각형 물체에도 외접 원은 그릴 수 있지만, 실제 모양을 잘 표현하지 못합니다.
        
        원형 객체에는 외접 원이 좋고, 일반 객체에는 Bounding Box가 더 좋습니다.
        
        ---
        
        ### 실수 2. 반지름을 거리로 바로 변환함
        
        반지름이 크면 가까운 것은 맞지만, 실제 거리로 바꾸려면 카메라 캘리브레이션과 객체 실제 크기 정보가 필요합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        공 추적 로봇에서는 다음 값을 발행할 수 있습니다.
        
        ```
        center_x
        center_y
        radius
        ```
        
        이 중 `radius`는 접근/정지 판단에 활용할 수 있습니다.
        
        ```
        radius가 작음 → 멀리 있음 → 전진
        radius가 큼 → 가까움 → 정지
        ```
        
        ---
        
        # 예제 68. 색상 객체 Bounding Box
        
        ## 핵심 주제
        
        색상 마스크에서 검출된 객체에 Bounding Box를 그립니다.
        
        Bounding Box는 객체의 위치와 크기를 간단하게 표현하는 데 매우 유용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 색상 마스크 생성
        2. Contour 검출
        3. Bounding Box 계산
        4. 중심 좌표와 크기 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_green = np.array([40, 80, 80])
                upper_green = np.array([80, 255, 255])
        
                mask = cv2.inRange(hsv, lower_green, upper_green)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, hierarchy = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                for contour in contours:
                    area = cv2.contourArea(contour)
        
                    if area > 500:
                        x, y, w, h = cv2.boundingRect(contour)
        
                        center_x = x + w // 2
                        center_y = y + h // 2
        
                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (0, 255, 0),
                            2
                        )
        
                        cv2.circle(
                            frame,
                            (center_x, center_y),
                            5,
                            (0, 0, 255),
                            -1
                        )
        
                        cv2.putText(
                            frame,
                            f"x:{x} y:{y} w:{w} h:{h}",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 255, 0),
                            2
                        )
        
                cv2.imshow("Color Bounding Box", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Bounding Box 중심과 Contour 중심을 혼동함
        
        Bounding Box 중심은 박스 기준 중심입니다.
        
        ```
        center_x = x + w // 2
        center_y = y + h // 2
        ```
        
        Contour 중심은 실제 객체 모양의 무게중심에 가깝습니다.
        
        ```
        moments = cv2.moments(contour)
        ```
        
        객체가 기울어져 있거나 불규칙하면 두 중심이 다를 수 있습니다.
        
        ---
        
        ### 실수 2. 여러 객체가 있을 때 모든 박스를 목표로 사용함
        
        추적 대상이 하나라면 가장 큰 객체만 선택하는 것이 더 안정적입니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Bounding Box는 ROS2 비전 메시지로 표현하기 좋습니다.
        
        ```
        class_id
        x
        y
        width
        height
        center_x
        center_y
        area
        ```
        
        이 구조는 YOLO 같은 딥러닝 검출 결과와도 비슷합니다.
        
        ---
        
        # 예제 69. 여러 객체 추적
        
        ## 핵심 주제
        
        색상 마스크에서 여러 객체를 동시에 검출하고 각각의 중심과 Bounding Box를 표시합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 여러 Contour 처리
        2. 면적 기준 필터링
        3. 객체 번호 표시
        4. 여러 객체 중심점 계산
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_blue = np.array([100, 100, 100])
                upper_blue = np.array([130, 255, 255])
        
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, hierarchy = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                object_id = 0
        
                for contour in contours:
                    area = cv2.contourArea(contour)
        
                    if area > 500:
                        x, y, w, h = cv2.boundingRect(contour)
        
                        center_x = x + w // 2
                        center_y = y + h // 2
        
                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (255, 0, 0),
                            2
                        )
        
                        cv2.circle(
                            frame,
                            (center_x, center_y),
                            5,
                            (0, 0, 255),
                            -1
                        )
        
                        cv2.putText(
                            frame,
                            f"ID:{object_id} Area:{int(area)}",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (255, 0, 0),
                            2
                        )
        
                        print(
                            "ID:",
                            object_id,
                            "Center:",
                            center_x,
                            center_y,
                            "Area:",
                            area
                        )
        
                        object_id += 1
        
                cv2.imshow("Multi Object Tracking", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. object_id가 진짜 추적 ID라고 생각함
        
        이 예제의 `object_id`는 현재 프레임에서 순서대로 붙인 번호입니다.
        
        다음 프레임에서도 같은 객체가 같은 ID를 유지한다는 보장은 없습니다.
        
        진짜 객체 추적 ID를 유지하려면 다음 기술이 필요합니다.
        
        ```
        이전 프레임 중심점과 현재 프레임 중심점 매칭
        Kalman Filter
        SORT
        DeepSORT
        ByteTrack
        ```
        
        ---
        
        ### 실수 2. Contour 순서를 신뢰함
        
        `findContours()`가 반환하는 순서는 항상 원하는 정렬 순서가 아닙니다.
        
        필요하면 면적 기준으로 정렬합니다.
        
        ```
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        여러 객체를 ROS2로 보낼 때는 배열 형태의 메시지가 필요합니다.
        
        예를 들면 다음과 같은 구조입니다.
        
        ```
        detected_objects:
          - id
          - center_x
          - center_y
          - width
          - height
          - area
        ```
        
        커스텀 메시지나 `vision_msgs` 계열 메시지로 확장할 수 있습니다.
        
        ---
        
        # 예제 70. ROS2 Topic 변환 준비
        
        ## 핵심 주제
        
        OpenCV에서 계산한 객체 정보를 ROS2 Topic으로 발행할 수 있도록 데이터 구조를 정리합니다.
        
        이번 예제는 실제 ROS2 코드는 아니지만, ROS2 노드로 옮기기 쉽게 OpenCV 처리 결과를 딕셔너리 형태로 정리합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 객체 검출 결과를 구조화
        2. 중심 좌표, 면적, 박스 정보 저장
        3. ROS2 메시지로 변환하기 쉬운 형태 이해
        4. OpenCV 코드와 ROS2 코드 분리 준비
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        def detect_blue_objects(frame):
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
            lower_blue = np.array([100, 100, 100])
            upper_blue = np.array([130, 255, 255])
        
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
            contours, hierarchy = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            objects = []
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > 500:
                    x, y, w, h = cv2.boundingRect(contour)
        
                    center_x = x + w // 2
                    center_y = y + h // 2
        
                    obj = {
                        "center_x": center_x,
                        "center_y": center_y,
                        "x": x,
                        "y": y,
                        "width": w,
                        "height": h,
                        "area": area
                    }
        
                    objects.append(obj)
        
            return objects, mask
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                objects, mask = detect_blue_objects(frame)
        
                for index, obj in enumerate(objects):
                    x = obj["x"]
                    y = obj["y"]
                    w = obj["width"]
                    h = obj["height"]
                    center_x = obj["center_x"]
                    center_y = obj["center_y"]
                    area = obj["area"]
        
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (255, 0, 0),
                        2
                    )
        
                    cv2.circle(
                        frame,
                        (center_x, center_y),
                        5,
                        (0, 0, 255),
                        -1
                    )
        
                    cv2.putText(
                        frame,
                        f"Obj {index} Area {int(area)}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 0, 0),
                        2
                    )
        
                print("ROS2 Topic으로 보낼 객체 목록:", objects)
        
                cv2.imshow("ROS2 Ready Detection", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. OpenCV 처리 코드와 ROS2 Publisher 코드를 섞어버림
        
        초보자는 한 함수 안에 다음을 모두 넣는 경우가 많습니다.
        
        ```
        이미지 변환
        색상 검출
        Contour 계산
        ROS2 메시지 생성
        Publish
        화면 출력
        ```
        
        이렇게 하면 디버깅이 어려워집니다.
        
        권장 구조는 다음입니다.
        
        ```
        detect_objects(frame)
        → 객체 정보 반환
        ROS2 callback
        → detect_objects 호출
        → 메시지 변환
        → publish
        ```
        
        ---
        
        ### 실수 2. NumPy 타입을 ROS2 메시지에 바로 넣음
        
        OpenCV 결과 중 일부 값은 NumPy 타입일 수 있습니다.
        
        ROS2 메시지에는 Python 기본 타입으로 변환하는 것이 안전합니다.
        
        ```
        center_x=int(center_x)
        area=float(area)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제의 `objects` 리스트는 ROS2에서 다음과 같은 메시지로 바꿀 수 있습니다.
        
        ```
        center_x: int
        center_y: int
        x: int
        y: int
        width: int
        height: int
        area: float
        ```
        
        간단한 실습에서는 `std_msgs/String`으로 JSON 문자열을 발행할 수도 있습니다.
        
        ```
        [
          {
            "center_x":320,
            "center_y":240,
            "x":280,
            "y":200,
            "width":80,
            "height":80,
            "area":5200.0
          }
        ]
        ```
        
        정식 프로젝트에서는 커스텀 메시지를 만드는 것이 좋습니다.
        
        ---
        
        # 7단계 핵심 정리
        
        이번 7단계에서는 색상 기반 객체 검출과 추적의 핵심 흐름을 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 61 | HSV 색상 마스크 |
        | 62 | 빨간색 객체 검출 |
        | 63 | 파란색 객체 검출 |
        | 64 | 초록색 객체 검출 |
        | 65 | 마스크 노이즈 제거 |
        | 66 | 객체 중심 추적 |
        | 67 | 실시간 원 검출 |
        | 68 | 색상 객체 Bounding Box |
        | 69 | 여러 객체 추적 |
        | 70 | ROS2 Topic 변환 준비 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        ```
        
        BGR 이미지를 HSV로 변환합니다.
        
        ```
        mask = cv2.inRange(hsv, lower_color, upper_color)
        ```
        
        특정 색상 범위만 마스크로 만듭니다.
        
        ```
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        ```
        
        마스크 노이즈를 제거합니다.
        
        ```
        contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        ```
        
        마스크에서 외곽선을 찾습니다.
        
        ```
        largest_contour = max(contours, key=cv2.contourArea)
        ```
        
        가장 큰 객체를 선택합니다.
        
        ```
        x, y, w, h = cv2.boundingRect(contour)
        ```
        
        Bounding Box를 계산합니다.
        
        ```
        center_x = x + w // 2
        center_y = y + h // 2
        ```
        
        박스 중심 좌표를 계산합니다.
        
        ```
        moments = cv2.moments(contour)
        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])
        ```
        
        Contour 중심 좌표를 계산합니다.
        
        ```
        error_x = center_x - image_center_x
        ```
        
        화면 중앙 대비 객체 위치 오차를 계산합니다.
        
        ```
        objects.append({
            "center_x": center_x,
            "center_y": center_y,
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "area": area
        })
        ```
        
        ROS2 Topic으로 보낼 수 있도록 객체 정보를 구조화합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        이번 단계는 OpenCV에서 ROS2 비전 제어로 넘어가는 핵심입니다.
        
        ```
        카메라 프레임
        → 색상 기반 객체 검출
        → 중심점 계산
        → 화면 중앙 대비 오차 계산
        → ROS2 Topic 발행
        → 주행 제어 또는 로봇 팔 제어
        ```
        
        특히 다음 ROS2 프로젝트의 기반이 됩니다.
        
        ```
        색상 공 추종 로봇
        라인 트레이싱 로봇
        색상 마커 기반 위치 추정
        컨베이어 색상 객체 분류
        로봇 팔 Pick 위치 검출
        ```
        
        ---
        
        # 실무 기준 색상 검출 처리 흐름
        
        ## 단일 색상 객체 추적
        
        ```
        BGR frame
        → HSV
        → inRange
        → Morphology
        → Contour
        → 가장 큰 Contour
        → 중심 좌표
        → error_x
        ```
        
        ## 여러 객체 검출
        
        ```
        BGR frame
        → HSV
        → 색상 마스크
        → Morphology
        → Contour 목록
        → 면적 필터링
        → 객체별 Bounding Box
        → 객체 목록 생성
        ```
        
        ## ROS2 Topic 발행 준비
        
        ```
        OpenCV 검출 결과
        → Python dict/list 구조
        → ROS2 메시지 변환
        → Publisher 발행
        → 제어 노드 Subscriber 수신
        ```
        
        ---
        
        # 실무에서 가장 중요한 판단 기준
        
        | 상황 | 추천 처리 |
        | --- | --- |
        | 색상 객체가 흔들리며 잡힘 | HSV 범위 조정 |
        | 작은 점이 많이 잡힘 | Morphology Opening |
        | 객체 내부가 뚫려 보임 | Morphology Closing |
        | 배경도 같은 색으로 잡힘 | ROI, 면적, 모양 조건 추가 |
        | 객체 하나만 추적 | 가장 큰 Contour 선택 |
        | 여러 객체 추적 | 모든 Contour 순회 |
        | 로봇 제어 필요 | center_x, error_x 계산 |
        | ROS2 연동 필요 | 검출 결과를 구조화 |
    - 8단계: 특징점, 매칭, 템플릿 매칭
        
        이번 단계는 ROS2 Humble 로봇 비전에서 **이미지 안의 물체를 색상만으로 찾기 어려울 때** 사용하는 핵심 기법입니다.
        
        색상 기반 검출은 빠르고 쉽지만 다음 상황에서는 한계가 있습니다.
        
        ```
        조명이 바뀌면 색상이 달라짐
        비슷한 색의 배경이 있으면 오검출됨
        물체의 색보다 모양이나 패턴이 더 중요함
        특정 로고, 부품, 마커, 이미지 패턴을 찾아야 함
        카메라가 움직여도 같은 물체를 인식해야 함
        ```
        
        이번 단계에서는 다음 흐름을 배웁니다.
        
        ```
        이미지 밝기 분포 분석
        → 히스토그램 평활화
        → 템플릿 매칭
        → ORB 특징점 검출
        → 특징점 매칭
        → 간단한 물체 인식
        → 로봇 비전 적용
        ```
        
        ---
        
        # 8단계: 특징점, 매칭, 템플릿 매칭
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 71 | 이미지 히스토그램 |
        | 72 | 히스토그램 평활화 |
        | 73 | CLAHE |
        | 74 | Template Matching |
        | 75 | ORB 특징점 검출 |
        | 76 | ORB 특징점 매칭 |
        | 77 | 이미지 유사도 비교 |
        | 78 | Feature Matching 시각화 |
        | 79 | 간단한 물체 인식 |
        | 80 | 로봇 비전에서 특징점 활용 |
        
        ---
        
        # 예제 71. 이미지 히스토그램
        
        ## 핵심 주제
        
        히스토그램은 이미지의 픽셀 밝기 값이 얼마나 분포되어 있는지 보여주는 그래프입니다.
        
        흑백 이미지 기준으로 픽셀 값은 보통 0~255입니다.
        
        ```
        0   = 검정
        255 = 흰색
        중간값 = 회색
        ```
        
        히스토그램을 보면 이미지가 어두운지, 밝은지, 대비가 약한지 확인할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Grayscale 이미지로 변환
        2. cv2.calcHist() 사용법 이해
        3. 밝기 분포 계산
        4. matplotlib로 히스토그램 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import matplotlib.pyplot as plt
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            hist = cv2.calcHist(
                [gray],
                [0],
                None,
                [256],
                [0, 256]
            )
        
            cv2.imshow("Gray Image", gray)
        
            plt.figure()
            plt.title("Grayscale Histogram")
            plt.xlabel("Pixel Value")
            plt.ylabel("Pixel Count")
            plt.plot(hist)
            plt.xlim([0, 256])
            plt.show()
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. OpenCV BGR 이미지를 matplotlib에 그대로 표시함
        
        이 예제에서는 히스토그램만 그리므로 큰 문제는 없지만, 컬러 이미지를 matplotlib로 표시할 때는 BGR/RGB 변환이 필요합니다.
        
        ```
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(rgb)
        ```
        
        ---
        
        ### 실수 2. 히스토그램만 보고 모든 것을 판단함
        
        히스토그램은 밝기 분포를 보여주지만, 객체 위치나 모양은 알려주지 않습니다.
        
        따라서 히스토그램은 보조 분석 도구로 사용해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 카메라 영상이 너무 어둡거나 너무 밝을 때 히스토그램을 보면 원인을 파악하기 쉽습니다.
        
        ```
        히스토그램이 왼쪽에 몰림 → 전체적으로 어두움
        히스토그램이 오른쪽에 몰림 → 전체적으로 밝음
        히스토그램이 좁게 몰림 → 대비가 낮음
        히스토그램이 넓게 퍼짐 → 대비가 높음
        ```
        
        로봇 카메라 전처리 튜닝에서 중요한 진단 도구입니다.
        
        ---
        
        # 예제 72. 히스토그램 평활화
        
        ## 핵심 주제
        
        히스토그램 평활화는 어둡거나 대비가 낮은 이미지를 더 선명하게 보이도록 밝기 분포를 넓게 펴는 기법입니다.
        
        특히 Grayscale 이미지에서 많이 사용합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2.equalizeHist() 사용법 이해
        2. 대비 개선 효과 확인
        3. 원본 히스토그램과 평활화 후 히스토그램 비교
        4. 조명 보정 기초 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
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
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 컬러 이미지에 equalizeHist를 바로 적용
        
        `cv2.equalizeHist()`는 1채널 이미지에 적용해야 합니다.
        
        잘못된 예:
        
        ```
        equalized = cv2.equalizeHist(image)
        ```
        
        올바른 예:
        
        ```
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        ```
        
        ---
        
        ### 실수 2. 평활화가 항상 좋은 결과를 만든다고 생각함
        
        히스토그램 평활화는 노이즈도 함께 강조할 수 있습니다.
        
        어두운 이미지에서는 효과가 좋을 수 있지만, 노이즈가 많은 영상에서는 오히려 결과가 나빠질 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇 카메라가 어두운 실내에서 동작할 때 평활화는 Edge나 Threshold 검출을 도울 수 있습니다.
        
        ```
        카메라 프레임
        → Grayscale
        → Histogram Equalization
        → Threshold 또는 Canny
        → Contour
        ```
        
        하지만 실시간 영상에서는 처리 결과가 프레임마다 흔들릴 수 있으므로 주의해야 합니다.
        
        ---
        
        # 예제 73. CLAHE
        
        ## 핵심 주제
        
        CLAHE는 Contrast Limited Adaptive Histogram Equalization의 약자입니다.
        
        일반 히스토그램 평활화는 이미지 전체에 같은 방식으로 적용하지만, CLAHE는 작은 영역별로 대비를 조정합니다.
        
        조명이 고르지 않은 이미지에서 더 안정적입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. CLAHE 개념 이해
        2. cv2.createCLAHE() 사용법 이해
        3. clipLimit와 tileGridSize 의미 이해
        4. 일반 평활화와 차이 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            equalized = cv2.equalizeHist(gray)
        
            clahe = cv2.createCLAHE(
                clipLimit=2.0,
                tileGridSize=(8, 8)
            )
        
            clahe_image = clahe.apply(gray)
        
            cv2.imshow("Original Gray", gray)
            cv2.imshow("Histogram Equalization", equalized)
            cv2.imshow("CLAHE", clahe_image)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. clipLimit를 너무 크게 설정
        
        clipLimit가 너무 크면 노이즈와 작은 밝기 변화가 과도하게 강조될 수 있습니다.
        
        처음에는 다음 값으로 시작하는 것이 좋습니다.
        
        ```
        clipLimit=2.0
        ```
        
        ---
        
        ### 실수 2. 컬러 이미지에 무작정 CLAHE 적용
        
        컬러 이미지에 CLAHE를 적용하려면 보통 YCrCb 또는 LAB 색상 공간의 밝기 채널에 적용합니다.
        
        초보 단계에서는 Grayscale에 적용하는 방식부터 익히는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        CLAHE는 조명이 불균일한 환경에서 유용합니다.
        
        ```
        복도 한쪽은 밝고 한쪽은 어두움
        공장 조명이 부분적으로 반사됨
        바닥 일부가 그림자에 가려짐
        ```
        
        이런 상황에서 라인 검출이나 Edge 검출 전처리에 도움이 될 수 있습니다.
        
        ---
        
        # 예제 74. Template Matching
        
        ## 핵심 주제
        
        Template Matching은 작은 템플릿 이미지를 큰 이미지 안에서 찾는 방법입니다.
        
        예를 들어 카메라 이미지 안에서 특정 마커, 로고, 버튼 모양을 찾을 때 사용할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 템플릿 매칭 개념 이해
        2. cv2.matchTemplate() 사용법 이해
        3. 가장 유사한 위치 찾기
        4. 검출 위치에 사각형 그리기
        ```
        
        ---
        
        ## 준비 파일
        
        ```
        practice_images/scene.jpg
        practice_images/template.jpg
        ```
        
        `scene.jpg`는 전체 장면 이미지이고, `template.jpg`는 그 안에서 찾을 작은 이미지입니다.
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        scene_path = "practice_images/scene.jpg"
        template_path = "practice_images/template.jpg"
        
        scene = cv2.imread(scene_path)
        template = cv2.imread(template_path)
        
        if scene is None or template is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        
            result = cv2.matchTemplate(
                scene_gray,
                template_gray,
                cv2.TM_CCOEFF_NORMED
            )
        
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
            template_height, template_width = template_gray.shape[:2]
        
            top_left = max_loc
            bottom_right = (
                top_left[0] + template_width,
                top_left[1] + template_height
            )
        
            output = scene.copy()
        
            cv2.rectangle(
                output,
                top_left,
                bottom_right,
                (0, 0, 255),
                2
            )
        
            print("최고 유사도:", max_val)
            print("검출 위치:", top_left)
        
            cv2.imshow("Template", template)
            cv2.imshow("Matched Result", output)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 크기나 회전이 달라진 객체에 그대로 사용
        
        Template Matching은 템플릿과 대상의 크기, 회전, 형태가 거의 같을 때 잘 작동합니다.
        
        대상 물체가 커지거나 작아지거나 회전하면 성능이 급격히 떨어질 수 있습니다.
        
        ---
        
        ### 실수 2. 유사도 임계값 없이 무조건 검출했다고 판단
        
        항상 최고 위치는 나오지만, 그것이 진짜 물체라는 보장은 없습니다.
        
        실무에서는 다음처럼 임계값을 둡니다.
        
        ```
        if max_val > 0.8:
            print("검출 성공")
        else:
            print("검출 실패")
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Template Matching은 다음 작업에 사용할 수 있습니다.
        
        ```
        특정 버튼 위치 찾기
        작업대 위 기준 마커 찾기
        로봇이 찾아야 할 단순 패턴 검출
        정해진 위치의 부품 유무 확인
        ```
        
        단, 물체 크기나 회전이 자주 바뀌는 모바일 로봇 환경에서는 특징점 기반 방법이나 딥러닝 검출이 더 적합할 수 있습니다.
        
        ---
        
        # 예제 75. ORB 특징점 검출
        
        ## 핵심 주제
        
        ORB는 이미지에서 특징적인 점을 찾아내는 알고리즘입니다.
        
        특징점은 코너, 모서리, 패턴이 뚜렷한 부분처럼 다른 위치와 구별되는 지점입니다.
        
        ORB는 빠르고 무료로 사용할 수 있어 로봇 비전에서 많이 사용됩니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ORB 객체 생성
        2. 특징점 검출
        3. Descriptor 계산
        4. 이미지 위에 특징점 그리기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=500)
        
            keypoints, descriptors = orb.detectAndCompute(gray, None)
        
            result = cv2.drawKeypoints(
                image,
                keypoints,
                None,
                color=(0, 255, 0),
                flags=0
            )
        
            print("검출된 특징점 개수:", len(keypoints))
        
            if descriptors is not None:
                print("Descriptor shape:", descriptors.shape)
        
            cv2.imshow("ORB Keypoints", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 특징점이 없는 이미지에서 descriptors를 바로 사용
        
        단색 벽이나 흐릿한 이미지에서는 특징점이 거의 없을 수 있습니다.
        
        이때 `descriptors`가 `None`일 수 있으므로 반드시 확인해야 합니다.
        
        ```
        if descriptors is None:
            print("특징점 descriptor가 없습니다.")
        ```
        
        ---
        
        ### 실수 2. 특징점이 많을수록 무조건 좋다고 생각함
        
        특징점이 너무 많으면 계산량이 증가합니다.
        
        실시간 로봇에서는 적절한 개수가 중요합니다.
        
        ```
        orb = cv2.ORB_create(nfeatures=500)
        ```
        
        처음에는 500~1000 정도로 시작하는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ORB 특징점은 다음 분야에 연결됩니다.
        
        ```
        Visual SLAM
        Visual Odometry
        이미지 매칭
        마커 없는 물체 인식
        장면 인식
        ```
        
        로봇이 이동하면서 이전 프레임과 현재 프레임의 특징점을 비교하면 카메라 움직임을 추정할 수 있습니다.
        
        ---
        
        # 예제 76. ORB 특징점 매칭
        
        ## 핵심 주제
        
        두 이미지에서 ORB 특징점을 검출하고, 서로 비슷한 특징점을 매칭합니다.
        
        이미지 매칭은 같은 물체나 같은 장소인지 판단하는 데 사용할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 두 이미지에서 ORB 특징점 검출
        2. Descriptor 매칭
        3. BFMatcher 사용법 이해
        4. 매칭 결과 시각화
        ```
        
        ---
        
        ## 준비 파일
        
        ```
        practice_images/object1.jpg
        practice_images/object2.jpg
        ```
        
        두 이미지는 같은 물체를 다른 각도 또는 거리에서 촬영한 이미지가 좋습니다.
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image1_path = "practice_images/object1.jpg"
        image2_path = "practice_images/object2.jpg"
        
        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        
        if image1 is None or image2 is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=1000)
        
            keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
            keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
        
            if descriptors1 is None or descriptors2 is None:
                print("특징점 descriptor가 부족합니다.")
            else:
                matcher = cv2.BFMatcher(
                    cv2.NORM_HAMMING,
                    crossCheck=True
                )
        
                matches = matcher.match(descriptors1, descriptors2)
        
                matches = sorted(matches, key=lambda x: x.distance)
        
                good_matches = matches[:50]
        
                result = cv2.drawMatches(
                    image1,
                    keypoints1,
                    image2,
                    keypoints2,
                    good_matches,
                    None,
                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
                )
        
                print("전체 매칭 개수:", len(matches))
                print("표시한 좋은 매칭 개수:", len(good_matches))
        
                cv2.imshow("ORB Matching", result)
        
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. ORB descriptor에 L2 거리 사용
        
        SIFT 같은 실수형 descriptor는 L2를 쓰지만, ORB는 이진 descriptor이므로 Hamming 거리를 사용해야 합니다.
        
        ```
        cv2.NORM_HAMMING
        ```
        
        ---
        
        ### 실수 2. 매칭 개수만 보고 같은 물체라고 판단
        
        매칭 개수가 많다고 반드시 같은 물체는 아닙니다.
        
        잘못된 매칭도 포함될 수 있습니다.
        
        실무에서는 거리 기준, RANSAC, Homography 검증 등을 추가합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ORB 매칭은 다음 작업에 사용할 수 있습니다.
        
        ```
        로봇이 이전에 본 장소인지 판단
        특정 패턴 물체 재인식
        카메라 이동량 추정
        Visual SLAM 특징점 매칭
        ```
        
        ROS2에서 카메라 프레임 간 특징점을 매칭하면 로봇의 시각적 움직임 추정으로 확장할 수 있습니다.
        
        ---
        
        # 예제 77. 이미지 유사도 비교
        
        ## 핵심 주제
        
        두 이미지가 얼마나 비슷한지 ORB 특징점 매칭 개수를 기준으로 간단히 판단합니다.
        
        완벽한 유사도 알고리즘은 아니지만, 초보자가 이미지 매칭 개념을 이해하기에 좋습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ORB 매칭 기반 유사도 개념 이해
        2. 좋은 매칭 개수 계산
        3. 임계값으로 유사/비유사 판단
        4. 간단한 물체 인식 기초 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        def calculate_orb_similarity(image1, image2):
            gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=1000)
        
            keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
            keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
        
            if descriptors1 is None or descriptors2 is None:
                return 0
        
            matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
            matches = matcher.match(descriptors1, descriptors2)
        
            good_matches = [
                match for match in matches if match.distance < 50
            ]
        
            return len(good_matches)
        
        image1_path = "practice_images/object1.jpg"
        image2_path = "practice_images/object2.jpg"
        
        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        
        if image1 is None or image2 is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            similarity_score = calculate_orb_similarity(image1, image2)
        
            print("ORB 유사도 점수:", similarity_score)
        
            if similarity_score > 30:
                print("두 이미지는 비슷한 물체일 가능성이 높습니다.")
            else:
                print("두 이미지는 다른 물체일 가능성이 높습니다.")
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. threshold 값을 모든 이미지에 동일하게 사용
        
        ```
        if similarity_score > 30:
        ```
        
        이 값은 실습용 기준입니다.
        
        이미지 크기, 특징점 수, 물체 패턴에 따라 적절한 기준은 달라집니다.
        
        ---
        
        ### 실수 2. 단색 물체에 ORB 유사도를 적용
        
        ORB는 코너나 패턴이 많은 이미지에서 잘 작동합니다.
        
        단색 공, 단색 박스처럼 특징점이 적은 물체에는 적합하지 않을 수 있습니다.
        
        이런 경우 색상 기반 검출이나 딥러닝 검출이 더 낫습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        로봇이 현재 보고 있는 물체가 기준 이미지와 같은지 판단할 때 사용할 수 있습니다.
        
        ```
        기준 부품 이미지
        현재 카메라 프레임의 ROI
        → ORB 유사도 비교
        → 같은 부품인지 판단
        ```
        
        단, 실제 프로젝트에서는 조명과 회전, 스케일 변화에 대한 검증이 추가로 필요합니다.
        
        ---
        
        # 예제 78. Feature Matching 시각화
        
        ## 핵심 주제
        
        Feature Matching 결과를 보기 좋게 시각화합니다.
        
        단순히 매칭 개수만 보는 것이 아니라, 실제로 어떤 점들이 연결되었는지 확인해야 잘못된 매칭을 찾을 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ORB 특징점 매칭 복습
        2. 좋은 매칭만 선별
        3. cv2.drawMatches() 활용
        4. 잘못된 매칭을 눈으로 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        image1_path = "practice_images/object1.jpg"
        image2_path = "practice_images/object2.jpg"
        
        image1 = cv2.imread(image1_path)
        image2 = cv2.imread(image2_path)
        
        if image1 is None or image2 is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=1000)
        
            keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
            keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
        
            if descriptors1 is None or descriptors2 is None:
                print("특징점 descriptor가 부족합니다.")
            else:
                matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                matches = matcher.match(descriptors1, descriptors2)
        
                matches = sorted(matches, key=lambda x: x.distance)
        
                good_matches = [
                    match for match in matches
                    if match.distance < 50
                ]
        
                good_matches = good_matches[:50]
        
                match_image = cv2.drawMatches(
                    image1,
                    keypoints1,
                    image2,
                    keypoints2,
                    good_matches,
                    None,
                    matchColor=(0, 255, 0),
                    singlePointColor=(255, 0, 0),
                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
                )
        
                print("좋은 매칭 개수:", len(good_matches))
        
                cv2.imshow("Feature Matching Visualization", match_image)
        
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 매칭 선이 많으면 좋은 결과라고 착각
        
        매칭 선이 많아도 잘못 연결된 선이 많으면 신뢰할 수 없습니다.
        
        시각화로 선이 자연스럽게 연결되는지 확인해야 합니다.
        
        ---
        
        ### 실수 2. 모든 매칭을 다 그림
        
        전체 매칭을 모두 그리면 화면이 복잡해지고 판단이 어렵습니다.
        
        좋은 매칭 일부만 표시하는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서 특징점 기반 위치 추정이나 물체 인식을 디버깅할 때 매칭 시각화는 매우 중요합니다.
        
        ```
        현재 프레임
        기준 이미지
        → 특징점 매칭
        → 시각화 이미지 발행
        → rqt_image_view 또는 RViz2로 확인
        ```
        
        알고리즘이 실패하는 이유를 눈으로 확인할 수 있습니다.
        
        ---
        
        # 예제 79. 간단한 물체 인식
        
        ## 핵심 주제
        
        기준 이미지와 현재 이미지의 특징점 매칭을 이용해 물체가 있는지 판단합니다.
        
        이번 예제는 물체 인식의 매우 기초적인 형태입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 기준 이미지와 장면 이미지 비교
        2. ORB 매칭 기반 물체 존재 여부 판단
        3. 좋은 매칭 개수 기준 적용
        4. 인식 결과 표시
        ```
        
        ---
        
        ## 준비 파일
        
        ```
        practice_images/reference_object.jpg
        practice_images/scene_with_object.jpg
        ```
        
        `reference_object.jpg`는 찾고 싶은 물체 이미지입니다.
        
        `scene_with_object.jpg`는 그 물체가 포함된 장면 이미지입니다.
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        reference_path = "practice_images/reference_object.jpg"
        scene_path = "practice_images/scene_with_object.jpg"
        
        reference = cv2.imread(reference_path)
        scene = cv2.imread(scene_path)
        
        if reference is None or scene is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
            scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=1500)
        
            ref_keypoints, ref_descriptors = orb.detectAndCompute(ref_gray, None)
            scene_keypoints, scene_descriptors = orb.detectAndCompute(scene_gray, None)
        
            if ref_descriptors is None or scene_descriptors is None:
                print("특징점 descriptor가 부족합니다.")
            else:
                matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
                matches = matcher.match(ref_descriptors, scene_descriptors)
        
                good_matches = [
                    match for match in matches
                    if match.distance < 50
                ]
        
                print("좋은 매칭 개수:", len(good_matches))
        
                output = scene.copy()
        
                if len(good_matches) > 30:
                    result_text = "Object Detected"
                    color = (0, 255, 0)
                else:
                    result_text = "Object Not Detected"
                    color = (0, 0, 255)
        
                cv2.putText(
                    output,
                    result_text,
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    color,
                    2
                )
        
                match_view = cv2.drawMatches(
                    reference,
                    ref_keypoints,
                    scene,
                    scene_keypoints,
                    sorted(good_matches, key=lambda x: x.distance)[:50],
                    None,
                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
                )
        
                cv2.imshow("Recognition Result", output)
                cv2.imshow("Matching View", match_view)
        
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 물체 위치까지 찾았다고 착각
        
        이 예제는 물체가 있을 가능성을 판단하는 기초 예제입니다.
        
        정확한 물체 위치 영역을 찾으려면 Homography를 이용해 기준 이미지의 사각형을 장면 이미지에 투영해야 합니다.
        
        ---
        
        ### 실수 2. 패턴이 없는 물체에 적용
        
        ORB 기반 인식은 다음 물체에 약합니다.
        
        ```
        단색 공
        반짝이는 금속
        투명 물체
        무늬 없는 박스
        흐릿한 이미지
        ```
        
        이런 경우 색상 검출, 모양 검출, 딥러닝 검출을 고려해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2에서 기준 물체 인식 노드를 만들 때 사용할 수 있습니다.
        
        ```
        기준 이미지 로드
        /camera/image_raw 수신
        현재 프레임과 ORB 매칭
        매칭 개수 기준으로 물체 존재 판단
        /object_detected Topic 발행
        ```
        
        ---
        
        # 예제 80. 로봇 비전에서 특징점 활용
        
        ## 핵심 주제
        
        특징점 매칭 결과를 로봇 비전 관점에서 사용할 수 있도록 구조화합니다.
        
        이번 예제에서는 카메라 프레임에서 기준 이미지와 매칭되는 정도를 계산하고, 결과를 딕셔너리로 정리합니다.
        
        ROS2 Topic으로 발행하기 좋은 형태입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 기준 이미지 특징점 미리 계산
        2. 현재 프레임 특징점 계산
        3. 좋은 매칭 개수 계산
        4. ROS2 메시지 변환 준비
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        def create_reference_features(reference_image):
            gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
        
            orb = cv2.ORB_create(nfeatures=1000)
        
            keypoints, descriptors = orb.detectAndCompute(gray, None)
        
            return orb, keypoints, descriptors
        
        def match_with_reference(frame, orb, reference_descriptors):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            keypoints, descriptors = orb.detectAndCompute(gray, None)
        
            result = {
                "detected": False,
                "good_match_count": 0,
                "total_match_count": 0
            }
        
            if reference_descriptors is None or descriptors is None:
                return result
        
            matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
            matches = matcher.match(reference_descriptors, descriptors)
        
            good_matches = [
                match for match in matches
                if match.distance < 50
            ]
        
            result["good_match_count"] = int(len(good_matches))
            result["total_match_count"] = int(len(matches))
        
            if len(good_matches) > 30:
                result["detected"] = True
        
            return result
        
        reference_path = "practice_images/reference_object.jpg"
        
        reference_image = cv2.imread(reference_path)
        
        if reference_image is None:
            print("기준 이미지를 읽을 수 없습니다.")
        else:
            orb, reference_keypoints, reference_descriptors = create_reference_features(
                reference_image
            )
        
            cap = cv2.VideoCapture(0)
        
            if not cap.isOpened():
                print("카메라를 열 수 없습니다.")
            else:
                while True:
                    ret, frame = cap.read()
        
                    if not ret:
                        print("프레임을 읽을 수 없습니다.")
                        break
        
                    match_result = match_with_reference(
                        frame,
                        orb,
                        reference_descriptors
                    )
        
                    if match_result["detected"]:
                        text = "Reference Object Detected"
                        color = (0, 255, 0)
                    else:
                        text = "Not Detected"
                        color = (0, 0, 255)
        
                    cv2.putText(
                        frame,
                        text,
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        color,
                        2
                    )
        
                    cv2.putText(
                        frame,
                        f"Good Matches: {match_result['good_match_count']}",
                        (20, 75),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2
                    )
        
                    print("ROS2 Topic으로 보낼 매칭 결과:", match_result)
        
                    cv2.imshow("Robot Vision Feature Matching", frame)
        
                    if cv2.waitKey(1) == ord('q'):
                        break
        
                cap.release()
                cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 기준 이미지 특징점을 매 프레임 계산
        
        기준 이미지는 변하지 않으므로 한 번만 계산해야 합니다.
        
        나쁜 구조:
        
        ```
        매 프레임마다 기준 이미지 로드
        매 프레임마다 기준 이미지 ORB 계산
        ```
        
        좋은 구조:
        
        ```
        시작 시 기준 이미지 ORB 계산
        매 프레임에서는 현재 프레임만 ORB 계산
        ```
        
        ---
        
        ### 실수 2. detected만 발행하고 신뢰도 정보를 보내지 않음
        
        실무에서는 True/False만 보내면 디버깅이 어렵습니다.
        
        다음 정보를 함께 보내는 것이 좋습니다.
        
        ```
        detected
        good_match_count
        total_match_count
        threshold
        timestamp
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제의 결과 구조는 ROS2 메시지로 바꾸기 쉽습니다.
        
        ```
        {
          "detected": true,
          "good_match_count": 42,
          "total_match_count": 128
        }
        ```
        
        간단한 실습에서는 `std_msgs/String`으로 JSON 문자열을 발행할 수 있고, 정식 프로젝트에서는 커스텀 메시지를 만드는 것이 좋습니다.
        
        예상 ROS2 흐름은 다음과 같습니다.
        
        ```
        reference_object.jpg 로드
        → 기준 특징점 계산
        → /camera/image_raw Subscribe
        → 현재 프레임 특징점 계산
        → 기준 특징점과 매칭
        → detected, good_match_count 발행
        ```
        
        ---
        
        # 8단계 핵심 정리
        
        이번 8단계에서는 색상 기반 검출을 넘어 **패턴, 특징점, 이미지 유사도**를 다루었습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 71 | 이미지 히스토그램 |
        | 72 | 히스토그램 평활화 |
        | 73 | CLAHE |
        | 74 | Template Matching |
        | 75 | ORB 특징점 검출 |
        | 76 | ORB 특징점 매칭 |
        | 77 | 이미지 유사도 비교 |
        | 78 | Feature Matching 시각화 |
        | 79 | 간단한 물체 인식 |
        | 80 | 로봇 비전에서 특징점 활용 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        ```
        
        이미지 밝기 히스토그램을 계산합니다.
        
        ```
        equalized = cv2.equalizeHist(gray)
        ```
        
        흑백 이미지의 대비를 개선합니다.
        
        ```
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_image = clahe.apply(gray)
        ```
        
        CLAHE로 부분 대비를 개선합니다.
        
        ```
        result = cv2.matchTemplate(scene_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        ```
        
        템플릿 매칭으로 가장 유사한 위치를 찾습니다.
        
        ```
        orb = cv2.ORB_create(nfeatures=1000)
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        ```
        
        ORB 특징점과 descriptor를 계산합니다.
        
        ```
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(descriptors1, descriptors2)
        ```
        
        ORB descriptor를 매칭합니다.
        
        ```
        matches = sorted(matches, key=lambda x: x.distance)
        ```
        
        좋은 매칭 순서로 정렬합니다.
        
        ```
        match_image = cv2.drawMatches(
            image1,
            keypoints1,
            image2,
            keypoints2,
            good_matches,
            None
        )
        ```
        
        특징점 매칭 결과를 시각화합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        이번 단계는 ROS2 로봇 비전에서 다음 주제와 연결됩니다.
        
        ```
        Visual SLAM
        Visual Odometry
        마커 없는 물체 인식
        기준 이미지 기반 물체 탐색
        작업대 부품 인식
        장면 유사도 판단
        ```
        
        색상 기반 검출이 다음에 적합하다면,
        
        ```
        빨간 공
        파란 표식
        초록 라인
        색상이 뚜렷한 물체
        ```
        
        특징점 기반 검출은 다음에 적합합니다.
        
        ```
        로고가 있는 물체
        무늬가 있는 부품
        패턴이 있는 마커
        책 표지
        기계 부품의 텍스처
        ```
        
        ---
        
        # 실무 기준 선택표
        
        | 상황 | 추천 방법 |
        | --- | --- |
        | 밝기 상태를 분석하고 싶음 | 히스토그램 |
        | 대비가 낮음 | Histogram Equalization |
        | 조명이 고르지 않음 | CLAHE |
        | 동일 크기 패턴을 찾고 싶음 | Template Matching |
        | 회전/시점 변화가 조금 있음 | ORB 특징점 |
        | 두 이미지가 같은 물체인지 비교 | ORB Matching |
        | 매칭 오류를 확인하고 싶음 | drawMatches 시각화 |
        | ROS2 Topic으로 인식 결과 발행 | 결과 dict 구조화 |
        
        ---
        
        # 실무에서 가장 중요한 판단 기준
        
        ```
        색상이 뚜렷하면 HSV 기반 검출이 빠르고 쉽다.
        패턴이 뚜렷하면 ORB 특징점 매칭이 유용하다.
        템플릿 매칭은 크기와 회전 변화에 약하다.
        ORB는 단색 물체에 약하다.
        조명 문제가 있으면 CLAHE나 평활화를 고려한다.
        실시간 ROS2에서는 계산량과 FPS를 반드시 확인한다.
        ```
        
    - 9단계: ROS2 연계를 위한 실전 OpenCV
        
        이번 단계는 지금까지 배운 OpenCV 문법을 **ROS2 Humble 카메라 노드 구조**로 연결하는 핵심 구간입니다.
        
        OpenCV 단독 실습에서는 보통 이렇게 처리했습니다.
        
        ```
        cv2.VideoCapture()
        → frame 읽기
        → OpenCV 처리
        → cv2.imshow()
        ```
        
        ROS2에서는 구조가 다음처럼 바뀝니다.
        
        ```
        /camera/image_raw Subscribe
        → cv_bridge로 ROS2 Image 메시지를 OpenCV frame으로 변환
        → OpenCV 처리
        → 결과 이미지 또는 좌표 Topic Publish
        ```
        
        ---
        
        # 9단계: ROS2 연계를 위한 실전 OpenCV
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 81 | cv_bridge 개념 |
        | 82 | ROS2 Image 메시지 이해 |
        | 83 | OpenCV 이미지를 ROS2 메시지로 변환 |
        | 84 | ROS2 Image 메시지를 OpenCV로 변환 |
        | 85 | 카메라 노드 구조 설계 |
        | 86 | 이미지 Subscriber 구조 |
        | 87 | 실시간 Edge Publisher |
        | 88 | 객체 중심 좌표 Publisher |
        | 89 | 로봇 추종용 비전 노드 |
        | 90 | OpenCV + ROS2 디버깅 포인트 |
        
        ---
        
        # 예제 81. cv_bridge 개념
        
        ## 핵심 주제
        
        `cv_bridge`는 ROS2의 `sensor_msgs/Image` 메시지와 OpenCV 이미지 배열을 서로 변환해 주는 도구입니다.
        
        ROS2 카메라 Topic은 일반 Python NumPy 배열이 아니라 ROS2 메시지 형식입니다.
        
        따라서 OpenCV로 처리하려면 변환이 필요합니다.
        
        ```
        ROS2 Image 메시지
        → cv_bridge
        → OpenCV 이미지, 즉 NumPy 배열
        ```
        
        반대로 OpenCV 처리 결과를 다시 ROS2 Topic으로 보내려면 다음 변환이 필요합니다.
        
        ```
        OpenCV 이미지
        → cv_bridge
        → ROS2 Image 메시지
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv_bridge가 필요한 이유 이해
        2. ROS2 Image와 OpenCV frame 차이 이해
        3. imgmsg_to_cv2() 개념 이해
        4. cv2_to_imgmsg() 개념 이해
        ```
        
        ---
        
        ## 핵심 개념 코드
        
        ```python
        from cv_bridge import CvBridge
        
        bridge = CvBridge()
        
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        
        ros_image_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. encoding을 확인하지 않음
        
        ROS2 카메라 메시지는 다음 encoding을 가질 수 있습니다.
        
        ```
        bgr8
        rgb8
        mono8
        ```
        
        OpenCV는 기본적으로 BGR을 많이 사용합니다.
        
        색상이 이상하게 보이면 encoding 문제를 먼저 확인해야 합니다.
        
        ---
        
        ### 실수 2. ROS2 메시지를 OpenCV 함수에 바로 넣음
        
        다음 코드는 잘못된 방식입니다.
        
        ```
        cv2.imshow("camera", msg)
        ```
        
        `msg`는 OpenCV 이미지가 아니라 ROS2 메시지입니다.
        
        반드시 변환해야 합니다.
        
        ```
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        cv2.imshow("camera", frame)
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 비전 노드의 기본 구조는 대부분 다음과 같습니다.
        
        ```
        Image Subscriber
        → cv_bridge 변환
        → OpenCV 처리
        → 결과 Publish
        ```
        
        따라서 `cv_bridge`는 ROS2와 OpenCV를 연결하는 핵심 다리입니다.
        
        ---
        
        # 예제 82. ROS2 Image 메시지 이해
        
        ## 핵심 주제
        
        ROS2에서 카메라 이미지는 `sensor_msgs/msg/Image` 메시지로 전달됩니다.
        
        이 메시지에는 실제 이미지 데이터뿐 아니라 이미지 크기, 인코딩, 시간 정보 등이 포함됩니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. sensor_msgs/Image 구조 이해
        2. height, width, encoding 의미 이해
        3. header timestamp 이해
        4. OpenCV 이미지와 차이 이해
        ```
        
        ---
        
        ## ROS2 Image 메시지 주요 필드
        
        ```
        header
        height
        width
        encoding
        is_bigendian
        step
        data
        ```
        
        ---
        
        ## 필드별 설명
        
        ```
        header
        ```
        
        메시지의 시간과 좌표계 정보를 담습니다.
        
        카메라 프레임이 언제 생성되었는지 확인할 때 중요합니다.
        
        ---
        
        ```
        height
        ```
        
        이미지 높이입니다.
        
        OpenCV의 `frame.shape[0]`에 해당합니다.
        
        ---
        
        ```
        width
        ```
        
        이미지 너비입니다.
        
        OpenCV의 `frame.shape[1]`에 해당합니다.
        
        ---
        
        ```
        encoding
        ```
        
        이미지 픽셀 형식을 의미합니다.
        
        대표적으로 다음이 있습니다.
        
        ```
        bgr8
        rgb8
        mono8
        ```
        
        ---
        
        ```
        step
        ```
        
        이미지 한 줄이 차지하는 바이트 수입니다.
        
        일반적으로 컬러 이미지에서는 대략 다음과 비슷합니다.
        
        ```
        step = width × 채널 수
        ```
        
        ---
        
        ```
        data
        ```
        
        실제 이미지 픽셀 데이터입니다.
        
        하지만 이 데이터는 그대로 OpenCV에서 다루기 어렵기 때문에 `cv_bridge`를 사용합니다.
        
        ---
        
        ## 메시지 정보 출력 예제
        
        ```
        def image_callback(msg):
            print("height:", msg.height)
            print("width:", msg.width)
            print("encoding:", msg.encoding)
            print("step:", msg.step)
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. width와 height 순서 혼동
        
        ROS2 메시지는 `height`, `width` 필드가 따로 있습니다.
        
        OpenCV shape는 다음 순서입니다.
        
        ```
        height, width, channels = frame.shape
        ```
        
        하지만 좌표를 다룰 때는 보통 다음 순서입니다.
        
        ```
        x, y
        ```
        
        초보자가 가장 많이 헷갈리는 부분입니다.
        
        ---
        
        ### 실수 2. encoding을 무시하고 변환
        
        카메라가 `rgb8`로 보내는데 `bgr8`로 해석하면 색상이 바뀔 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        카메라 노드 디버깅 시 가장 먼저 확인할 것은 다음입니다.
        
        ```
        Topic 이름이 맞는가?
        Image 메시지가 들어오는가?
        width, height가 예상과 맞는가?
        encoding이 bgr8인지 rgb8인지 mono8인지?
        ```
        
        ---
        
        # 예제 83. OpenCV 이미지를 ROS2 메시지로 변환
        
        ## 핵심 주제
        
        OpenCV에서 처리한 이미지를 ROS2 Image Topic으로 발행할 수 있도록 메시지로 변환합니다.
        
        예를 들어 다음 이미지를 ROS2로 보낼 수 있습니다.
        
        ```
        원본 카메라 이미지
        Edge 결과 이미지
        색상 마스크 이미지
        객체 박스가 그려진 이미지
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. cv2_to_imgmsg() 사용법 이해
        2. OpenCV 이미지 encoding 설정
        3. ROS2 Image Publisher 구조 이해
        4. 처리 결과 이미지를 Topic으로 발행하는 개념 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from cv_bridge import CvBridge
        import cv2
        
        class OpenCVImagePublisher(Node):
            def __init__(self):
                super().__init__("opencv_image_publisher")
        
                self.publisher = self.create_publisher(
                    Image,
                    "/opencv/image",
                    10
                )
        
                self.bridge = CvBridge()
        
                self.timer = self.create_timer(
                    0.1,
                    self.timer_callback
                )
        
                self.image = cv2.imread("practice_images/sample.jpg")
        
            def timer_callback(self):
                if self.image is None:
                    self.get_logger().error("이미지를 읽을 수 없습니다.")
                    return
        
                msg = self.bridge.cv2_to_imgmsg(
                    self.image,
                    encoding="bgr8"
                )
        
                self.publisher.publish(msg)
        
                self.get_logger().info("OpenCV 이미지를 ROS2 Image로 발행했습니다.")
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = OpenCVImagePublisher()
        
            rclpy.spin(node)
        
            node.destroy_node()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. encoding을 잘못 설정
        
        흑백 이미지를 발행하면서 `bgr8`로 설정하면 문제가 생길 수 있습니다.
        
        흑백 이미지는 보통 다음처럼 발행합니다.
        
        ```
        msg = bridge.cv2_to_imgmsg(gray_image, encoding="mono8")
        ```
        
        컬러 이미지는 보통 다음입니다.
        
        ```
        msg = bridge.cv2_to_imgmsg(color_image, encoding="bgr8")
        ```
        
        ---
        
        ### 실수 2. 이미지 경로를 ROS2 실행 위치 기준으로 잘못 작성
        
        ROS2 패키지에서 실행할 때 현재 작업 디렉토리가 예상과 다를 수 있습니다.
        
        실무에서는 패키지 경로를 기준으로 이미지 파일을 찾는 구조를 쓰는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 OpenCV 처리 결과를 RViz2나 `rqt_image_view`에서 확인할 때 필요합니다.
        
        ```
        OpenCV 처리 결과
        → cv2_to_imgmsg()
        → /processed_image Publish
        → rqt_image_view에서 확인
        ```
        
        ---
        
        # 예제 84. ROS2 Image 메시지를 OpenCV로 변환
        
        ## 핵심 주제
        
        ROS2 카메라 Topic을 구독하고, 수신한 Image 메시지를 OpenCV 이미지로 변환합니다.
        
        이 구조가 ROS2 비전 노드의 기본입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ROS2 Image Subscriber 생성
        2. imgmsg_to_cv2() 사용법 이해
        3. OpenCV 화면 출력
        4. 카메라 Topic 처리 구조 이해
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from cv_bridge import CvBridge
        import cv2
        
        class ImageSubscriber(Node):
            def __init__(self):
                super().__init__("image_subscriber")
        
                self.subscription = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
                self.bridge = CvBridge()
        
            def image_callback(self, msg):
                frame = self.bridge.imgmsg_to_cv2(
                    msg,
                    desired_encoding="bgr8"
                )
        
                cv2.imshow("ROS2 Camera Image", frame)
                cv2.waitKey(1)
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = ImageSubscriber()
        
            rclpy.spin(node)
        
            node.destroy_node()
            cv2.destroyAllWindows()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Topic 이름이 다름
        
        카메라 Topic 이름은 환경에 따라 다를 수 있습니다.
        
        먼저 다음 명령으로 확인합니다.
        
        ```
        ros2 topic list
        ```
        
        그리고 Image Topic 정보를 확인합니다.
        
        ```
        ros2 topic info /camera/image_raw
        ```
        
        ---
        
        ### 실수 2. cv2.waitKey(1)을 빼먹음
        
        `cv2.imshow()`를 사용하면 `cv2.waitKey(1)`이 필요합니다.
        
        없으면 창이 갱신되지 않거나 멈춘 것처럼 보일 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 앞으로 만들 모든 ROS2 OpenCV 노드의 출발점입니다.
        
        ```
        Image Subscribe
        → cv_bridge 변환
        → OpenCV 처리
        ```
        
        ---
        
        # 예제 85. 카메라 노드 구조 설계
        
        ## 핵심 주제
        
        ROS2에서 OpenCV 카메라 처리 노드를 만들 때는 기능을 구조적으로 나누어야 합니다.
        
        초보자는 모든 코드를 콜백 안에 넣는 경우가 많습니다.
        
        하지만 실무에서는 다음처럼 역할을 분리하는 것이 좋습니다.
        
        ```
        입력 수신
        변환
        처리
        결과 생성
        발행
        디버깅 표시
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. ROS2 비전 노드 기본 구조 이해
        2. image_callback 역할 이해
        3. process_frame() 함수 분리
        4. publish_result() 함수 분리
        ```
        
        ---
        
        ## 권장 구조
        
        ```python
        class VisionNode(Node):
            def __init__(self):
                self.bridge = CvBridge()
                self.image_sub = ...
                self.image_pub = ...
                self.result_pub = ...
        
            def image_callback(self, msg):
                frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                processed_frame, result = self.process_frame(frame)
                self.publish_image(processed_frame)
                self.publish_result(result)
        
            def process_frame(self, frame):
                # OpenCV 처리
                return processed_frame, result
        
            def publish_image(self, processed_frame):
                # 처리 이미지 발행
                pass
        
            def publish_result(self, result):
                # 좌표, 상태 등 발행
                pass
        ```
        
        ---
        
        ## 구조별 설명
        
        ```
        def image_callback(self, msg):
        ```
        
        ROS2 메시지를 받는 입구입니다.
        
        이 함수는 너무 복잡해지지 않도록 관리하는 것이 좋습니다.
        
        ---
        
        ```
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        ```
        
        ROS2 Image를 OpenCV frame으로 변환합니다.
        
        ---
        
        ```
        processed_frame, result = self.process_frame(frame)
        ```
        
        OpenCV 처리 로직은 별도 함수로 분리합니다.
        
        예를 들어 다음 작업이 들어갈 수 있습니다.
        
        ```
        Grayscale
        Gaussian Blur
        Canny Edge
        HSV 색상 검출
        Contour
        중심 좌표 계산
        ```
        
        ---
        
        ```
        self.publish_image(processed_frame)
        ```
        
        처리된 이미지를 ROS2 Topic으로 발행합니다.
        
        ---
        
        ```
        self.publish_result(result)
        ```
        
        객체 중심 좌표, 검출 여부, 면적 같은 결과를 별도 Topic으로 발행합니다.
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 콜백 함수가 너무 커짐
        
        나쁜 구조는 다음과 같습니다.
        
        ```
        image_callback 안에
        변환
        전처리
        검출
        좌표 계산
        이미지 발행
        문자열 발행
        로그
        디버깅 표시
        전부 들어감
        ```
        
        이렇게 되면 오류가 났을 때 어디가 문제인지 찾기 어렵습니다.
        
        ---
        
        ### 실수 2. OpenCV 코드와 ROS2 코드를 분리하지 않음
        
        OpenCV 처리 함수는 가능하면 ROS2 없이도 테스트 가능하게 만드는 것이 좋습니다.
        
        ```
        def detect_object(frame):
            return result
        ```
        
        이렇게 만들면 카메라 파일, 웹캠, ROS2 Topic 어디서든 재사용할 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        실무 ROS2 비전 노드는 보통 다음 Topic을 가집니다.
        
        ```
        Subscribe:
          /camera/image_raw
        
        Publish:
          /vision/processed_image
          /vision/target_center
          /vision/detection_status
        ```
        
        ---
        
        # 예제 86. 이미지 Subscriber 구조
        
        ## 핵심 주제
        
        카메라 Topic을 구독하고 OpenCV로 변환한 뒤, 처리 함수로 넘기는 기본 구조를 만듭니다.
        
        이번 예제는 아직 복잡한 검출을 하지 않고, 구조를 안정적으로 잡는 데 집중합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ROS2 Image Subscriber 작성
        2. cv_bridge 변환
        3. process_frame() 함수 분리
        4. OpenCV 결과 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from cv_bridge import CvBridge
        import cv2
        
        class BasicVisionSubscriber(Node):
            def __init__(self):
                super().__init__("basic_vision_subscriber")
        
                self.bridge = CvBridge()
        
                self.image_sub = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
            def image_callback(self, msg):
                try:
                    frame = self.bridge.imgmsg_to_cv2(
                        msg,
                        desired_encoding="bgr8"
                    )
        
                    processed_frame = self.process_frame(frame)
        
                    cv2.imshow("Processed Frame", processed_frame)
                    cv2.waitKey(1)
        
                except Exception as e:
                    self.get_logger().error(f"이미지 처리 오류: {e}")
        
            def process_frame(self, frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
                processed_frame = cv2.cvtColor(
                    gray,
                    cv2.COLOR_GRAY2BGR
                )
        
                return processed_frame
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = BasicVisionSubscriber()
        
            rclpy.spin(node)
        
            node.destroy_node()
            cv2.destroyAllWindows()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 예외 처리를 하지 않음
        
        카메라 메시지 변환 중 오류가 나면 노드가 종료될 수 있습니다.
        
        실무 노드에서는 최소한 콜백 내부에 예외 처리를 넣는 것이 좋습니다.
        
        ---
        
        ### 실수 2. 흑백 이미지를 그대로 컬러 그리기 함수에 사용
        
        흑백 이미지에 컬러 텍스트나 박스를 그리면 기대와 다를 수 있습니다.
        
        결과 시각화가 필요하면 다시 BGR로 변환하는 것이 좋습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 구조를 기반으로 이후 Edge Publisher, 객체 중심 Publisher를 만들 수 있습니다.
        
        ---
        
        # 예제 87. 실시간 Edge Publisher
        
        ## 핵심 주제
        
        ROS2 카메라 이미지를 구독하고, Canny Edge를 적용한 결과 이미지를 다시 ROS2 Topic으로 발행합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Image Subscriber와 Publisher 동시 사용
        2. Canny Edge 처리
        3. mono8 이미지 발행
        4. rqt_image_view로 결과 확인 가능한 구조 만들기
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from cv_bridge import CvBridge
        import cv2
        
        class EdgePublisher(Node):
            def __init__(self):
                super().__init__("edge_publisher")
        
                self.bridge = CvBridge()
        
                self.image_sub = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
                self.edge_pub = self.create_publisher(
                    Image,
                    "/vision/edge_image",
                    10
                )
        
            def image_callback(self, msg):
                try:
                    frame = self.bridge.imgmsg_to_cv2(
                        msg,
                        desired_encoding="bgr8"
                    )
        
                    edge_image = self.process_frame(frame)
        
                    edge_msg = self.bridge.cv2_to_imgmsg(
                        edge_image,
                        encoding="mono8"
                    )
        
                    edge_msg.header = msg.header
        
                    self.edge_pub.publish(edge_msg)
        
                except Exception as e:
                    self.get_logger().error(f"Edge 처리 오류: {e}")
        
            def process_frame(self, frame):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
                edges = cv2.Canny(blurred, 50, 150)
        
                return edges
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = EdgePublisher()
        
            rclpy.spin(node)
        
            node.destroy_node()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 실행 후 확인 명령
        
        ```
        ros2 topic list
        ```
        
        ```
        ros2 topic echo /vision/edge_image --once
        ```
        
        이미지는 `rqt_image_view`에서 보는 것이 편합니다.
        
        ```
        rqt_image_view
        ```
        
        선택 Topic:
        
        ```
        /vision/edge_image
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. Edge 이미지를 bgr8로 발행
        
        Canny 결과는 1채널 이미지입니다.
        
        따라서 `mono8`으로 발행하는 것이 맞습니다.
        
        ---
        
        ### 실수 2. header를 복사하지 않음
        
        이미지 동기화나 TF 연계가 필요한 경우 header가 중요합니다.
        
        ```
        edge_msg.header = msg.header
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 “처리 이미지 Topic 발행”의 기본입니다.
        
        ```
        원본 카메라
        → OpenCV 처리
        → 결과 이미지 Topic 발행
        → rqt_image_view/RViz2 확인
        ```
        
        ---
        
        # 예제 88. 객체 중심 좌표 Publisher
        
        ## 핵심 주제
        
        카메라 영상에서 색상 객체를 검출하고, 객체 중심 좌표를 ROS2 Topic으로 발행합니다.
        
        간단한 실습에서는 `geometry_msgs/Point`를 사용할 수 있습니다.
        
        ```
        x = center_x
        y = center_y
        z = area 또는 검출 여부 보조값
        ```
        
        정식 프로젝트에서는 커스텀 메시지를 권장하지만, 입문 실습에서는 `Point`가 이해하기 쉽습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 색상 객체 중심점 계산
        2. geometry_msgs/Point 발행
        3. 중심 좌표와 면적을 Topic으로 전달
        4. 로봇 제어 노드와 연결할 준비
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from geometry_msgs.msg import Point
        from cv_bridge import CvBridge
        import cv2
        import numpy as np
        
        class TargetCenterPublisher(Node):
            def __init__(self):
                super().__init__("target_center_publisher")
        
                self.bridge = CvBridge()
        
                self.image_sub = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
                self.center_pub = self.create_publisher(
                    Point,
                    "/vision/target_center",
                    10
                )
        
            def image_callback(self, msg):
                try:
                    frame = self.bridge.imgmsg_to_cv2(
                        msg,
                        desired_encoding="bgr8"
                    )
        
                    target = self.detect_blue_target(frame)
        
                    if target is not None:
                        center_x, center_y, area = target
        
                        point_msg = Point()
                        point_msg.x = float(center_x)
                        point_msg.y = float(center_y)
                        point_msg.z = float(area)
        
                        self.center_pub.publish(point_msg)
        
                        self.get_logger().info(
                            f"target center: x={center_x}, y={center_y}, area={area}"
                        )
        
                except Exception as e:
                    self.get_logger().error(f"객체 중심 처리 오류: {e}")
        
            def detect_blue_target(self, frame):
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_blue = np.array([100, 100, 100])
                upper_blue = np.array([130, 255, 255])
        
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
                kernel = np.ones((5, 5), np.uint8)
        
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, _ = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                if len(contours) == 0:
                    return None
        
                largest_contour = max(contours, key=cv2.contourArea)
        
                area = cv2.contourArea(largest_contour)
        
                if area < 500:
                    return None
        
                moments = cv2.moments(largest_contour)
        
                if moments["m00"] == 0:
                    return None
        
                center_x = int(moments["m10"] / moments["m00"])
                center_y = int(moments["m01"] / moments["m00"])
        
                return center_x, center_y, area
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = TargetCenterPublisher()
        
            rclpy.spin(node)
        
            node.destroy_node()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 확인 명령
        
        ```
        ros2 topic echo /vision/target_center
        ```
        
        예상 출력 예시는 다음과 같습니다.
        
        ```
        x: 312.0
        y: 226.0
        z: 4820.0
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 검출 실패 시 이전 좌표를 계속 사용
        
        객체가 사라졌는데 이전 좌표를 계속 쓰면 로봇이 잘못 움직일 수 있습니다.
        
        검출 실패 상태를 따로 발행하는 것이 좋습니다.
        
        ---
        
        ### 실수 2. Point.z에 면적을 넣고 의미를 문서화하지 않음
        
        실습에서는 편하지만 협업에서는 혼란을 줍니다.
        
        정식 메시지는 다음처럼 만드는 것이 좋습니다.
        
        ```
        bool detected
        float64 center_x
        float64 center_y
        float64 area
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 Topic은 다음 제어 노드가 구독할 수 있습니다.
        
        ```
        /vision/target_center
        → 로봇 주행 제어 노드
        → 화면 중앙과 target x 비교
        → /cmd_vel 발행
        ```
        
        ---
        
        # 예제 89. 로봇 추종용 비전 노드
        
        ## 핵심 주제
        
        색상 객체 중심 좌표를 계산하고, 화면 중앙 대비 오차를 발행합니다.
        
        로봇 추종 제어에서 핵심은 객체 좌표 자체보다 **화면 중앙에서 얼마나 벗어났는지**입니다.
        
        ```
        error_x = center_x - image_center_x
        ```
        
        이 값으로 로봇의 회전 방향을 결정합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 객체 중심 좌표 계산
        2. 화면 중앙 기준선 계산
        3. error_x 계산
        4. error_x를 ROS2 Topic으로 발행
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from geometry_msgs.msg import Point
        from cv_bridge import CvBridge
        import cv2
        import numpy as np
        
        class FollowVisionNode(Node):
            def __init__(self):
                super().__init__("follow_vision_node")
        
                self.bridge = CvBridge()
        
                self.image_sub = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
                self.error_pub = self.create_publisher(
                    Point,
                    "/vision/target_error",
                    10
                )
        
                self.debug_image_pub = self.create_publisher(
                    Image,
                    "/vision/debug_image",
                    10
                )
        
            def image_callback(self, msg):
                try:
                    frame = self.bridge.imgmsg_to_cv2(
                        msg,
                        desired_encoding="bgr8"
                    )
        
                    debug_frame, result = self.process_frame(frame)
        
                    if result is not None:
                        center_x = result["center_x"]
                        center_y = result["center_y"]
                        area = result["area"]
                        error_x = result["error_x"]
        
                        error_msg = Point()
                        error_msg.x = float(error_x)
                        error_msg.y = float(center_y)
                        error_msg.z = float(area)
        
                        self.error_pub.publish(error_msg)
        
                    debug_msg = self.bridge.cv2_to_imgmsg(
                        debug_frame,
                        encoding="bgr8"
                    )
                    debug_msg.header = msg.header
        
                    self.debug_image_pub.publish(debug_msg)
        
                except Exception as e:
                    self.get_logger().error(f"추종 비전 처리 오류: {e}")
        
            def process_frame(self, frame):
                height, width = frame.shape[:2]
                image_center_x = width // 2
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_blue = np.array([100, 100, 100])
                upper_blue = np.array([130, 255, 255])
        
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, _ = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                debug_frame = frame.copy()
        
                cv2.line(
                    debug_frame,
                    (image_center_x, 0),
                    (image_center_x, height),
                    (255, 0, 0),
                    2
                )
        
                if len(contours) == 0:
                    cv2.putText(
                        debug_frame,
                        "Target Not Found",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )
                    return debug_frame, None
        
                largest_contour = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(largest_contour)
        
                if area < 500:
                    return debug_frame, None
        
                moments = cv2.moments(largest_contour)
        
                if moments["m00"] == 0:
                    return debug_frame, None
        
                center_x = int(moments["m10"] / moments["m00"])
                center_y = int(moments["m01"] / moments["m00"])
        
                error_x = center_x - image_center_x
        
                cv2.drawContours(
                    debug_frame,
                    [largest_contour],
                    -1,
                    (0, 255, 0),
                    2
                )
        
                cv2.circle(
                    debug_frame,
                    (center_x, center_y),
                    8,
                    (0, 0, 255),
                    -1
                )
        
                cv2.putText(
                    debug_frame,
                    f"error_x: {error_x}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )
        
                result = {
                    "center_x": center_x,
                    "center_y": center_y,
                    "area": area,
                    "error_x": error_x
                }
        
                return debug_frame, result
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = FollowVisionNode()
        
            rclpy.spin(node)
        
            node.destroy_node()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 제어 노드에서 사용할 수 있는 간단한 로직
        
        ```
        if error_x < -30:
            print("왼쪽으로 회전")
        elif error_x > 30:
            print("오른쪽으로 회전")
        else:
            print("정면 유지")
        ```
        
        실제 `/cmd_vel` 제어에서는 다음처럼 비례 제어로 확장할 수 있습니다.
        
        ```
        angular_z = -0.002 * error_x
        ```
        
        단, 실제 로봇에서는 최대 회전 속도를 제한해야 합니다.
        
        ---
        
        ## 확인 명령
        
        ```
        ros2 topic echo /vision/target_error
        ```
        
        ```
        rqt_image_view
        ```
        
        확인 Topic:
        
        ```
        /vision/debug_image
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. error_x 부호를 반대로 사용
        
        카메라 좌표계와 로봇 회전 방향을 반드시 확인해야 합니다.
        
        로봇이 반대로 돌면 `angular_z` 부호를 바꿔야 합니다.
        
        ---
        
        ### 실수 2. 검출 실패 시 제어 노드가 계속 움직임
        
        비전 노드가 target_error를 발행하지 않는 경우 제어 노드에서 정지하도록 설계해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        이 예제는 실제 객체 추종 로봇의 비전 노드에 가깝습니다.
        
        ```
        비전 노드:
          /camera/image_raw Subscribe
          /vision/target_error Publish
        
        제어 노드:
          /vision/target_error Subscribe
          /cmd_vel Publish
        ```
        
        ---
        
        # 예제 90. OpenCV + ROS2 디버깅 포인트
        
        ## 핵심 주제
        
        ROS2와 OpenCV를 함께 사용할 때 자주 발생하는 문제를 점검하는 방법을 정리합니다.
        
        실무에서는 코드 자체보다 디버깅 능력이 더 중요할 때가 많습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. Topic 확인 방법 이해
        2. Image encoding 확인
        3. cv_bridge 오류 원인 파악
        4. GUI/imshow 문제 대응
        5. FPS와 지연시간 점검
        ```
        
        ---
        
        # 1. Topic 이름 확인
        
        ## 확인 명령
        
        ```
        ros2 topic list
        ```
        
        카메라 Topic이 실제로 무엇인지 확인합니다.
        
        예:
        
        ```
        /camera/image_raw
        /image_raw
        /usb_cam/image_raw
        /color/image_raw
        ```
        
        코드의 Topic 이름이 실제와 다르면 콜백이 실행되지 않습니다.
        
        ---
        
        # 2. Topic 타입 확인
        
        ```
        ros2 topic info /camera/image_raw
        ```
        
        예상 타입:
        
        ```
        Type: sensor_msgs/msg/Image
        ```
        
        타입이 `CompressedImage`라면 `sensor_msgs/Image` Subscriber로는 바로 받을 수 없습니다.
        
        ---
        
        # 3. Image 메시지 수신 확인
        
        ```
        ros2 topic hz /camera/image_raw
        ```
        
        카메라 FPS를 확인합니다.
        
        예:
        
        ```
        average rate: 30.0
        ```
        
        FPS가 너무 낮으면 카메라 드라이버, 해상도, USB 대역폭, 처리 부하를 확인해야 합니다.
        
        ---
        
        # 4. encoding 확인
        
        간단히 콜백에서 출력합니다.
        
        ```
        def image_callback(self, msg):
            self.get_logger().info(f"encoding: {msg.encoding}")
        ```
        
        예상 값:
        
        ```
        bgr8
        rgb8
        mono8
        ```
        
        색상이 이상하면 encoding을 먼저 확인합니다.
        
        ---
        
        # 5. cv_bridge 변환 오류
        
        ## 대표 오류 원인
        
        ```
        잘못된 desired_encoding
        Image 타입이 아닌 Topic 구독
        CompressedImage를 Image처럼 처리
        cv_bridge 미설치
        ```
        
        ---
        
        ## 기본 변환
        
        ```
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        ```
        
        흑백 카메라라면 다음이 필요할 수 있습니다.
        
        ```
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="mono8")
        ```
        
        ---
        
        # 6. imshow 창이 안 뜨는 문제
        
        ## 일반 PC
        
        ```
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        ```
        
        `waitKey(1)`이 없으면 창이 갱신되지 않을 수 있습니다.
        
        ---
        
        ## Docker / WSL2 환경
        
        GUI 설정이 필요할 수 있습니다.
        
        ```
        DISPLAY 환경변수
        X11 Forwarding
        VcXsrv
        권한 설정
        ```
        
        초보자 교육에서는 GUI가 복잡하면 처리 이미지를 Topic으로 발행하고 `rqt_image_view`로 확인하는 것이 더 안정적입니다.
        
        ---
        
        # 7. FPS 확인
        
        ROS2 Topic FPS:
        
        ```
        ros2 topic hz /camera/image_raw
        ```
        
        처리 결과 Topic FPS:
        
        ```
        ros2 topic hz /vision/debug_image
        ```
        
        원본은 30Hz인데 결과가 5Hz라면 OpenCV 처리나 발행 로직이 느린 것입니다.
        
        ---
        
        # 8. 처리 지연 줄이기
        
        ## 권장 방법
        
        ```
        해상도 낮추기
        ROI만 처리
        불필요한 imshow 제거
        큰 커널 필터 줄이기
        Bilateral Filter 남용 금지
        딥러닝 모델 입력 크기 최적화
        ```
        
        ---
        
        # 9. Queue 크기 문제
        
        ```
        self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )
        ```
        
        마지막 인자 `10`은 Queue 크기입니다.
        
        처리가 느린데 Queue가 쌓이면 지연이 커질 수 있습니다.
        
        실시간 제어에서는 최신 프레임 중심 처리가 더 중요합니다.
        
        ---
        
        # 10. 실무 디버깅 순서
        
        문제가 생기면 다음 순서로 확인합니다.
        
        ```
        1. ros2 topic list로 Topic 존재 확인
        2. ros2 topic info로 메시지 타입 확인
        3. ros2 topic hz로 프레임 수신 확인
        4. msg.encoding 출력
        5. cv_bridge 변환 확인
        6. OpenCV 처리 함수만 따로 테스트
        7. 결과 이미지 Topic 발행
        8. rqt_image_view로 결과 확인
        9. 좌표 Topic echo로 수치 확인
        10. 제어 노드와 연결
        ```
        
        ---
        
        # 9단계 핵심 정리
        
        이번 9단계에서는 OpenCV와 ROS2 Humble을 연결하는 핵심 구조를 배웠습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 81 | cv_bridge 개념 |
        | 82 | ROS2 Image 메시지 구조 |
        | 83 | OpenCV 이미지를 ROS2 Image로 변환 |
        | 84 | ROS2 Image를 OpenCV 이미지로 변환 |
        | 85 | 카메라 노드 구조 설계 |
        | 86 | 이미지 Subscriber 기본 구조 |
        | 87 | Edge 결과 이미지 Publisher |
        | 88 | 객체 중심 좌표 Publisher |
        | 89 | 로봇 추종용 비전 노드 |
        | 90 | OpenCV + ROS2 디버깅 포인트 |
        
        ---
        
        # 초보자가 반드시 기억해야 할 핵심 문법
        
        ```
        from cv_bridge import CvBridge
        bridge = CvBridge()
        ```
        
        ROS2 Image와 OpenCV 이미지를 변환하기 위한 기본 준비입니다.
        
        ```
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        ```
        
        ROS2 Image 메시지를 OpenCV 이미지로 변환합니다.
        
        ```
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        ```
        
        OpenCV 컬러 이미지를 ROS2 Image 메시지로 변환합니다.
        
        ```
        msg = bridge.cv2_to_imgmsg(edge_image, encoding="mono8")
        ```
        
        OpenCV 흑백 이미지를 ROS2 Image 메시지로 변환합니다.
        
        ```
        self.create_subscription(Image, "/camera/image_raw", self.image_callback, 10)
        ```
        
        카메라 이미지를 구독합니다.
        
        ```
        self.create_publisher(Image, "/vision/debug_image", 10)
        ```
        
        처리 결과 이미지를 발행합니다.
        
        ```
        self.create_publisher(Point, "/vision/target_center", 10)
        ```
        
        객체 중심 좌표를 발행합니다.
        
        ```
        edge_msg.header = msg.header
        ```
        
        원본 이미지의 시간과 frame 정보를 유지합니다.
        
        ---
        
        # ROS2 Humble 강의 전 관점에서 중요한 이유
        
        이번 단계는 OpenCV 기초 문법을 실제 ROS2 로봇 시스템으로 연결하는 가장 중요한 단계입니다.
        
        ```
        OpenCV 단독 처리
        → ROS2 Image Subscribe
        → cv_bridge 변환
        → OpenCV 처리
        → 결과 Image Publish
        → 좌표 Topic Publish
        → 제어 노드 연결
        ```
        
        이 구조를 이해하면 다음 프로젝트로 확장할 수 있습니다.
        
        ```
        라인 트레이싱 로봇
        색상 공 추종 로봇
        객체 중심 좌표 기반 로봇 팔 제어
        Edge 기반 장애물 검출
        OpenCV + YOLO + ROS2 통합
        RViz2/rqt_image_view 기반 시각화
        ```
        
        ---
        
        # 실무 기준 ROS2 비전 노드 설계 흐름
        
        ```
        1. 카메라 Topic 확인
        2. Image Subscriber 작성
        3. cv_bridge로 OpenCV 변환
        4. OpenCV 처리 함수 분리
        5. 처리 결과 이미지 발행
        6. 객체 좌표 또는 상태 Topic 발행
        7. rqt_image_view로 이미지 확인
        8. ros2 topic echo로 좌표 확인
        9. 제어 노드와 연결
        10. FPS와 지연시간 최적화
        ```
        
    - 10단계: 로봇 실무 프로젝트형
        
        이번 단계는 지금까지 배운 OpenCV 문법을 ROS2 Humble 실무 프로젝트 관점으로 묶는 단계입니다.
        
        핵심 흐름은 다음입니다.
        
        ```
        카메라 영상 입력
        → ROI 설정
        → 색상/밝기/Edge/Contour 처리
        → 객체 중심 좌표 계산
        → 로봇 제어 또는 로봇 팔 작업 좌표로 연결
        → ROS2 Topic 발행 준비
        ```
        
        ---
        
        # 10단계: 로봇 실무 프로젝트형 예제
        
        | 번호 | 핵심 주제 |
        | --- | --- |
        | 91 | 라인 트레이싱 전처리 |
        | 92 | 차선 중심 계산 |
        | 93 | ArUco Marker 검출 |
        | 94 | QR 코드 검출 |
        | 95 | 장애물 색상 검출 |
        | 96 | 작업물 위치 검출 |
        | 97 | 컨베이어 객체 카운팅 |
        | 98 | 로봇 팔 Pick 위치 계산 |
        | 99 | OpenCV + YOLO 연계 준비 |
        | 100 | ROS2 비전 프로젝트 통합 구조 |
        
        ---
        
        # 예제 91. 라인 트레이싱 전처리
        
        ## 핵심 주제
        
        라인 트레이싱 로봇은 카메라 영상에서 바닥의 선을 찾아 따라가는 로봇입니다.
        
        전체 이미지를 모두 처리할 필요는 없습니다.
        
        보통 화면 아래쪽만 보면 충분합니다.
        
        ```
        카메라 프레임
        → 하단 ROI 자르기
        → Grayscale
        → Gaussian Blur
        → Threshold
        → 라인 후보 마스크 생성
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 라인 트레이싱용 ROI 설정
        2. Grayscale 변환
        3. Threshold 이진화
        4. 라인 후보 영역 확인
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                height, width = frame.shape[:2]
        
                roi = frame[int(height * 0.6):height, 0:width]
        
                gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
                ret, binary = cv2.threshold(
                    blurred,
                    100,
                    255,
                    cv2.THRESH_BINARY_INV
                )
        
                cv2.imshow("Original Frame", frame)
                cv2.imshow("Line ROI", roi)
                cv2.imshow("Line Binary", binary)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 전체 이미지를 모두 처리함
        
        전체 이미지를 처리하면 벽, 사람, 조명, 책상 다리 같은 불필요한 영역이 검출될 수 있습니다.
        
        라인 트레이싱은 대부분 하단 ROI만 처리하는 것이 안정적입니다.
        
        ---
        
        ### 실수 2. Threshold 값을 고정하고 모든 환경에서 사용함
        
        바닥 색상과 조명에 따라 `100`이라는 기준값은 달라져야 합니다.
        
        실무에서는 다음 값을 실험합니다.
        
        ```
        80
        100
        120
        150
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 라인 트레이싱 노드는 다음 구조로 확장됩니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → ROI
        → Threshold
        → Contour
        → 라인 중심 계산
        → /cmd_vel 발행
        ```
        
        ---
        
        # 예제 92. 차선 중심 계산
        
        ## 핵심 주제
        
        라인 트레이싱에서 가장 중요한 값은 라인의 중심 x좌표입니다.
        
        화면 중앙과 라인 중심의 차이를 계산하면 로봇이 어느 방향으로 회전해야 하는지 알 수 있습니다.
        
        ```
        error_x = line_center_x - image_center_x
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 라인 Contour 검출
        2. 가장 큰 라인 영역 선택
        3. 라인 중심점 계산
        4. 화면 중앙 대비 오차 계산
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                height, width = frame.shape[:2]
                image_center_x = width // 2
        
                roi_start_y = int(height * 0.6)
                roi = frame[roi_start_y:height, 0:width]
        
                gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
                ret, binary = cv2.threshold(
                    blurred,
                    100,
                    255,
                    cv2.THRESH_BINARY_INV
                )
        
                contours, _ = cv2.findContours(
                    binary,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                cv2.line(
                    frame,
                    (image_center_x, 0),
                    (image_center_x, height),
                    (255, 0, 0),
                    2
                )
        
                if len(contours) > 0:
                    largest_contour = max(contours, key=cv2.contourArea)
                    area = cv2.contourArea(largest_contour)
        
                    if area > 300:
                        moments = cv2.moments(largest_contour)
        
                        if moments["m00"] != 0:
                            line_center_x = int(moments["m10"] / moments["m00"])
                            line_center_y = int(moments["m01"] / moments["m00"])
        
                            line_center_y_on_frame = line_center_y + roi_start_y
        
                            error_x = line_center_x - image_center_x
        
                            cv2.drawContours(
                                roi,
                                [largest_contour],
                                -1,
                                (0, 255, 0),
                                2
                            )
        
                            cv2.circle(
                                frame,
                                (line_center_x, line_center_y_on_frame),
                                8,
                                (0, 0, 255),
                                -1
                            )
        
                            cv2.putText(
                                frame,
                                f"error_x: {error_x}",
                                (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 255, 255),
                                2
                            )
        
                            print("라인 중심:", line_center_x, line_center_y_on_frame)
                            print("화면 중앙 대비 오차:", error_x)
        
                cv2.imshow("Line Center Frame", frame)
                cv2.imshow("Line Binary", binary)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. ROI 좌표 보정을 잊음
        
        ROI에서 계산한 `center_y`는 전체 이미지 기준 좌표가 아닙니다.
        
        전체 이미지 위에 표시하려면 `roi_start_y`를 더해야 합니다.
        
        ---
        
        ### 실수 2. error_x 부호를 로봇 제어에 반대로 사용함
        
        실제 로봇이 반대로 회전하면 제어식의 부호를 바꿔야 합니다.
        
        ```
        angular_z = -0.002 * error_x
        ```
        
        또는
        
        ```
        angular_z = 0.002 * error_x
        ```
        
        실제 카메라 장착 방향에 따라 달라질 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        라인 트레이싱 제어 노드는 다음처럼 동작할 수 있습니다.
        
        ```
        error_x가 음수 → 왼쪽으로 보정
        error_x가 양수 → 오른쪽으로 보정
        error_x가 0 근처 → 직진
        ```
        
        ---
        
        # 예제 93. ArUco Marker 검출
        
        ## 핵심 주제
        
        ArUco Marker는 로봇 비전에서 위치 인식, 마커 기반 정렬, 작업 위치 지정에 자주 사용되는 사각형 마커입니다.
        
        OpenCV의 `aruco` 모듈을 사용하면 마커 ID와 꼭짓점을 검출할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ArUco Dictionary 이해
        2. Marker 검출
        3. Marker ID 표시
        4. Marker 중심 좌표 계산
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        aruco_dict = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_4X4_50
        )
        
        parameters = cv2.aruco.DetectorParameters()
        
        detector = cv2.aruco.ArucoDetector(
            aruco_dict,
            parameters
        )
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
                corners, ids, rejected = detector.detectMarkers(gray)
        
                if ids is not None:
                    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
                    for marker_corners, marker_id in zip(corners, ids):
                        points = marker_corners[0]
        
                        center_x = int(points[:, 0].mean())
                        center_y = int(points[:, 1].mean())
        
                        cv2.circle(
                            frame,
                            (center_x, center_y),
                            6,
                            (0, 0, 255),
                            -1
                        )
        
                        cv2.putText(
                            frame,
                            f"ID: {int(marker_id[0])}",
                            (center_x + 10, center_y),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2
                        )
        
                        print("Marker ID:", int(marker_id[0]))
                        print("Marker Center:", center_x, center_y)
        
                cv2.imshow("ArUco Detection", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. opencv-python만 설치하고 aruco가 없다고 당황함
        
        일부 환경에서는 `opencv-contrib-python`이 필요할 수 있습니다.
        
        ```
        pip install opencv-contrib-python
        ```
        
        ---
        
        ### 실수 2. 마커가 너무 작거나 흐림
        
        마커가 작거나 초점이 흐리면 검출률이 떨어집니다.
        
        마커는 충분히 크게 출력하고, 카메라 초점을 맞춰야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ArUco Marker는 다음 프로젝트에 자주 사용됩니다.
        
        ```
        로봇 정지 위치 지정
        로봇 팔 Pick 기준점 설정
        충전 스테이션 위치 인식
        카메라 캘리브레이션 보조
        작업대 좌표 기준 마커
        ```
        
        ---
        
        # 예제 94. QR 코드 검출
        
        ## 핵심 주제
        
        QR 코드는 물체 ID, 작업 지시, 위치 정보, 제품 정보를 담을 수 있습니다.
        
        OpenCV의 `QRCodeDetector`를 사용하면 QR 코드를 검출하고 문자열 데이터를 읽을 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. QRCodeDetector 사용법 이해
        2. QR 코드 위치 검출
        3. QR 데이터 읽기
        4. QR 영역 표시
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        
        cap = cv2.VideoCapture(0)
        
        qr_detector = cv2.QRCodeDetector()
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                data, points, straight_qrcode = qr_detector.detectAndDecode(frame)
        
                if points is not None:
                    points = points.astype(int)
        
                    for i in range(len(points[0])):
                        pt1 = tuple(points[0][i])
                        pt2 = tuple(points[0][(i + 1) % len(points[0])])
        
                        cv2.line(
                            frame,
                            pt1,
                            pt2,
                            (0, 255, 0),
                            2
                        )
        
                    if data:
                        cv2.putText(
                            frame,
                            data,
                            tuple(points[0][0]),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 0, 255),
                            2
                        )
        
                        print("QR 데이터:", data)
        
                cv2.imshow("QR Code Detection", frame)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. QR 코드가 검출되었지만 data가 비어 있음
        
        검출은 되었지만 초점, 조명, 각도 때문에 디코딩은 실패할 수 있습니다.
        
        마커가 너무 작거나 흐리면 문자열을 읽지 못합니다.
        
        ---
        
        ### 실수 2. QR을 너무 비스듬히 보여줌
        
        QR 코드는 어느 정도 기울어져도 읽히지만, 너무 비스듬하면 실패합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        QR 코드는 다음에 활용할 수 있습니다.
        
        ```
        제품 ID 인식
        작업 지시 코드 읽기
        로봇 목적지 정보 읽기
        물류 박스 식별
        컨베이어 제품 분류
        ```
        
        ROS2에서는 읽은 문자열을 `std_msgs/String` Topic으로 발행할 수 있습니다.
        
        ---
        
        # 예제 95. 장애물 색상 검출
        
        ## 핵심 주제
        
        로봇이 특정 색상의 장애물을 검출하고 위치를 파악합니다.
        
        예를 들어 빨간색 장애물을 위험 영역으로 판단할 수 있습니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 빨간색 마스크 생성
        2. 장애물 Contour 검출
        3. Bounding Box 표시
        4. 화면 중앙 기준 위치 판단
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                height, width = frame.shape[:2]
                image_center_x = width // 2
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_red1 = np.array([0, 100, 100])
                upper_red1 = np.array([10, 255, 255])
                lower_red2 = np.array([170, 100, 100])
                upper_red2 = np.array([179, 255, 255])
        
                mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
                mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        
                mask = cv2.bitwise_or(mask1, mask2)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, _ = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                obstacle_detected = False
        
                for contour in contours:
                    area = cv2.contourArea(contour)
        
                    if area > 800:
                        obstacle_detected = True
        
                        x, y, w, h = cv2.boundingRect(contour)
                        center_x = x + w // 2
                        center_y = y + h // 2
        
                        error_x = center_x - image_center_x
        
                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (0, 0, 255),
                            2
                        )
        
                        cv2.circle(
                            frame,
                            (center_x, center_y),
                            6,
                            (255, 0, 0),
                            -1
                        )
        
                        cv2.putText(
                            frame,
                            f"Obstacle error_x: {error_x}",
                            (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 0, 255),
                            2
                        )
        
                        print("장애물 중심:", center_x, center_y, "면적:", area)
        
                if not obstacle_detected:
                    cv2.putText(
                        frame,
                        "No Red Obstacle",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )
        
                cv2.imshow("Obstacle Detection", frame)
                cv2.imshow("Obstacle Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 색상만으로 장애물을 판단함
        
        빨간 포스터, 빨간 옷, 빨간 조명도 장애물로 검출될 수 있습니다.
        
        실무에서는 거리 센서, LiDAR, Depth Camera와 함께 판단하는 것이 안전합니다.
        
        ---
        
        ### 실수 2. 면적을 거리로 바로 해석함
        
        면적이 크면 가까울 가능성이 있지만, 실제 거리는 카메라 보정과 객체 크기를 알아야 계산할 수 있습니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        장애물 검출 결과는 다음 Topic으로 발행할 수 있습니다.
        
        ```
        /vision/obstacle_detected
        /vision/obstacle_center
        /vision/obstacle_area
        ```
        
        제어 노드는 장애물이 중앙에 크고 가깝게 보이면 정지하도록 만들 수 있습니다.
        
        ---
        
        # 예제 96. 작업물 위치 검출
        
        ## 핵심 주제
        
        작업대 위 물체의 위치를 검출합니다.
        
        로봇 팔 Pick 작업에서는 물체의 중심 좌표가 중요합니다.
        
        ```
        작업대 영상
        → 색상 또는 Threshold
        → Contour
        → Bounding Box
        → 중심점 계산
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. 작업물 후보 영역 검출
        2. Contour 기반 위치 계산
        3. 중심점 표시
        4. Pick 후보 좌표 생성
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/workpiece.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_object = np.array([20, 80, 80])
            upper_object = np.array([40, 255, 255])
        
            mask = cv2.inRange(hsv, lower_object, upper_object)
        
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
        
            for contour in contours:
                area = cv2.contourArea(contour)
        
                if area > 500:
                    x, y, w, h = cv2.boundingRect(contour)
        
                    center_x = x + w // 2
                    center_y = y + h // 2
        
                    cv2.rectangle(
                        result,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )
        
                    cv2.circle(
                        result,
                        (center_x, center_y),
                        6,
                        (0, 0, 255),
                        -1
                    )
        
                    cv2.putText(
                        result,
                        f"Pick: ({center_x}, {center_y})",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2
                    )
        
                    print("작업물 중심 픽셀 좌표:", center_x, center_y)
        
            cv2.imshow("Workpiece Mask", mask)
            cv2.imshow("Workpiece Detection", result)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 픽셀 좌표를 로봇 팔 좌표로 바로 사용
        
        픽셀 좌표는 이미지 안의 위치입니다.
        
        로봇 팔이 사용하는 실제 좌표와 다릅니다.
        
        픽셀 좌표를 로봇 좌표로 바꾸려면 다음이 필요합니다.
        
        ```
        카메라 캘리브레이션
        작업대 평면 기준 Homography
        카메라-로봇 좌표계 변환
        Hand-eye calibration
        ```
        
        ---
        
        ### 실수 2. 그림자까지 작업물로 검출
        
        조명 조건이 나쁘면 그림자나 반사가 같이 검출될 수 있습니다.
        
        HSV 범위, Morphology, 면적 필터링을 조정해야 합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        작업물 중심 좌표는 다음 Topic으로 발행할 수 있습니다.
        
        ```
        /vision/pick_candidate
        ```
        
        로봇 팔 제어 노드는 이 좌표를 받아 실제 Pick 좌표로 변환합니다.
        
        ---
        
        # 예제 97. 컨베이어 객체 카운팅
        
        ## 핵심 주제
        
        컨베이어 위를 지나가는 객체를 검출하고 특정 기준선을 통과할 때 카운트합니다.
        
        공장 자동화, 물류, 검사 시스템에서 매우 자주 사용되는 구조입니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 객체 검출
        2. 기준선 설정
        3. 객체 중심점 추적
        4. 기준선 통과 시 카운트 증가
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        cap = cv2.VideoCapture(0)
        
        count = 0
        counted_centers = []
        
        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
        else:
            while True:
                ret, frame = cap.read()
        
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break
        
                height, width = frame.shape[:2]
        
                line_y = height // 2
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_object = np.array([20, 80, 80])
                upper_object = np.array([40, 255, 255])
        
                mask = cv2.inRange(hsv, lower_object, upper_object)
        
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, _ = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                cv2.line(
                    frame,
                    (0, line_y),
                    (width, line_y),
                    (255, 0, 0),
                    2
                )
        
                current_centers = []
        
                for contour in contours:
                    area = cv2.contourArea(contour)
        
                    if area > 500:
                        x, y, w, h = cv2.boundingRect(contour)
        
                        center_x = x + w // 2
                        center_y = y + h // 2
        
                        current_centers.append((center_x, center_y))
        
                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (0, 255, 0),
                            2
                        )
        
                        cv2.circle(
                            frame,
                            (center_x, center_y),
                            5,
                            (0, 0, 255),
                            -1
                        )
        
                        if abs(center_y - line_y) < 10:
                            already_counted = False
        
                            for old_center in counted_centers:
                                old_x, old_y = old_center
        
                                distance = ((center_x - old_x) ** 2 + (center_y - old_y) ** 2) ** 0.5
        
                                if distance < 50:
                                    already_counted = True
                                    break
        
                            if not already_counted:
                                count += 1
                                counted_centers.append((center_x, center_y))
                                print("객체 카운트:", count)
        
                cv2.putText(
                    frame,
                    f"Count: {count}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 255, 255),
                    2
                )
        
                cv2.imshow("Conveyor Counting", frame)
                cv2.imshow("Mask", mask)
        
                if cv2.waitKey(1) == ord('q'):
                    break
        
            cap.release()
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 기준선 근처에서 객체가 여러 프레임 머물며 중복 카운트됨
        
        영상은 초당 여러 프레임이므로 객체 하나가 기준선 근처에 여러 번 나타납니다.
        
        중복 방지 로직이 필요합니다.
        
        ---
        
        ### 실수 2. 단순 중심점 거리만으로 추적
        
        실무에서는 객체 ID 추적이 필요합니다.
        
        더 안정적인 방법은 다음입니다.
        
        ```
        Centroid Tracking
        SORT
        DeepSORT
        ByteTrack
        ```
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        컨베이어 카운트 결과는 다음 Topic으로 발행할 수 있습니다.
        
        ```
        /vision/object_count
        /vision/object_detected
        ```
        
        MES, APS, WMS 시스템과도 연결 가능한 산업용 패턴입니다.
        
        ---
        
        # 예제 98. 로봇 팔 Pick 위치 계산
        
        ## 핵심 주제
        
        로봇 팔이 물체를 집으려면 이미지 좌표를 작업대 좌표로 변환해야 합니다.
        
        이번 예제에서는 가장 단순한 선형 스케일 변환으로 개념을 이해합니다.
        
        실제 현장에서는 Homography 또는 Hand-eye Calibration이 필요합니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. 픽셀 좌표와 로봇 좌표 차이 이해
        2. 작업대 영역 기준 변환
        3. 이미지 중심 좌표를 mm 단위로 근사 변환
        4. Pick 좌표 생성
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/workpiece.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            height, width = image.shape[:2]
        
            workspace_width_mm = 400
            workspace_height_mm = 300
        
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
            lower_object = np.array([20, 80, 80])
            upper_object = np.array([40, 255, 255])
        
            mask = cv2.inRange(hsv, lower_object, upper_object)
        
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
        
            result = image.copy()
        
            if len(contours) > 0:
                largest_contour = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(largest_contour)
        
                if area > 500:
                    x, y, w, h = cv2.boundingRect(largest_contour)
        
                    center_x = x + w // 2
                    center_y = y + h // 2
        
                    robot_x_mm = center_x / width * workspace_width_mm
                    robot_y_mm = center_y / height * workspace_height_mm
        
                    cv2.rectangle(
                        result,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )
        
                    cv2.circle(
                        result,
                        (center_x, center_y),
                        6,
                        (0, 0, 255),
                        -1
                    )
        
                    cv2.putText(
                        result,
                        f"Pick mm: ({robot_x_mm:.1f}, {robot_y_mm:.1f})",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2
                    )
        
                    print("픽셀 좌표:", center_x, center_y)
                    print("로봇 Pick 좌표 근사 mm:", robot_x_mm, robot_y_mm)
        
            cv2.imshow("Pick Position", result)
            cv2.imshow("Mask", mask)
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 단순 비례 변환을 실제 로봇에 그대로 사용
        
        이 예제는 개념 설명용입니다.
        
        실제 로봇 팔에는 다음이 필요합니다.
        
        ```
        카메라 내부 파라미터
        렌즈 왜곡 보정
        작업대 평면 Homography
        카메라 좌표계와 로봇 좌표계 변환
        Hand-eye Calibration
        로봇 TCP 보정
        ```
        
        ---
        
        ### 실수 2. z좌표를 고려하지 않음
        
        Pick 작업에는 x, y뿐 아니라 z좌표와 그리퍼 자세도 필요합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        Pick 좌표는 다음 Topic 또는 Action으로 연결됩니다.
        
        ```
        /vision/pick_pose
        → 로봇 팔 planning node
        → MoveIt2
        → trajectory 실행
        ```
        
        정식 구조에서는 `geometry_msgs/PoseStamped`를 사용하는 것이 좋습니다.
        
        ---
        
        # 예제 99. OpenCV + YOLO 연계 준비
        
        ## 핵심 주제
        
        YOLO 같은 딥러닝 객체 검출 모델을 사용하려면 OpenCV 프레임을 모델 입력 형식에 맞게 전처리해야 합니다.
        
        이번 예제는 실제 YOLO 추론이 아니라, YOLO 입력 전처리 구조를 준비합니다.
        
        일반적인 YOLO 입력은 다음과 같습니다.
        
        ```
        BGR frame
        → RGB 변환
        → Resize
        → 정규화
        → Batch 차원 추가
        → 모델 입력
        ```
        
        ---
        
        ## 실습 목표
        
        ```
        1. BGR to RGB 변환
        2. 모델 입력 크기 Resize
        3. 0~1 정규화
        4. NCHW 형태 변환
        ```
        
        ---
        
        ## 실습 소스
        
        ```python
        import cv2
        import numpy as np
        
        image_path = "practice_images/sample.jpg"
        
        image = cv2.imread(image_path)
        
        if image is None:
            print("이미지를 읽을 수 없습니다.")
        else:
            input_size = 640
        
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
            resized = cv2.resize(rgb_image, (input_size, input_size))
        
            normalized = resized.astype(np.float32) / 255.0
        
            chw = np.transpose(normalized, (2, 0, 1))
        
            batch = np.expand_dims(chw, axis=0)
        
            print("원본 shape:", image.shape)
            print("RGB Resize shape:", resized.shape)
            print("정규화 범위:", normalized.min(), normalized.max())
            print("CHW shape:", chw.shape)
            print("Batch shape:", batch.shape)
        
            cv2.imshow("Original BGR", image)
            cv2.imshow("YOLO Input Preview", cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))
        
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. BGR/RGB 변환을 빼먹음
        
        색상 순서가 틀리면 모델 정확도가 떨어질 수 있습니다.
        
        ---
        
        ### 실수 2. 무조건 640×640으로 찌그러뜨림
        
        비율을 유지하지 않고 강제 Resize하면 객체 모양이 왜곡됩니다.
        
        실제 YOLO에서는 Letterbox 전처리를 많이 사용합니다.
        
        ---
        
        ## ROS2와 연결되는 포인트
        
        ROS2 + YOLO 노드는 보통 다음 구조입니다.
        
        ```
        /camera/image_raw
        → cv_bridge
        → OpenCV frame
        → YOLO 전처리
        → 모델 추론
        → Bounding Box 결과
        → /vision/detections 발행
        → debug image 발행
        ```
        
        ---
        
        # 예제 100. ROS2 비전 프로젝트 통합 구조
        
        ## 핵심 주제
        
        마지막 예제에서는 OpenCV 기반 ROS2 비전 프로젝트의 전체 구조를 설계합니다.
        
        이 예제는 코드 한 파일보다 중요한 **실무 프로젝트 구조**를 다룹니다.
        
        ---
        
        ## 실습 목표
        
        ```
        1. ROS2 비전 패키지 구조 이해
        2. OpenCV 처리 함수 분리
        3. Image Topic과 좌표 Topic 분리
        4. 디버깅 이미지 발행
        5. 제어 노드와 연결 가능한 구조 설계
        ```
        
        ---
        
        ## 권장 패키지 구조
        
        ```
        ros2_opencv_vision/
        ├─ package.xml
        ├─ setup.py
        ├─ resource/
        │  └─ ros2_opencv_vision
        ├─ ros2_opencv_vision/
        │  ├─ __init__.py
        │  ├─ vision_node.py
        │  ├─ line_detector.py
        │  ├─ color_detector.py
        │  ├─ aruco_detector.py
        │  └─ utils.py
        └─ launch/
           └─ vision.launch.py
        ```
        
        ---
        
        ## 파일 역할
        
        | 파일 | 역할 |
        | --- | --- |
        | `vision_node.py` | ROS2 Subscriber/Publisher 담당 |
        | `line_detector.py` | 라인 검출 함수 |
        | `color_detector.py` | 색상 객체 검출 함수 |
        | `aruco_detector.py` | ArUco Marker 검출 함수 |
        | `utils.py` | 공통 변환, 그리기, 파라미터 함수 |
        | `vision.launch.py` | 비전 노드 실행 설정 |
        
        ---
        
        ## 통합 노드 예시 코드
        
        ```python
        import rclpy
        from rclpy.node import Node
        from sensor_msgs.msg import Image
        from geometry_msgs.msg import Point
        from std_msgs.msg import Bool
        from cv_bridge import CvBridge
        import cv2
        import numpy as np
        
        class IntegratedVisionNode(Node):
            def __init__(self):
                super().__init__("integrated_vision_node")
        
                self.bridge = CvBridge()
        
                self.image_sub = self.create_subscription(
                    Image,
                    "/camera/image_raw",
                    self.image_callback,
                    10
                )
        
                self.debug_image_pub = self.create_publisher(
                    Image,
                    "/vision/debug_image",
                    10
                )
        
                self.target_pub = self.create_publisher(
                    Point,
                    "/vision/target_center",
                    10
                )
        
                self.detected_pub = self.create_publisher(
                    Bool,
                    "/vision/target_detected",
                    10
                )
        
            def image_callback(self, msg):
                try:
                    frame = self.bridge.imgmsg_to_cv2(
                        msg,
                        desired_encoding="bgr8"
                    )
        
                    debug_frame, detection = self.detect_blue_target(frame)
        
                    detected_msg = Bool()
                    detected_msg.data = detection is not None
                    self.detected_pub.publish(detected_msg)
        
                    if detection is not None:
                        point_msg = Point()
                        point_msg.x = float(detection["center_x"])
                        point_msg.y = float(detection["center_y"])
                        point_msg.z = float(detection["area"])
        
                        self.target_pub.publish(point_msg)
        
                    debug_msg = self.bridge.cv2_to_imgmsg(
                        debug_frame,
                        encoding="bgr8"
                    )
                    debug_msg.header = msg.header
        
                    self.debug_image_pub.publish(debug_msg)
        
                except Exception as e:
                    self.get_logger().error(f"통합 비전 처리 오류: {e}")
        
            def detect_blue_target(self, frame):
                debug_frame = frame.copy()
        
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
                lower_blue = np.array([100, 100, 100])
                upper_blue = np.array([130, 255, 255])
        
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
                kernel = np.ones((5, 5), np.uint8)
        
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
                contours, _ = cv2.findContours(
                    mask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE
                )
        
                height, width = frame.shape[:2]
                image_center_x = width // 2
        
                cv2.line(
                    debug_frame,
                    (image_center_x, 0),
                    (image_center_x, height),
                    (255, 0, 0),
                    2
                )
        
                if len(contours) == 0:
                    cv2.putText(
                        debug_frame,
                        "Target Not Found",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )
                    return debug_frame, None
        
                largest_contour = max(contours, key=cv2.contourArea)
        
                area = cv2.contourArea(largest_contour)
        
                if area < 500:
                    return debug_frame, None
        
                moments = cv2.moments(largest_contour)
        
                if moments["m00"] == 0:
                    return debug_frame, None
        
                center_x = int(moments["m10"] / moments["m00"])
                center_y = int(moments["m01"] / moments["m00"])
        
                error_x = center_x - image_center_x
        
                cv2.drawContours(
                    debug_frame,
                    [largest_contour],
                    -1,
                    (0, 255, 0),
                    2
                )
        
                cv2.circle(
                    debug_frame,
                    (center_x, center_y),
                    8,
                    (0, 0, 255),
                    -1
                )
        
                cv2.putText(
                    debug_frame,
                    f"center=({center_x},{center_y}) area={int(area)}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )
        
                cv2.putText(
                    debug_frame,
                    f"error_x={error_x}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )
        
                detection = {
                    "center_x": center_x,
                    "center_y": center_y,
                    "area": area,
                    "error_x": error_x
                }
        
                return debug_frame, detection
        
        def main(args=None):
            rclpy.init(args=args)
        
            node = IntegratedVisionNode()
        
            rclpy.spin(node)
        
            node.destroy_node()
            rclpy.shutdown()
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ## 실행 확인 명령
        
        ```
        ros2 topic list
        ```
        
        확인해야 할 Topic:
        
        ```
        /vision/debug_image
        /vision/target_center
        /vision/target_detected
        ```
        
        ---
        
        ```
        ros2 topic echo /vision/target_detected
        ```
        
        검출 여부 확인:
        
        ```
        data: true
        ```
        
        ---
        
        ```
        ros2 topic echo /vision/target_center
        ```
        
        검출 좌표 확인:
        
        ```
        x: 318.0
        y: 225.0
        z: 5230.0
        ```
        
        ---
        
        ```
        rqt_image_view
        ```
        
        디버깅 이미지 Topic 선택:
        
        ```
        /vision/debug_image
        ```
        
        ---
        
        ## 실무에서 자주 하는 실수
        
        ### 실수 1. 검출 여부와 좌표를 분리하지 않음
        
        좌표만 발행하면 객체가 사라졌는지 알기 어렵습니다.
        
        반드시 검출 여부 Topic 또는 메시지 필드를 함께 두는 것이 좋습니다.
        
        ---
        
        ### 실수 2. 처리 이미지와 수치 결과를 하나의 Topic으로만 처리함
        
        이미지는 사람이 디버깅하기 위한 것이고, 좌표는 제어 노드가 쓰기 위한 것입니다.
        
        둘은 분리하는 것이 좋습니다.
        
        ---
        
        ### 실수 3. OpenCV 처리 로직을 노드 안에 계속 추가함
        
        프로젝트가 커지면 다음처럼 분리해야 합니다.
        
        ```
        color_detector.py
        line_detector.py
        aruco_detector.py
        qr_detector.py
        ```
        
        그래야 테스트와 유지보수가 쉬워집니다.
        
        ---
        
        # 10단계 핵심 정리
        
        이번 10단계에서는 로봇 실무 프로젝트형 OpenCV 예제를 다뤘습니다.
        
        | 예제 | 핵심 내용 |
        | --- | --- |
        | 91 | 라인 트레이싱 전처리 |
        | 92 | 차선 중심 계산 |
        | 93 | ArUco Marker 검출 |
        | 94 | QR 코드 검출 |
        | 95 | 장애물 색상 검출 |
        | 96 | 작업물 위치 검출 |
        | 97 | 컨베이어 객체 카운팅 |
        | 98 | 로봇 팔 Pick 위치 계산 |
        | 99 | OpenCV + YOLO 연계 준비 |
        | 100 | ROS2 비전 프로젝트 통합 구조 |
        
        ---
        
        # OpenCV 실습 100제 전체 핵심 요약
        
        ## 1단계: 기본 입출력
        
        ```
        이미지 읽기
        이미지 출력
        이미지 저장
        픽셀 접근
        ROI 자르기
        ```
        
        ## 2단계: 색상 변환과 전처리
        
        ```
        BGR/RGB/GRAY/HSV 변환
        밝기/대비 조절
        Threshold
        Adaptive Threshold
        Otsu Threshold
        ```
        
        ## 3단계: 기하 변환
        
        ```
        Resize
        회전
        이동
        Flip
        Affine Transform
        Perspective Transform
        Padding
        ```
        
        ## 4단계: 필터링
        
        ```
        Average Blur
        Gaussian Blur
        Median Blur
        Bilateral Filter
        Sharpening
        Noise 제거
        ```
        
        ## 5단계: Edge와 Contour
        
        ```
        Sobel
        Laplacian
        Canny
        Contour
        Bounding Box
        중심점 계산
        도형 분류
        ```
        
        ## 6단계: 카메라와 비디오
        
        ```
        VideoCapture
        실시간 프레임 처리
        FPS 확인
        비디오 저장
        프레임 캡처
        ```
        
        ## 7단계: 색상 기반 객체 추적
        
        ```
        HSV Mask
        빨강/파랑/초록 객체 검출
        Morphology
        객체 중심 추적
        여러 객체 추적
        ```
        
        ## 8단계: 특징점과 매칭
        
        ```
        Histogram
        CLAHE
        Template Matching
        ORB
        Feature Matching
        이미지 유사도
        ```
        
        ## 9단계: ROS2 연계
        
        ```
        cv_bridge
        Image Subscriber
        Image Publisher
        Edge Publisher
        Target Center Publisher
        Follow Vision Node
        ```
        
        ## 10단계: 로봇 실무 프로젝트
        
        ```
        라인 트레이싱
        ArUco
        QR
        장애물 검출
        작업물 Pick 좌표
        컨베이어 카운팅
        YOLO 연계 준비
        ROS2 통합 구조
        ```
        
        ---
        
        # ROS2 Humble 강의 전 최종 학습 로드맵
        
        취업 준비생 대상이라면 OpenCV를 다음 순서로 복습시키는 것이 좋습니다.
        
        ```
        1. 이미지 구조 이해
        2. 색상 공간 이해
        3. Threshold와 HSV 마스크
        4. Contour와 중심점 계산
        5. 실시간 카메라 처리
        6. 객체 추적
        7. ROS2 Image 메시지와 cv_bridge
        8. 비전 결과 Topic 발행
        9. /cmd_vel 또는 MoveIt2와 연결
        ```
        
        ---
        
        # 최종 실무 연결 구조
        
        ```
        카메라 센서
        → ROS2 camera driver
        → /camera/image_raw
        → cv_bridge
        → OpenCV frame
        → 전처리
        → 객체/라인/마커 검출
        → 중심 좌표 또는 상태 계산
        → /vision/... Topic 발행
        → 제어 노드
        → /cmd_vel 또는 로봇 팔 제어
        ```