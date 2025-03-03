from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor, compose_transformation_matrix  # Import the function
import numpy as np

def check_workspace_limits(executor, robot_name, x_range, y_range, z_range, step_size=0.05):
    """
    Check the robot's workspace limits by testing positions within the given ranges.
    """
    reachable_positions = []
    unreachable_positions = []

    for x in np.arange(x_range[0], x_range[1], step_size):
        for y in np.arange(y_range[0], y_range[1], step_size):
            for z in np.arange(z_range[0], z_range[1], step_size):
                target_pos = [x, y, z]

                # Check if the position is reachable
                target_transform = compose_transformation_matrix(executor.FACING_DOWN_R, target_pos)  # Use the imported function
                goal_config = executor.facing_down_ik(robot_name, target_transform)
                if goal_config:
                    reachable_positions.append(target_pos)
                    print(f"Position {target_pos} is reachable")
                else:
                    unreachable_positions.append(target_pos)
                    print(f"Position {target_pos} is unreachable")

    return reachable_positions, unreachable_positions

# Initialize the simulation environment and motion executor
env = SimEnv()
executor = MotionExecutor(env)

# Define the ranges to test (adjust these based on your setup)
x_range = [-1.0, 1.0]  # X-axis range
y_range = [-1.0, 1.0]  # Y-axis range
z_range = [0.0, 1.2]   # Z-axis range

# Check the workspace limits
reachable, unreachable = check_workspace_limits(executor, "ur5e_1", x_range, y_range, z_range)

# Print the results
print("Reachable positions:", reachable)
print("Unreachable positions:", unreachable)