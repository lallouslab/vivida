from vivida.ida_vivida import cwks

def get_input_file_path():
    return cwks.getMeta("StorageName")

def get_import_module_qty():
    """Get number of imported modules"""
    return len(cwks.getImports())

