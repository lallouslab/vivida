import vivisect
import logging

cwks : vivisect.VivWorkspace = None
"""Current workspace."""

ARGV = []
"""Passed arguments"""

class VivIDAScriptExitException(Exception):
    def __init__(self, exit_code: int):
        super().__init__()
        self.exit_code = exit_code


def set_cwks(vw : vivisect.VivWorkspace):
    """Set current workspace."""
    global cwks
    cwks = vw
    cwks.ida_byteorder = 'little' #;! TODO: get from wks meta
    cwks.ea64 = False # ;!TODO: get from wks meta


def set_argv(script_name: str, argv: list[str] = []):
    global ARGV
    ARGV = [script_name] + argv


def set_vivisect_log_level(level: int) -> None:
    logging.getLogger("vivisect").setLevel(level)
    logging.getLogger("vivisect.base").setLevel(level)
    logging.getLogger("vivisect.impemu").setLevel(level)
    logging.getLogger("vtrace").setLevel(level)
    logging.getLogger("envi").setLevel(level)
    logging.getLogger("envi.codeflow").setLevel(level)    