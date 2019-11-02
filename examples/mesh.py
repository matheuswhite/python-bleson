#!/usr/bin/env python3

import sys
from time import sleep
from bleson import get_provider, Observer
from bleson import MeshBeacon

# Get the wait time from the first script argument or default it to 10 seconds
WAIT_TIME = int(sys.argv[1]) if len(sys.argv)>1 else 10

def on_advertisement(advertisement):
    print(advertisement.raw_data.hex())
    print(advertisement.address)
    print(advertisement)
    # exit(1)

adapter = get_provider().get_adapter()

observer = Observer(adapter)
observer.on_advertising_data = on_advertisement

observer.start()
sleep(WAIT_TIME)
observer.stop()

# 182b00dddd0000000000000000000000000000000000000000


