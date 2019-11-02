#!/usr/bin/env python3

import sys
from time import sleep
from bleson import get_provider, MeshBeacon

# Get the wait time from the first script argument or default it to 10 seconds
WAIT_TIME = float(sys.argv[1]) if len(sys.argv)>1 else 10

try:
    adapter = get_provider().get_adapter()

    beacon = MeshBeacon(adapter=adapter, beacon_type=b'\x29', data=b'\xaa\xbb\xcc\xdd\x00\x03\xdd\xdd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    beacon.start()
    sleep(WAIT_TIME)

except KeyboardInterrupt:
    pass

finally:
    beacon.stop()
