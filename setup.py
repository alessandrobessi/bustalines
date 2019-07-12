import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='bustalines',
    version='1.0',
    author='Alessandro Bessi',
    author_email='alessandro.bessi@mail.com',
    description='Read specific lines of a text file without loading it in memory',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alessandrobessi/bustalines',
    packages=['bustalines'],
    package_dir={'bustalines': 'bustalines'},
    package_data={'bustalines': ['c/bustalines.so']},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
