import time
from classes import accesspoint

class Gateway(accesspoint.AccessPoint):
    def __init__(self, ident, AP_type):
        accesspoint.AccessPoint.__init__(self)
        self.repeaters = []
        self.repeat_threads = []
        self.ident = ident
        self.AP_type = AP_type

    def check_in(self):
        if self.download_firmware==False and self.download_complete==False and self.upgrade_complete==False:          
            for item in self.repeaters:
                if item.download_complete == False:
                    break
                time.sleep(self.check_in_offset)
                self.download_firmware = True
        elif self.download_firmware==True and self.download_complete==False and self.upgrade_complete==False:
            self.download_complete = True
        elif self.download_firmware==True and self.download_complete==True and self.upgrade_complete==False:
            self.upgrade_complete = True