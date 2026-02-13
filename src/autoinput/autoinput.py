from enum import IntFlag
from typing import Callable, Any
import traceback as tracebk
import sys

class autoinput_type(IntFlag):
    STRING  = 0x00
    INTEGER = 0x01
    FLOAT   = 0x02
    BOOLYN  = 0x04
    BOOLTF  = 0x08
    ARRAY   = 0x10

class InputError(Exception):
    def __init__(self, ostr):
        super().__init__(ostr)

class ProgramError(Exception):
    def __init__(self, ostr):
        super().__init__(f"{ostr} This error is not your fault, it's a program's error (bug)")


def string_yes_no_to_bool(string: str) -> bool:
    if not string.lower() in set(["yes", "no", "y", "n"]):
        raise ValueError("Not a parsable input.")
    return string.lower() in set(["yes", "y"])

def string_true_false_to_bool(string: str) -> bool:
    if not string.lower() in set(["true", "false", "t", "f"]):
        raise ValueError("Not a parsable input.")
    return string.lower() in set(["true", "t"])


def one_space(string: str) -> str:
    res = ""
    prevspace = False
    for sym in string:
        if sym == " ":
            if not prevspace:
                res += sym
                prevspace = True
        else:
            res += sym
            prevspace = False
    return res


def autoinput(outstring: str, typeel, pipe_in: Callable[[str], str]=input, pipe_out: Callable[[str], None]=print, pipe_out_end_name: str="end", pipe_out_flush_name: str = "flush", parser=None) -> Any:
    """
    autoinput - input with automatic parsing and error handling.
    """
    array: bool = False
    def check_parser():
        nonlocal parser
        if not parser is None:
            raise ProgramError(f"Tried to load two parsers at the same time.")
    if typeel & autoinput_type.INTEGER:
        check_parser()
        parser = int
    if typeel & autoinput_type.FLOAT:
        check_parser()
        parser = float
    if typeel & autoinput_type.BOOLYN:
        check_parser()
        parser = string_yes_no_to_bool
    if typeel & autoinput_type.BOOLTF:
        check_parser()
        parser = string_true_false_to_bool
    if typeel & autoinput_type.ARRAY:
        array = True
    while 1:
        # block 1: print
        try:
            if pipe_out_end_name is None:
                pipe_out(outstring)
            else:
                out_kw = {pipe_out_end_name: ""}
                if not pipe_out_flush_name is None:
                    out_kw[pipe_out_flush_name] = True
                pipe_out(outstring, **out_kw)
        except Exception as e:
            print("Error while printing! Traceback:", file=sys.stderr)
            tracebk.print_exc()
            raise ProgramError("Error while printing.")
        # block 2: get input without parsing to types (excluding arrays) and return
        instr: str = pipe_in()
        if array:
            inobj = instr.split()
        else:
            inobj: str = instr
        # block 3: parse input and process errors
        try:
            try:
                if not parser is None:
                    if type(inobj) is str:
                        res = parser(inobj)
                    else:
                        res = []
                        for el in inobj:
                            res.append(parser(el))
                else:
                    res = inobj
                return res
            except (KeyboardInterrupt, EOFError):
                exit()
            except ValueError:
                raise InputError(one_space(f"Not {'an array of' if array else 'an' if typeel & autoinput_type.INTEGER else 'a'}\
                                                                    {'integer' if typeel & autoinput_type.INTEGER\
                                                                    else 'float' if typeel & autoinput_type.FLOAT\
                                                                    else 'bool (yes/no)' if typeel & autoinput_type.BOOLYN\
                                                                    else 'bool (true/false)' if typeel & autoinput_type.BOOLTF\
                                                                    else 'string or custom type'}."))
            except TypeError:
                raise ProgramError("Error while parsing input.")
        except InputError:
            tracebk.print_exc()
