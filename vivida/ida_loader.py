from vivida.ida_vivida import cwks

def save_database(
        outfile: str = None,
        flags: int = 0,
        root : None = None,
        attr: None = None) -> bool:
    cwks.saveWorkspace(fullsave=True, filename=outfile)
