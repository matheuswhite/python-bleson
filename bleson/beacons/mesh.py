from bleson.core.roles import Advertiser
from bleson.core.types import Advertisement
from bleson.interfaces.adapter import Adapter
from bleson.logger import log


class MeshBeacon(Advertiser):
    def __init__(self, adapter, beacon_type: bytes, data: bytes):
        super().__init__(adapter)
        self.advertisement=Advertisement()
        self.beacon_type = beacon_type[0:1]
        self.data = data
        self.len = int(len(data) + 1).to_bytes(1, 'big')

        self.advertisement.raw_data=self.mesh_packet()
        print(f"Beacon Adv raw data = {self.advertisement.raw_data}")

    def mesh_packet(self):
        return self.len + self.beacon_type + self.data
