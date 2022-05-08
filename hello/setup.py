from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled

setup(ext_modules=cythonize([
    Extension(name="hello", sources=["hello.pyx"]),
    Extension(name="func", sources=["func.py"]),
    ],
    annotate=True))