from bustalines import FileMap

fm = FileMap('README.md')
print(len(fm))
print(fm[0])
print(fm[len(fm) - 1])