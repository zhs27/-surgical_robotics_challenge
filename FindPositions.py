import os

def get_needle():
  needle = [0, 0, 0, 0, 0, 0, 0]
  cmd = "rostopic echo -n1 /ambf/env/Needle/State"
  needle_state = os.system(cmd)
  print(needle_state)
