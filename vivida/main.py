import argparse, sys, os
from vivida.utils import create_or_load, run_script_as_main

# ---------------------------------------------------------------------------
def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='vivida - An IDAPython bridge for vivisect')

    # Add arguments
    parser.add_argument('-c', '--create-new', dest='create_new', action='store_true', help='Toggle argument')
    parser.add_argument('-i', '--interactive', dest='interactive', action='store_true', help='Drop to interactive mode when the script terminates')
    parser.add_argument('-S', '--run-script', type=str, help='Run script')
    parser.add_argument('--', dest='script_args', nargs=argparse.REMAINDER)
    parser.add_argument('inputfile', type=str, help='Input file name to disassemble and analyze or the VIV workspace file name')

    # Parse the command-line arguments
    args, script_args = parser.parse_known_args()

    # Check if filename argument is provided
    if not args.inputfile:
        parser.print_help()
        exit(0)
    
    # Create or load the workspace
    fn = args.inputfile.strip()
    ok, vw = create_or_load(fn, always_create=args.create_new)
    if not ok:
        msg = vw
        print(f"vivida: failed to prepare workspace: {msg}")
        exit(1)

    exit_code, _globals = 0, {}

    vivida_dir = os.path.dirname(os.path.abspath(__file__))
    if vivida_dir not in sys.path:
        sys.path.append(vivida_dir)

    # Check if script argument is provided and run it
    if args.run_script:
        ok, info = run_script_as_main(args.run_script.strip(), args=script_args)
        if not ok:
            print(f"vivida: failed to run script: {info}")
            exit(1)
        exit_code, _globals = info
        from vivida.ida_vivida import cwks as vw
        _globals['vw'] = vw
        _globals['exit_code'] = exit_code

        # Forceful exit
        if exit_code is not None:
            sys.exit(exit_code)

    if args.interactive:
        import code
        code.interact(local=_globals)

    return exit_code

# ---------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    