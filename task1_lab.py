import cv2
import numpy as np
import time
import logging
#from lab_ur5.robot_inteface.robot_interface import RobotInterfaceWithGripper
from lab_ur5.motion_planning.motion_planner import MotionPlanner
from lab_ur5.motion_planning.geometry_and_transforms import GeometryAndTransforms  # Import the class
from lab_ur5.manipulation.manipulation_controller import ManipulationController
# Configure logging
logging.basicConfig(level=logging.DEBUG)

def create_stack(block_positions, target_location, robot_ip):

    # Initialize the robot interface and motion planner
    planner = MotionPlanner()
    transforms = GeometryAndTransforms.from_motion_planner(planner) # Initialize the transforms class
    robot = ManipulationController(robot_ip,"ur5e_1",planner,transforms)
    # Move robot to home position
    robot.move_home()
    # for debugging 

    current_joint_angles = robot.getActualQ()
    current_tcp_pose = robot.getActualTCPPose()
    logging.debug(f"Current Joint Angles: {current_joint_angles}")
    logging.debug(f"Current TCP Pose: {current_tcp_pose}")

    # Stack cubes at the target location
    for i, block_pos in enumerate(block_positions):
        # Transform block position from world frame to robot frame
        #block_pos_robot = transforms.point_world_to_robot("ur5e_2", block_pos)#why would we need the transformation ? we need the point after its transfroamtion to the robot frame.

        # Move to block position (with gripper facing downwards)
        #target_pos = [block_pos_robot[0], block_pos_robot[1], block_pos_robot[2] + 0.12]
        #gripper_pose = transforms.get_gripper_facing_downwards_6d_pose_robot_frame("ur5e_2", target_pos, rz=0)
        #planner.plan_and_move_to_pose(robot, gripper_pose)
        #basically we change the coordinates of the block to the robot frame and then we find out how it would look (x,y,z) faqcing down and then we move the robot to that position.

        # Grasp the block
        robot.pick_up(block_pos[0], block_pos[1], block_pos[2] + 0.12)
        robot.put_down(target_location[0], target_location[1], target_location[2] + i * 0.05)

        # for debugging 
        #current_tcp_pose = robot.getActualTCPPose()
        #logging.debug(f"TCP Pose after grasping: {current_tcp_pose}")


        # Transform stack position from world frame to robot frame
        #stack_pos_world = [target_location[0], target_location[1], target_location[2] + i * 0.05]
        #stack_pos_robot = transforms.point_world_to_robot("ur5e_2", stack_pos_world)

        # Move to stack position (with gripper facing downwards)
        #gripper_pose = transforms.get_gripper_facing_downwards_6d_pose_robot_frame("ur5e_2", stack_pos_robot, rz=0)
        #planner.plan_and_move_to_pose(robot, gripper_pose)

        # Release the block
        #robot.release_grasp()

        # Wait for stability
        time.sleep(2)

   


def save_video(frames, filename):
    out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
    for frame in frames:
        out.write(frame)
    out.release()

# Example usage
block_positions = [
    [0.3, 0.0, 0.03],
    [0.4, 0.0, 0.03],
    [0.5, 0.0, 0.03],
    [0.6, 0.0, 0.03]
]
target_location = [0.7, 0.0, 0.03]  # just an example location
robot_ip = "192.168.0.10" 

create_stack(block_positions, target_location, robot_ip)