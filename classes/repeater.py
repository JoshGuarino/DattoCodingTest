from classes import accesspoint

class Repeater(accesspoint.AccessPoint):
        def __init__(self, ident, AP_type, sub_ident):
            accesspoint.AccessPoint.__init__(self)
            self.ident = ident + '.'+ sub_ident
            self.AP_type = AP_type