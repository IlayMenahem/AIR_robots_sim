from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import cv2

def relay_race(start_position):
    env = SimEnv()
    executor = MotionExecutor(env)
    env.reset(randomize=False, block_positions=[start_position])

    executor.pick_up("ur5e_2", start_position[0], start_position[1])

    pi = 3.14159265359

    angle = pi*(8.925/32)
    p = -0.315*pi
    joint_positions = [angle, p, -p, pi, -pi/2, 0]
    executor.moveJ("ur5e_2", joint_positions, speed=3)
    executor.moveJ("ur5e_1", joint_positions, speed=3)

    # Move the second robot to a final position and put down the block
    final_position = [-0.7, -0.8, 0.15]
    executor.plan_and_move_to_xyz_facing_down("ur5e_1", final_position)
    executor.put_down("ur5e_1", final_position[0], final_position[1], final_position[2] + 0.05)

    # Wait for stability
    executor.wait(4)

    # Record video (replace with your video recording logic)
    frames = []
    for _ in range(100):  # Capture 100 frames
        frame = env.render(mode="rgb_array")  # Render the simulation frame
        frames.append(frame)

    # Save video
    out = cv2.VideoWriter('relay_race_simulation.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
    for frame in frames:
        out.write(frame)
    out.release()

start_position = [-0.7, -0.8, 0.03]
relay_race(start_position)
