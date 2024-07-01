# subprocess   - Capture_output


import subprocess

import sys

cmd = ['ping','127.0.0.1']

sub = subprocess.run(
    cmd, capture_output= True,
    text = True,encoding='cp850'
)

print(sub.stdout)