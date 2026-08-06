# OpenCV 100제 VSCode 프로젝트

Notion 강의 자료의 OpenCV 예제 1~100을 실행 파일로 분리한 프로젝트입니다.
원본 설명은 `notes/ex001.md`부터 `notes/ex100.md`에 보존되어 있습니다.

## 설치

```bat
conda env create -f environment.yml
conda activate opencv-100
```

이미 환경이 있다면 다음도 가능합니다.

```bat
pip install -r requirements.txt
```

## 실행

프로젝트 루트에서 원하는 번호를 실행합니다.

```bat
python run_example.py 1
python run_example.py 62
```

또는 다음 파일을 실행합니다.

```bat
scripts\run_example.bat
```

단계 전체 실행:

```bat
scripts\run_stage01.bat
```

## 주의사항

- 이미지 예제는 `practice_images/sample.jpg`를 기본으로 사용합니다.
- 비디오 예제는 원본 코드의 경로가 다를 수 있으므로 `practice_videos/sample.mp4`로 맞춰야 할 수 있습니다.
- 카메라 예제는 PC에 웹캠이 연결되어 있어야 합니다.
- ROS2 예제는 Windows 일반 Anaconda 환경만으로 실행되지 않으며 ROS2 Humble, `rclpy`, `cv_bridge` 등이 필요합니다.
- 82번과 90번은 원본이 설명 중심이므로 실행 파일은 안내를 출력하고, 전체 내용은 해당 `notes` 파일에 있습니다.
- 여러 예제를 연속 실행하면 OpenCV 창이나 웹캠 입력 때문에 중간에 사용자 조작이 필요할 수 있습니다.

## 폴더 구조

```text
opencv_100/
├─ stage01/ ~ stage10/     예제 Python 파일
├─ notes/                  예제별 원본 설명
├─ practice_images/        실습 이미지
├─ practice_videos/        실습 비디오
├─ outputs/                결과 저장 폴더
├─ scripts/                Windows 실행 배치 파일
├─ run_example.py          번호 기반 실행기
├─ environment.yml
└─ requirements.txt
```

## 예제 목록

