from vivida.ida_vivida import VivIDAScriptExitException

BADADDR = 0xFFFFFFFFFFFFFFFF

def qexit(code):
    raise VivIDAScriptExitException(code)