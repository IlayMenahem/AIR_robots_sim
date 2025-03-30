from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import cv2
import os

def relay_race(start_position):
    env = SimEnv(render_mode='human')
    executor = MotionExecutor(env)
    env.reset(randomize=False, block_positions=[start_position])

    executor.pick_up("ur5e_2", start_position[0], start_position[1])

    pi = 3.14159265359

    angle = pi*(8.925/32)
    p = -0.315*pi
    joint_positions = [angle, p, -p, pi, -pi/2, 0]
    executor.moveJ("ur5e_2", joint_positions, speed=3)
    executor.moveJ("ur5e_1", joint_positions, speed=3)

    executor.wait(4)


start_position = [-0.7, -0.8, 0.03]
relay_race(start_position)