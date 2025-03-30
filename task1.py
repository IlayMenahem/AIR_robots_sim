from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import cv2
import numpy as np

def create_stack(block_positions, target_location):
    # Initialize the simulation environment and motion executor
    env = SimEnv()
    executor = MotionExecutor(env)

    # Add blocks to the world
    env.reset(randomize=False, block_positions=block_positions)
    move_to = [1.305356658502026, -0.7908733209856437, 1.4010098471710881, 4.102251451313659, -1.5707962412281837, -0.26543967541515895]
    executor.moveJ("ur5e_2", move_to)
    # Stack cubes at the target location
    for i, block_pos in enumerate(block_positions):

        executor.pick_up("ur5e_2", block_pos[0], block_pos[1], block_pos[2] + 0.12)

        target_pos = [target_location[0], target_location[1], target_location[2] + i * 0.05]  # Adjust height for stacking
        executor.plan_and_move_to_xyz_facing_down("ur5e_2", target_pos)


        executor.put_down("ur5e_2", target_pos[0], target_pos[1], target_pos[2] + 0.05)

        executor.wait(2)

# Example usage
block_positions = [
    [-0.7, -0.6, 0.03],
    [-0.7, -0.7, 0.03],
    [-0.7, -0.8, 0.03],
    [-0.7, -0.9, 0.03]
]
target_location = [-0.7, -0.5, 0.15]  # Example target location
create_stack(block_positions, target_location)