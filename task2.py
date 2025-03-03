from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import cv2
import numpy as np

def relay_race(start_position):
    # Initialize the simulation environment and motion executor
    env = SimEnv()
    executor = MotionExecutor(env)

    # Add a block to the world
    env.reset(randomize=False, block_positions=[start_position])

    # Pick up the block with the first robot (ur5e_1)
    executor.pick_up("ur5e_2", start_position[0], start_position[1], start_position[2] + 0.1)

    # Move the first robot to a handover position
    handover_position = [-0.5, -0.4, 0.15]  # Example handover position
    executor.plan_and_move_to_xyz_facing_down("ur5e_1", handover_position)

    # Transfer the block to the second robot (ur5e_2)
    executor.pick_up("ur5e_1", handover_position[0], handover_position[1], handover_position[2] + 0.1)

    # Move the second robot to a final position
    final_position = [-0.7, -0.8, 0.15]  # Example final position
    executor.plan_and_move_to_xyz_facing_down("ur5e_1", final_position)

    # Put down the block
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

# Example usage
start_position = [-0.5, -0.6, 0.03]  # Example starting position
relay_race(start_position)