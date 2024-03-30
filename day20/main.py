from typing import NamedTuple

class Modu(NamedTuple):
    typu: str
    name: str
    dest: tuple[str, ...]

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
