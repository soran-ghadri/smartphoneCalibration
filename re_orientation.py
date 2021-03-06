import math
import numpy as np


def reorientation(
        v: list[list],
        teta_x: float,
        teta_y: float,
        teta_z: float) -> list[list]:
    """
    Accelerometer calibration.
    :param v:
    :param teta_x:
    :param teta_y:
    :param teta_z:
    :return: Velocity - matrix
    """
    R_x = np.array([[1, 0, 0],
                    [0, math.cos(teta_x), -math.sin(teta_x)],
                    [0, math.sin(teta_x), math.cos(teta_x)]])
    R_y = np.array([[math.cos(teta_y), 0, -math.sin(teta_y)],
                    [0, 1, 0],
                    [math.sin(teta_y), 0, math.cos(teta_y)]])
    R_z = np.array([[math.cos(teta_z), -math.sin(teta_z), 0],
                    [math.sin(teta_z), math.cos(teta_z), 0],
                    [0, 0, 1]])
    R = np.matmul(R_x, R_y, R_z)
    v_o = np.matmul(R, v)
    return v_o
