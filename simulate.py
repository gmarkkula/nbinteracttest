import numpy as np

def run_simulation(time_step, end_time, lv_speed, lv_dot, lv_dec, limit_lv_speed, lv_min_speed):
    time_stamp = np.arange(0, end_time, time_step)
    n_time_steps = len(time_stamp)
    dot_time_step = np.nonzero(time_stamp >= lv_dot)[0][0]
    acc = np.zeros(len(time_stamp))
    acc[dot_time_step:] = -lv_dec
    speed = np.full(len(time_stamp), lv_speed)
    speed += np.cumsum(acc * time_step)
    if limit_lv_speed:
        speed = np.maximum(speed, lv_min_speed)
    return (time_stamp, speed)