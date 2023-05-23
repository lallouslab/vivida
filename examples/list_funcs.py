import idaapi, idautils, idc

def test_enum_funcs():
    n = idaapi.get_func_qty()
    f = idaapi.getn_func(0)
    name = idaapi.get_func_name(f.start_ea)

    print(f"n={n}, {f.start_ea:x}-{f.end_ea:x}: name={name}")

def test_idautils():
    for ifunc, func_ea in enumerate(idautils.Functions()):
        f = idaapi.get_func(func_ea)
        first_16bytes = idaapi.get_bytes(f.start_ea, 16).hex()
        print(f"#{ifunc} {f.start_ea:x} {f.end_ea:x} name={idaapi.get_func_name(f.start_ea)} first_16bytes={first_16bytes}")

if __name__ == "__main__":
    print(f"Passed arguments: {idc.ARGV}")
    print(f"Processor {idaapi.inf_get_procname()}")
    print(f"File type: {idaapi.inf_get_filetype()}")
    test_enum_funcs()
    test_idautils()
