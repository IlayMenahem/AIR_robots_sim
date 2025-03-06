from time import sleep

from lab_ur5.motion_planning.motion_planner import MotionPlanner
from lab_ur5.motion_planning.geometry_and_transforms import GeometryAndTransforms
from lab_ur5.manipulation.manipulation_controller import ManipulationController
from lab_ur5.robot_inteface.robots_metadata import ur5e_1, ur5e_2

def meet_at_middle(robot1, robot2, axis='x', mid_point=[-0.4, -0.6], offset=0.08):
    r1_point = mid_point.copy()
    r2_point = mid_point.copy()

    if axis == "x":
        r1_point[0] += offset
        r2_point[0] -= offset
    elif axis == "y":
        r1_point[1] += offset
        r2_point[1] -= offset

    robot1.plan_and_move_to_xyzrz(r1_point[0], r1_point[1], 0.2, 0)
    robot2.plan_and_move_to_xyzrz(r2_point[0], r2_point[1], 0.2, 0)

def relay_race(start_position, end_position):
    motion_planner = MotionPlanner()
    gt = GeometryAndTransforms.from_motion_planner(motion_planner)
    robot1 = ManipulationController(ur5e_1["ip"], ur5e_1["name"], motion_planner, gt)
    robot2 = ManipulationController(ur5e_2["ip"], ur5e_2["name"], motion_planner, gt)

    robot1.speed = 0.3
    robot1.acceleration = 0.3
    robot2.speed = 0.3
    robot2.acceleration = 0.3

    robot1.move_home()
    robot2.move_home()

    robot1.pick_up(start_position[0], start_position[1], start_position[2])

    meet_at_middle(robot1, robot2, axis='x', mid_point=[-0.4, -0.6])

    robot1.grasp_object()
    robot2.release_object()

    robot2.put_down(end_position[0], end_position[1], end_position[2])

    sleep(5)


if __name__ == "__main__":
    initial_position = [0.369, 0.0, 0.03]
    end_position = [-0.72, -0.5, 0.03]
    relay_race(initial_position, end_position)
