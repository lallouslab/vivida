from vivida.ida_vivida  import cwks
from vivida.ida_segment import segment_t

def Functions():
    return iter(cwks.getFunctions())

def Segments():
    """
    Get list of segments (sections) in the binary image

    @return: List of segment start addresses.
    """
    for vseg in cwks.getSegments():
        yield vseg[0]
