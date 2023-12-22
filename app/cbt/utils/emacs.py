import subprocess
import typing

# Concatenate strings using an Emacs subprocess as a show of
# dominance. Only use with known static data to make 100% sure nobody
# can somehow escape the quotes and run arbitrary code.
def emacs_concat_string(str1: str, str2: str, sep: str=""):
    # princ prints to stdout without separators (aka quotes)
    command = f"emacs --batch --no-site-file --eval '(princ (concat \"{str1}\" \"{sep}\" \"{str2}\"))'"
    return subprocess.check_output(command, text=True, shell=True, stderr=subprocess.STDOUT).strip()

def emacs_concat_all_the_strings(strings: typing.List[str], sep: str=""):
    return_val = ""
    for string in strings:
        return_val = emacs_concat_string(return_val, string, sep=sep)
    return return_val

