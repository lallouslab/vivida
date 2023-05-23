from vivida.ida_vivida import cwks

#---------------------------------------------------------------------
(
  f_EXE_old,           # MS DOS EXE File
  f_COM_old,            # MS DOS COM File
  f_BIN,                # Binary File
  f_DRV,                # MS DOS Driver
  f_WIN,                # New Executable (NE)
  f_HEX,                # Intel Hex Object File
  f_MEX,                # MOS Technology Hex Object File
  f_LX,                 # Linear Executable (LX)
  f_LE,                 # Linear Executable (LE)
  f_NLM,                # Netware Loadable Module (NLM)
  f_COFF,               # Common Object File Format (COFF)
  f_PE,                 # Portable Executable (PE)
  f_OMF,                # Object Module Format
  f_SREC,               # Motorola SREC (S-record)
  f_ZIP,                # ZIP file (this file is never loaded to IDA database)
  f_OMFLIB,             # Library of OMF Modules
  f_AR,                 # ar library
  f_LOADER,             # file is loaded using LOADER DLL
  f_ELF,                # Executable and Linkable Format (ELF)
  f_W32RUN,             # Watcom DOS32 Extender (W32RUN)
  f_AOUT,               # Linux a.out (AOUT)
  f_PRC,                # PalmPilot program file
  f_EXE,                # MS DOS EXE File
  f_COM,                # MS DOS COM File
  f_AIXAR,              # AIX ar library
  f_MACHO,              # Mac OS X Mach-O
  f_PSXOBJ,             # Sony Playstation PSX object file
) = range(27)

_file_format_to_file_type = {
    "pe":       f_PE,
    "ihex":     f_HEX,
    "elf":      f_ELF,
}

def inf_get_filetype():
    return _file_format_to_file_type.get(cwks.getMeta('Format'), f_BIN)

#---------------------------------------------------------------------
_arch_to_procname = {
    "i386":     "metapc",
    "amd64":    "metapc",
}

def inf_get_procname():
    name = cwks.getMeta('Architecture')
    return _arch_to_procname.get(name, name)
