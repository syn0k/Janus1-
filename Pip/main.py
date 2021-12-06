# import module progress
# The package can be installed through pip (this is the recommended method):
# pip install progressbar

import time
import progressbar

for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)