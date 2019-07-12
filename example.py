from bustalines import FileMap

fm = FileMap('.gitignore')
print(len(fm))
print(fm[0])
print(fm[len(fm) - 1])
print(fm[0:4])
del fm
