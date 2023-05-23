import os, sys, runpy, traceback
import vivisect
from vivida.ida_vivida import set_cwks, set_argv, VivIDAScriptExitException
from vivida import VIV_EXT
from typing import Tuple, Union, List, Dict, Any

def create_or_load(filename: str, always_create=False) -> Tuple[bool, Union[vivisect.VivWorkspace, str]]:
    if filename.endswith(VIV_EXT) and os.path.exists(filename):
        always_create = False
        viv_fn = filename
    else:
        viv_fn = filename + VIV_EXT

    try:
        vw = vivisect.VivWorkspace()
        if always_create or not os.path.exists(viv_fn):
            vw.loadFromFile(filename)
            vw.analyze()
            vw.saveWorkspace(fullsave=True, filename=viv_fn)
        else:
            vw.loadWorkspace(viv_fn)
        set_cwks(vw)
        return (True, vw)
    except Exception as e:
        return (False, f"Exception:: {e!s}")


def run_script_as_main(
        script_path: str, 
        args: List[str] = []) -> Tuple[bool, Union[Tuple[Union[int, None], Dict[Any, Any]], str]]:
    if not os.path.exists(script_path):
        return (False, f"Script not found: {script_path}")

    script_path = os.path.abspath(script_path)
    set_argv(script_path, args)
    
    exit_code = None
    _globals = {}
    cwd = os.getcwd()
    added_cur_dir = False
    try:
        os.chdir(os.path.dirname(script_path))
        if '.' not in sys.path:
            added_cur_dir = True
            sys.path.append('.')
        _globals = runpy.run_path(script_path, run_name="__main__")
    except VivIDAScriptExitException as e_exit:
        exit_code = e_exit.exit_code
    except Exception as e:
        return (False, traceback.format_exc())
    finally:
        if added_cur_dir and '.' in sys.path:
            sys.path.remove('.')
        os.chdir(cwd)

    return (True, (exit_code, _globals))
