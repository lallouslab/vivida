"""
getXrefsFrom

# Reference Types
# NOTE: All XREFs may have type specific flags
REF_CODE   = 1 # A branch/call
REF_DATA   = 2 # A memory dereference
REF_PTR    = 3 # A pointer immediate (may be in operand *or* part of LOC_PTR)

ref_type_names = {
    REF_CODE: "Code",
    REF_DATA: "Data",
    REF_PTR: "Pointer",
}


"""