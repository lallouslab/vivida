from vivida.ida_vivida import cwks
from typing import Union

def get_cmt(ea: int, rptble: bool = False) -> Union[str, None]:
    """Get regular comment."""
    return cwks.getComment(ea)

def set_cmt(ea: int, comm: str, rptble: bool = False) -> None:
    """Set regular comment."""
    cwks.setComment(ea, comm)

def get_bytes(ea: int, size: int) -> bytes:
    """Get bytes."""
    return cwks.readMemory(ea, size)


def _get_nbyte(ea: int, n: int) -> int:
    try:
        return int.from_bytes(
            get_bytes(ea, n), cwks.ida_byteorder, signed=False) & (2**(n*8)-1)
    except:
        return 0
    
def get_byte(ea: int) -> int:
    return _get_nbyte(ea, 1)

def get_word(ea: int) -> int:
    return _get_nbyte(ea, 2)

def get_dword(ea: int) -> int:
    return _get_nbyte(ea, 4)

def get_qword(ea: int) -> int:
    return _get_nbyte(ea, 8)

def _put_nbyte(ea, v, n):
    try:
        b = v.to_bytes(v & (2 ** (8*n)-1), cwks.ida_byteorder)
        cwks.writeMemory(ea, b)
        return True
    except:
        return False

def put_byte(ea: int, v: int):
    return _put_nbyte(ea, v, 1)

def put_word(ea: int, v: int):
    return _put_nbyte(ea, v, 2)

def put_dword(ea: int, v: int):
    return _put_nbyte(ea, v, 4)

def put_qword(ea: int, v: int):
    return _put_nbyte(ea, v, 8)
