import random
import time
from simulation_files import global_vars

class AccessPoint:
    def __init__(self):
        self.check_in_offset =  round(random.uniform(0, global_vars.offset), 2)
        self.download_time =  round(random.uniform(0, global_vars.offset), 2)
        self.upgrade_time =  round(random.uniform(0, global_vars.offset), 2)
        self.download_firmware = False
        self.download_complete = False
        self.upgrade_complete = False