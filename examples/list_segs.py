import idaapi, idautils

def test_enum_segs():
    n = idaapi.get_segm_qty()

    for i in range(n):
        seg = idaapi.getnseg(i)
        print(f"{seg.start_ea:x}-{seg.end_ea:x} {seg.name}")
        #print(f"Bytes: {idaapi.get_bytes(seg.start_ea, 55).hex()}")
    print(f"n={n}")

def test_idautils_enum_segs():
    for iseg, seg_ea in enumerate(idautils.Segments(), start=1):
        seg = idaapi.getseg(seg_ea)
        print(f"#{iseg} {seg.start_ea:x}-{seg.end_ea:x} {seg.name}")

if __name__ == "__main__":
    test_enum_segs()
    test_idautils_enum_segs()