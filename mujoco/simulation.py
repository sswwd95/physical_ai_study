import mujoco
import mujoco.viewer
import time
import os

# 강사의 Tip: 
# MuJoCo(Multi-Joint dynamics with Contact)는 로봇공학에서 가장 널리 쓰이는 물리 엔진 중 하나입니다.
# DeepMind에서 인수한 이후 오픈소스로 바뀌어 누구나 쉽게 고성능 시뮬레이션을 즐길 수 있게 되었죠.

def main():
    # 1. 모델 경로 설정
    # MuJoCo Menagerie에서 다운로드한 TIAGo Dual 모델의 경로를 지정합니다.
    # 'scene_position.xml'은 바닥(floor)과 조명, 그리고 위치 제어기(position actuator)가 포함된 설정입니다.
    model_path = os.path.join("mujoco_menagerie", "pal_tiago_dual", "scene_position.xml")
    
    if not os.path.exists(model_path):
        print(f"Error: 모델 파일을 찾을 수 없습니다. 경로를 확인해주세요: {model_path}")
        return

    # 2. 모델 로드 (Load Model)
    # XML 파일을 읽어서 MuJoCo가 이해할 수 있는 바이너리 형태(mjModel)로 변환합니다.
    print("로봇 모델을 로드 중입니다...")
    model = mujoco.MjModel.from_xml_path(model_path)
    
    # 3. 데이터 생성 (Data structure)
    # mjData는 시뮬레이션의 상태(관절 위치, 속도, 힘 등)가 저장되는 곳입니다.
    data = mujoco.MjData(model)

    # 4. 시뮬레이션 실행 및 시각화 (Launch Viewer)
    # mujoco.viewer.launch를 사용하면 실시간으로 로봇을 확인하고 마우스로 조작할 수 있는 창이 뜹니다.
    print("시뮬레이션을 시작합니다. 창이 뜨면 로봇을 확인해보세요!")
    
    with mujoco.viewer.launch_passive(model, data) as viewer:
        # 시뮬레이션 루프
        # 강사의 Tip: 시뮬레이션 시간과 실제 시간을 맞추기 위해 time.sleep과 제어 루프를 적절히 조절합니다.
        start_time = time.time()
        
        while viewer.is_running():
            step_start = time.time()

            # 5. 로봇 제어 (Control)
            # 강사의 Tip: data.ctrl 배열을 통해 로봇의 각 Actuator(제어기)에 값을 전달할 수 있습니다.
            # TIAGo Dual의 팔(arm) 관절 중 일부를 사인 함수를 이용해 부드럽게 움직여 보겠습니다.
            import math
            current_sim_time = data.time
            # 보통 0번부터 관절 순서대로 매핑되어 있습니다. (scene_position.xml 기준)
            # 간단하게 몇 개의 관절을 흔들어 보겠습니다.
            movement = math.sin(current_sim_time * 2.0) * 0.5
            for i in range(len(data.ctrl)):
                # 모든 관절에 조금씩 움직임을 주어 로봇이 '살아있는' 느낌을 줍니다.
                # 실제 현업에서는 특정 관절의 이름을 찾아 정확히 제어해야 합니다.
                data.ctrl[i] = movement

            # mj_step은 물리 엔진을 '한 걸음' 전진시킵니다.
            # 이 때 모든 관절의 움직임과 충돌 계산이 일어납니다.
            mujoco.mj_step(model, data)

            # 주기적으로 시각화 정보를 업데이트합니다.
            viewer.sync()

            # 시뮬레이션 속도를 실제 시간과 비슷하게 맞춥니다.
            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)

if __name__ == "__main__":
    main()
