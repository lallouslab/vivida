from vivida.ida_vivida import cwks
from vivida.ida_range import range_t

class func_t(range_t):
    """Function structure."""
    def __init__(self, start_ea, end_ea):
        super().__init__(start_ea, end_ea)
        self.flags = 0

def get_func_qty():
    """Get total number of functions in the program"""
    return len(cwks.getFunctions())

def get_func(ea) -> func_t:
    func_ea = cwks.getFunction(ea)
    if func_ea is None:
        return None
    
    f = func_t(func_ea, func_ea + cwks.getFunctionMeta(func_ea, 'Size', 1))
    return f

def get_func_name(ea: int) -> str:
    """Get function name."""
    return cwks.getName(ea)

def getn_func(n: int) -> func_t:
    """Get pointer to function structure by number."""
    func_ea = cwks.getFunctions()[n]
    return get_func(func_ea)