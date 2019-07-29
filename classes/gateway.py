from classes import accesspoint

class Gateway(accesspoint.AccessPoint):
    def __init__(self, ident, AP_type):
        accesspoint.AccessPoint.__init__(self)
        self.repeaters = []
        self.repeat_threads = []
        self.ident = ident
        self.AP_type = AP_type