# bustalines
Read specific lines of a text file without loading it in memory.

A C backend leverages `mmap` to map a text file into the virtual
address space of the process. This allows to read specific lines 
of a text file without loading it in memory.

This comes in handy when you need to sample lines from a large 
text file (e.g. 100Gb) that does not fit in memory. Basically, 
instead of allocating a number of bytes equal to the size of the
file, you only allocate a number of bytes equal to the
number of lines times the size of a pointer to char (which is
4 bytes in 32-bit machines and 8 bytes in 64-bit machines).

The class FileMap has four methods:
* `__init__`: to create the mapping
* `__len__`: to retrieve the number of lines mapped
* `__getitem__`: to access to a given line
* `__del__`: to unmap and free memory

The class FileMap can be easily and nicely integrated with the
Dataset classes of deep learning frameworks like PyTorch and
MxNet (see examples).
