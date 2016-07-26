import time
from creta import ETA

with ETA(120, strict=True) as eta:
    for s in eta:
        print s
        time.sleep(1)
