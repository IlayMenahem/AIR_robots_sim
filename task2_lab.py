from lab_ur5.motion_planning.motion_planner import MotionPlanner
from lab_ur5.motion_planning.geometry_and_transforms import GeometryAndTransforms
from lab_ur5.manipulation.manipulation_controller import ManipulationController
from lab_ur5.robot_inteface.robots_metadata import ur5e_1, ur5e_2
workspace_x_lim = [-1.0, 1]
workspace_y_lim = [-1.0, 1]


def relay_race(start_position: list[float], handover_position: list[float]) -> None:
    '''
    Makes the first robot pick up a block and meet the second robot at the handover position.

    Args:
        start_position: The position of the block to pick up.
        handover_position: The position to handover the block.

    Returns:
        None
    '''

    motion_planner = MotionPlanner()
    gt = GeometryAndTransforms.from_motion_planner(motion_planner)

    r1_controller = ManipulationController(ur5e_1["ip"],ur5e_1["name"],motion_planner,gt)
    r1_controller.speed = 2
    r1_controller.acceleration = 0.3

    r2_controller = ManipulationController(ur5e_2["ip"],ur5e_2["name"],motion_planner,gt)
    r2_controller.speed = 2
    r2_controller.acceleration = 0.3

    if not(workspace_x_lim[0] <= start_position[0] <= workspace_x_lim[1] and
        workspace_y_lim[0] <= start_position[1] <= workspace_y_lim[1]):
        raise ValueError("target_position must be within workspace_x_lim")

    if not(workspace_x_lim[0] <= handover_position[0] <= workspace_x_lim[1] and
        workspace_y_lim[0] <= handover_position[1] <= workspace_y_lim[1]):
        raise ValueError("target_position must be within workspace_x_lim")

    r1_controller.move_home()
    r2_controller.move_home()

    x_start, y_start, z_start = start_position
    r1_controller.pick_up(x_start, y_start, 0)
    r1_joints = [-2.183211628590719, -2.7464448414244593, -0.8477506041526794, -1.148409680729248, -1.5770967642413538, 2.22922682762146]
    r1_controller.moveJ(r1_joints)

    r2_joints =[1.0078383684158325, -0.3228061956218262, -0.9654921293258667, -0.3881130975535889, -1.599175755177633, 2.573286771774292]
    r2_controller.moveJ(r2_joints)

    tcp1_xyz = r1_controller.getActualTCPPose()
    tcp1_joints = r1_controller.getActualQ()

    print("r1 xyz")
    print(tcp1_xyz)
    print("r1 joints")
    print(tcp1_joints)


    tcp2_xyz = r2_controller.getActualTCPPose()
    tcp2_joints = r2_controller.getActualQ()

    print("r2 xyz:")
    print(tcp2_xyz)
    print("r2 joints:")
    print(tcp2_joints)

relay_race([0.3, 0, 0.03], [-0.5, -0.45, 0.15])
