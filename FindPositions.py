import os

def get_needle():
  needle = [0, 0, 0, 0, 0, 0, 0]
  cmd = "cd ~"
  os.system(cmd)
  cmd = "cd surgical_robotics_challenge"
  os.system(cmd)
  cmd = "rostopic echo -n1 /ambf/env/Needle/State"
  needle_state = os.system(cmd)
  print(needle_state)
