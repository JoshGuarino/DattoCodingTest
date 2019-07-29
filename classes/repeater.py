import time
from classes import accesspoint

class Repeater(accesspoint.AccessPoint):
    def __init__(self, ident, AP_type, sub_ident):
        accesspoint.AccessPoint.__init__(self)
        self.ident = ident + '.'+ sub_ident
        self.gw_pointer = int(ident)-1
        self.AP_type = AP_type

    def check_in(self):
        if self.download_firmware==False and self.download_complete==False and self.upgrade_complete==False:
            time.sleep(self.check_in_offset)
            self.download_firmware = True
            print('download started', self.AP_type, self.ident)
        elif self.download_firmware==True and self.download_complete==False and self.upgrade_complete==False:
            self.download_complete = True
            print('download complete', self.AP_type, self.ident)
        elif self.download_firmware==True and self.download_complete==True and self.upgrade_complete==False:
            self.upgrade_complete = True
            print('upgrade complete', self.AP_type, self.ident)