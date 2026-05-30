import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danish/Downloads/Auto--Agesis-main/install/ros2_streamer'
