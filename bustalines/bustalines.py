import os
from ctypes import *


class Map(Structure):
    _fields_ = [('count', c_ulong),
                ('filesize', c_ulong),
                ('begin', c_char_p),
                ('map', c_char_p)]


dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'c', 'bustalines.so')

lib = CDLL(filename)
lib.create_map.restype = POINTER(Map)
lib.print_line.argtypes = [POINTER(Map), c_int]
lib.remove_map.argtypes = [POINTER(Map)]
lib.get_line.restype = c_char_p
lib.get_map_len.restype = c_ulong


class FileMap:

    def __init__(self, filename: str):
        filename = c_char_p(str.encode(filename))
        self.map = lib.create_map(filename)

    def __len__(self) -> int:
        return lib.get_map_len(self.map)

    def __getitem__(self, item: int) -> str:
        s = lib.get_line(self.map, item)
        return str(c_char_p(s).value)

    def __del__(self) -> None:
        lib.remove(self.map)
