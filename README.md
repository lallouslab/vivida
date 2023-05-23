# VivIDA

VivIDA is an IDAPython thin layer on top of [vivisect](https://github.com/vivisect/vivisect) the combined disassembler/static analysis/symbolic execution/debugger framework.

The goal behind VivIDA, is to let you run your IDAPython scripts _unmodified_ under `vivisect`.

# Install

1. Clone the repo
2. Install with `python setup.py` or `python setup.py develop`
3. You should now have a new script in %PYTHON%\Scripts called `vivida`

# Usage

```bash
usage: vivida [-h] [-c] [-i] [-S RUN_SCRIPT] [-- ...] filename

vivida - An IDAPython bridge for vivisect

positional arguments:
  filename              Input file name to disassemble and analyze or the VIV
                        workspace file name

options:
  -h, --help            show this help message and exit
  -c, --create-new      Toggle argument
  -i, --interactive     Drop to interactive mode when the script terminates
  -S RUN_SCRIPT, --run-script RUN_SCRIPT
                        Run script
  -- ...scripts: arg1 arg 2
```

## Example #1

We run `vivida` with the `list_funcs.py` script and the `Wizmo32.exe` binary. The first time, if no `Wizmo32.exe.viv` workspace file is available, then it is created. Subsequent calls will attempt to load the workspace first.

```
vivida -S examples\list_funcs.py c:\Tools\Bins\Wizmo32.exe
```

## Example #2

Interactive mode can be entered directly after a script is executed (if it was passed) or just after the workspace is loaded:

```bash
C:\>vivida c:\Tools\Bins\Wizmo32.exe -i
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import idautils
>>> [hex(x) for x in idautils.Functions()]
['0x401c17', '0x401c64', '0x401f50', '0x4023ba', '0x4020f1', '0x401cc8', '0x401a3c', '0x4022b1', '0x401a0a', '0x402342', '0x40233c', '0x401b90', '0x401d1c', '0x4019c6', '0x401afc', '0x401cec', '0x401d22', '0x402372', '0x402336', '0x402360', '0x40235a', '0x401320', '0x4015d0', '0x4018a5', '0x40160e', '0x401000', '0x402390', '0x40238a', '0x401ff5', '0x402312', '0x402028', '0x401600', '0x401609', '0x4022ee', '0x401130', '0x401090', '0x401330', '0x401e47', '0x402366', '0x401bad', '0x402348', '0x401eec', '0x401d28', '0x401866', '0x4023c0', '0x402300', '0x401fab', '0x401f20', '0x401caf', '0x4022f4', '0x4022fa', '0x4023b4', '0x401e96', '0x401e8a', '0x40237e', '0x4016d2', '0x401ced', '0x401cf3', '0x4016ca', '0x40230c', '0x4018a0', '0x4022bd', '0x40207d', '0x4020e4', '0x4022cb', '0x402318', '0x40180b', '0x40236c', '0x40234e', '0x40181f', '0x401b61', '0x401b74', '0x40206c', '0x402306', '0x402040', '0x401fda', '0x40200d', '0x40239c', '0x401a75', '0x4023a8', '0x4023a2', '0x401bd5', '0x401c02', '0x401c9e', '0x4018e6']
>>>
>>> vw                              
<vivisect.VivWorkspace object at 0x0000016AF4377ED0>

```

# Features and limitations

This is just the early release of `vivida` and there is a lot of work to be done to achieve more compatibility with IDAPython.
There are things that will not be possible or may not behave the same as in the real IDAPython.

Please see the [examples](./examples) directory.

## TODO

- [ ] Bytes
  - [x] get_bytes
  - [x] get_byte/get_word/etc.
  - [ ] ...
- [ ] Functions
  - [x] Enum
  - [ ] Flowchart
  - [ ] Items
- [ ] Segments
  - [x] Enum
  - [ ] Management
- [ ] IDA Info
  - [ ] min/max ea
  - [ ] start/main
  - [ ] ...
- [ ] X-refs
- [ ] Imports
- [ ] Exports
- [ ] Instruction decoding
- [ ] Debugger
- [ ] Items

Please feel free to contribute to this project.