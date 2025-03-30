import time
import logging
from lab_ur5.motion_planning.motion_planner import MotionPlanner
from lab_ur5.motion_planning.geometry_and_transforms import GeometryAndTransforms  # Import the class
from lab_ur5.manipulation.manipulation_controller import ManipulationController
# Configure logging
logging.basicConfig(level=logging.DEBUG)

def create_stack(block_positions: list[list[float]], target_location: list[float], robot_ip: str) -> None:
    '''
    stack the blocks at the target location

    Args:
    block_positions: list[list[float]]: list of block positions
    target_location: list[float]: target location to stack the blocks
    robot_ip: str: ip address of the robot

    Returns:
    None
    '''
    # Initialize the robot interface and motion planner
    planner = MotionPlanner()
    transforms = GeometryAndTransforms.from_motion_planner(planner) # Initialize the transforms class
    robot = ManipulationController(robot_ip,"ur5e_1",planner,transforms)
    # Move robot to home position
    robot.move_home()

    current_joint_angles = robot.getActualQ()
    current_tcp_pose = robot.getActualTCPPose()
    logging.debug(f"Current Joint Angles: {current_joint_angles}")
    logging.debug(f"Current TCP Pose: {current_tcp_pose}")

    # Stack cubes at the target location
    for i, block_pos in enumerate(block_positions):
        # Grasp the block
        robot.pick_up(block_pos[0], block_pos[1], block_pos[2] + 0.12)
        robot.put_down(target_location[0], target_location[1], target_location[2] + i * 0.05)

        # Wait for stability
        time.sleep(2)

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
