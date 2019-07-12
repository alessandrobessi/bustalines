import os
from ctypes import *
from typing import Union, List


class Map(Structure):
    _fields_ = [('count', c_ulong),
                ('filesize', c_ulong),
                ('begin', c_char_p),
                ('map', c_char_p)]


dir = os.path.dirname(__file__)
shared_object = os.path.join(dir, 'c', 'bustalines.so')

lib = CDLL(shared_object)
lib.create_map.restype = POINTER(Map)
lib.print_line.argtypes = [POINTER(Map), c_int]
lib.remove_map.argtypes = [POINTER(Map)]
lib.get_line.restype = c_char_p
lib.get_map_len.restype = c_ulong


class FileMap:

    def __init__(self, filename: str, encoding: str = 'latin1'):
        filename = c_char_p(str.encode(filename))
        self.map = lib.create_map(filename)
        self.encoding = encoding

    def __len__(self) -> int:
        return lib.get_map_len(self.map)

    def __getitem__(self, item: Union[int, slice]) -> Union[str, List[str]]:
        if isinstance(item, int):
            s = lib.get_line(self.map, item)
            return str(c_char_p(s).value.decode(self.encoding))
        elif isinstance(item, slice):
            lst = []
            start, stop, step = item.indices(lib.get_map_len(self.map))
            for i in range(start, stop, step):
                s = lib.get_line(self.map, i)
                lst.append(str(c_char_p(s).value.decode(self.encoding)))
            return lst

    def __del__(self) -> None:
        lib.remove(self.map)
