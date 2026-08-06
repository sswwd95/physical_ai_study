# ============================================================================
# 노션 원문 학습 설명: 예제 74. Template Matching
# ============================================================================
#
# [핵심 주제]
# Template Matching은 작은 템플릿 이미지를 큰 이미지 안에서 찾는 방법임
#
# 예를 들어 카메라 이미지 안에서 특정 마커, 로고, 버튼 모양을 찾을 때 사용 가능
#
# [실습 목표]
# 1. 템플릿 매칭 개념 이해
# 2. cv2.matchTemplate() 사용법 이해
# 3. 가장 유사한 위치 찾기
# 4. 검출 위치에 사각형 그리기
#
# [준비 파일]
# practice_images/scene.jpg
# practice_images/template.jpg
#
# `scene.jpg`는 전체 장면 이미지이고, `template.jpg`는 그 안에서 찾을 작은 이미지입니다.
#
# [실무에서 자주 하는 실수]
# 실수 1. 크기나 회전이 달라진 객체에 그대로 사용
#
# Template Matching은 템플릿과 대상의 크기, 회전, 형태가 거의 같을 때 잘 작동함
#
# 대상 물체가 커지거나 작아지거나 회전하면 성능이 급격히 떨어질 수 있음
#
# 실수 2. 유사도 임계값 없이 무조건 검출했다고 판단
#
# 항상 최고 위치는 나오지만, 그것이 진짜 물체라는 보장은 없음
#
# 실무에서는 다음처럼 임계값을 둡니다.
#
# if max_val > 0.8:
# print("검출 성공")
# else:
# print("검출 실패")
#
# [ROS2와 연결되는 포인트]
# Template Matching은 다음 작업에 사용 가능
#
# 특정 버튼 위치 찾기
# 작업대 위 기준 마커 찾기
# 로봇이 찾아야 할 단순 패턴 검출
# 정해진 위치의 부품 유무 확인
#
# 단, 물체 크기나 회전이 자주 바뀌는 모바일 로봇 환경에서는 특징점 기반 방법이나 딥러닝 검출이 더 적합할 수 있음
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# scene path 변수에 이후 처리에 사용할 값을 저장
scene_path = "practice_images/scene.jpg"
# template path 변수에 이후 처리에 사용할 값을 저장
template_path = "practice_images/template.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
scene = cv2.imread(scene_path)
template = cv2.imread(template_path)

# 이미지 또는 검출 결과 생성 여부 확인
if scene is None or template is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 작은 템플릿 이미지가 원본의 어느 위치와 가장 비슷한지 계산
    result = cv2.matchTemplate(
        scene_gray,
        template_gray,
        cv2.TM_CCOEFF_NORMED
    )

    # 행렬에서 최솟값·최댓값과 해당 위치를 찾습니다.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    template_height, template_width = template_gray.shape[:2]

    # top left 변수에 이후 처리에 사용할 값을 저장
    top_left = max_loc
    # bottom right 변수에 이후 처리에 사용할 값을 저장
    bottom_right = (
        top_left[0] + template_width,
        top_left[1] + template_height
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
    output = scene.copy()

    # 검출 영역을 알아보기 쉽도록 사각형을 그리기
    cv2.rectangle(
        output,
        top_left,
        bottom_right,
        (0, 0, 255),
        2
    )

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("최고 유사도:", max_val)
    print("검출 위치:", top_left)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Template", template)
    cv2.imshow("Matched Result", output)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
