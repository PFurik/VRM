# System (Default Lib.)
import sys
# Own library for robot control (kinematics), visualization, etc. (See manipulator.py)
import manipulator


def main():
    # Initial Parameters -> ABB IRB910SC 
    # Product Manual: https://search.abb.com/library/Download.aspx?DocumentID=3HAC056431-001&LanguageCode=en&DocumentPartId=&Action=Launch

    # Working range (Axis 1, Axis 2)
    axis_wr = [[-140.0, 140.0],[-150.0, 150.0], [-120.0,120.0]]
    # Length of Arms (Link 1, Link2)
    arm_length = [0.3, 0.25, 0.1]


    # DH (Denavit-Hartenberg) parameters
    theta_0 = [0.0, 0.0, 0.0]
    a = [arm_length[0], arm_length[1], arm_length[2] ]
    d       = [0.0, 0.0, 0.0]
    alpha   = [0.0, 0.0, 0.0]

    # Initialization of the Class (Control Manipulator)
    # Input:
    #   (1) Robot name         [String]
    #   (2) DH Parameters      [DH_parameters Structure]
    #   (3) Axis working range [Float Array]
    scara = manipulator.Control('ABB IRB 910SC (SCARA)', manipulator.DH_parameters(theta_0, a, d, alpha), axis_wr)

    # Test Results (Select one of the options -> See below)
    test_kin = 'FK'

    if test_kin == 'FK':
        scara.forward_kinematics(1, [-140, -150, -120], True)
    elif test_kin == 'IK':
        scara.inverse_kinematics([0.3, 0.2, 25],0, True)
    elif test_kin == 'BOTH':
        scara.forward_kinematics(0, [0.0, 45.0, 25], True)
        scara.inverse_kinematics(scara.p,0, False)

    # 1. Display the entire environment with the robot and other functions.
    # 2. Display the work envelope (workspace) in the environment (depends on input).
    # Input:
    #  (1) Work Envelop Parameters
    #       a) Visible                   [BOOL]
    #       b) Type (0: Mesh, 1: Points) [INT]
    scara.display_environment([True, 1])

if __name__ == '__main__':
    sys.exit(main())