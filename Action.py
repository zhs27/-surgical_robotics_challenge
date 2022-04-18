import Point

class Action:
    def __init__(self, s_pt=None, e_pt=None, t='u2d'):
        self.start_pt = s_pt
        self.end_pt = e_pt
        self.op_type = t