| 번호 | 단계 | 주제 | 파일 |
| ---: | ---: | --- | --- |
| 1 | 01 | OpenCV 설치 확인 및 버전 출력 | `stage01/ex001.py` |
| 2 | 01 | 이미지 파일 읽기 | `stage01/ex002.py` |
| 3 | 01 | 이미지 화면 출력 | `stage01/ex003.py` |
| 4 | 01 | 이미지 저장 | `stage01/ex004.py` |
| 5 | 01 | 이미지 크기, 채널, 데이터 타입 확인 | `stage01/ex005.py` |
| 6 | 01 | 컬러 이미지와 흑백 이미지 비교 | `stage01/ex006.py` |
| 7 | 01 | BGR 색상 구조 이해 | `stage01/ex007.py` |
| 8 | 01 | 이미지 픽셀 값 읽기 | `stage01/ex008.py` |
| 9 | 01 | 이미지 픽셀 값 수정 | `stage01/ex009.py` |
| 10 | 01 | 관심 영역 ROI 자르기 | `stage01/ex010.py` |
| 11 | 02 | BGR에서 RGB로 변환 | `stage02/ex011.py` |
| 12 | 02 | BGR에서 Grayscale 변환 | `stage02/ex012.py` |
| 13 | 02 | BGR에서 HSV 변환 | `stage02/ex013.py` |
| 14 | 02 | 특정 색상 영역 검출 | `stage02/ex014.py` |
| 15 | 02 | 이미지 밝기 조절 | `stage02/ex015.py` |
| 16 | 02 | 이미지 대비 조절 | `stage02/ex016.py` |
| 17 | 02 | 이미지 반전 | `stage02/ex017.py` |
| 18 | 02 | Threshold 이진화 | `stage02/ex018.py` |
| 19 | 02 | Adaptive Threshold | `stage02/ex019.py` |
| 20 | 02 | Otsu Threshold | `stage02/ex020.py` |
| 21 | 03 | 이미지 Resize | `stage03/ex021.py` |
| 22 | 03 | 비율 유지 Resize | `stage03/ex022.py` |
| 23 | 03 | 이미지 회전 | `stage03/ex023.py` |
| 24 | 03 | 이미지 이동 | `stage03/ex024.py` |
| 25 | 03 | 이미지 뒤집기 | `stage03/ex025.py` |
| 26 | 03 | Affine Transform | `stage03/ex026.py` |
| 27 | 03 | Perspective Transform | `stage03/ex027.py` |
| 28 | 03 | 이미지 패딩 | `stage03/ex028.py` |
| 29 | 03 | 이미지 피라미드 축소 | `stage03/ex029.py` |
| 30 | 03 | 이미지 피라미드 확대 | `stage03/ex030.py` |
| 31 | 04 | 평균 블러 | `stage04/ex031.py` |
| 32 | 04 | Gaussian Blur | `stage04/ex032.py` |
| 33 | 04 | Median Blur | `stage04/ex033.py` |
| 34 | 04 | Bilateral Filter | `stage04/ex034.py` |
| 35 | 04 | Sharpening | `stage04/ex035.py` |
| 36 | 04 | 엣지 보존 필터 | `stage04/ex036.py` |
| 37 | 04 | 노이즈 이미지 생성 | `stage04/ex037.py` |
| 38 | 04 | Salt & Pepper 노이즈 제거 | `stage04/ex038.py` |
| 39 | 04 | 이미지 스무딩 비교 | `stage04/ex039.py` |
| 40 | 04 | 실시간 카메라 블러 처리 | `stage04/ex040.py` |
| 41 | 05 | Sobel Edge | `stage05/ex041.py` |
| 42 | 05 | Laplacian Edge | `stage05/ex042.py` |
| 43 | 05 | Canny Edge | `stage05/ex043.py` |
| 44 | 05 | Contour 검출 | `stage05/ex044.py` |
| 45 | 05 | Contour 면적 계산 | `stage05/ex045.py` |
| 46 | 05 | Bounding Box | `stage05/ex046.py` |
| 47 | 05 | 최소 외접 원 | `stage05/ex047.py` |
| 48 | 05 | 다각형 근사 | `stage05/ex048.py` |
| 49 | 05 | 도형 분류 | `stage05/ex049.py` |
| 50 | 05 | 객체 중심점 계산 | `stage05/ex050.py` |
| 51 | 06 | 웹캠 열기 | `stage06/ex051.py` |
| 52 | 06 | 실시간 프레임 출력 | `stage06/ex052.py` |
| 53 | 06 | 키보드 입력으로 종료 | `stage06/ex053.py` |
| 54 | 06 | 카메라 해상도 설정 | `stage06/ex054.py` |
| 55 | 06 | FPS 확인 | `stage06/ex055.py` |
| 56 | 06 | 비디오 파일 읽기 | `stage06/ex056.py` |
| 57 | 06 | 비디오 저장 | `stage06/ex057.py` |
| 58 | 06 | 실시간 흑백 변환 | `stage06/ex058.py` |
| 59 | 06 | 실시간 Edge 검출 | `stage06/ex059.py` |
| 60 | 06 | 카메라 프레임 캡처 | `stage06/ex060.py` |
| 61 | 07 | HSV 색상 마스크 | `stage07/ex061.py` |
| 62 | 07 | 빨간색 객체 검출 | `stage07/ex062.py` |
| 63 | 07 | 파란색 객체 검출 | `stage07/ex063.py` |
| 64 | 07 | 초록색 객체 검출 | `stage07/ex064.py` |
| 65 | 07 | 마스크 노이즈 제거 | `stage07/ex065.py` |
| 66 | 07 | 객체 중심 추적 | `stage07/ex066.py` |
| 67 | 07 | 실시간 원 검출 | `stage07/ex067.py` |
| 68 | 07 | 색상 객체 Bounding Box | `stage07/ex068.py` |
| 69 | 07 | 여러 객체 추적 | `stage07/ex069.py` |
| 70 | 07 | ROS2 Topic 변환 준비 | `stage07/ex070.py` |
| 71 | 08 | 이미지 히스토그램 | `stage08/ex071.py` |
| 72 | 08 | 히스토그램 평활화 | `stage08/ex072.py` |
| 73 | 08 | CLAHE | `stage08/ex073.py` |
| 74 | 08 | Template Matching | `stage08/ex074.py` |
| 75 | 08 | ORB 특징점 검출 | `stage08/ex075.py` |
| 76 | 08 | ORB 특징점 매칭 | `stage08/ex076.py` |
| 77 | 08 | 이미지 유사도 비교 | `stage08/ex077.py` |
| 78 | 08 | Feature Matching 시각화 | `stage08/ex078.py` |
| 79 | 08 | 간단한 물체 인식 | `stage08/ex079.py` |
| 80 | 08 | 로봇 비전에서 특징점 활용 | `stage08/ex080.py` |
| 81 | 09 | cv_bridge 개념 | `stage09/ex081.py` |
| 82 | 09 | ROS2 Image 메시지 이해 | `stage09/ex082.py` |
| 83 | 09 | OpenCV 이미지를 ROS2 메시지로 변환 | `stage09/ex083.py` |
| 84 | 09 | ROS2 Image 메시지를 OpenCV로 변환 | `stage09/ex084.py` |
| 85 | 09 | 카메라 노드 구조 설계 | `stage09/ex085.py` |
| 86 | 09 | 이미지 Subscriber 구조 | `stage09/ex086.py` |
| 87 | 09 | 실시간 Edge Publisher | `stage09/ex087.py` |
| 88 | 09 | 객체 중심 좌표 Publisher | `stage09/ex088.py` |
| 89 | 09 | 로봇 추종용 비전 노드 | `stage09/ex089.py` |
| 90 | 09 | OpenCV + ROS2 디버깅 포인트 | `stage09/ex090.py` |
| 91 | 10 | 라인 트레이싱 전처리 | `stage10/ex091.py` |
| 92 | 10 | 차선 중심 계산 | `stage10/ex092.py` |
| 93 | 10 | ArUco Marker 검출 | `stage10/ex093.py` |
| 94 | 10 | QR 코드 검출 | `stage10/ex094.py` |
| 95 | 10 | 장애물 색상 검출 | `stage10/ex095.py` |
| 96 | 10 | 작업물 위치 검출 | `stage10/ex096.py` |
| 97 | 10 | 컨베이어 객체 카운팅 | `stage10/ex097.py` |
| 98 | 10 | 로봇 팔 Pick 위치 계산 | `stage10/ex098.py` |
| 99 | 10 | OpenCV + YOLO 연계 준비 | `stage10/ex099.py` |
| 100 | 10 | ROS2 비전 프로젝트 통합 구조 | `stage10/ex100.py` |
