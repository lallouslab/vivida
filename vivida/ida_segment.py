from vivida.ida_vivida import cwks
from vivida.ida_range import range_t

class segment_t(range_t):
    """Segment structure."""
    def __init__(self, start_ea, end_ea, name:str=None, filename:str=None):
        super().__init__(start_ea, end_ea)
        self.name = name
        self.filename = filename
    
    @staticmethod
    def from_vseg(seg):
        return segment_t(seg[0], seg[0] + seg[1], seg[2], seg[3])

def get_segm_qty() -> int:
    """Get number of segments"""
    return len(cwks.getSegments())

def getseg(ea: int) -> segment_t:
    """Get pointer to segment structure by address."""
    seg = cwks.getSegment(ea)
    return segment_t.from_vseg(seg) if seg else None

def getnseg(n: int) -> segment_t:
    """Get pointer to segment structure by number."""
    return segment_t.from_vseg(cwks.getSegments()[n])
