#!/usr/bin/env python

from setuptools import setup
from distutils.core import setup

from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
from Cython.Build import cythonize

extensions = [
  Extension("fastxml.splitter", ["fastxml/splitter.pyx"], language='c++', extra_compile_args=['-std=c++11'], include_dirs = ["/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1",
 "/usr/local/include",
" /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/8.0.0/include",
 "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include",
 "/usr/include"])
]

setup(name='fastxml',
      version="0.9.0",
      description='FastXML Extreme Multi-label Classification Algorithm',
      url="https://github.com/refefer/fastxml",
      cmdclass = {'build_ext': build_ext},
      ext_modules= cythonize(extensions),
      packages=['fastxml'],
      scripts=[
          "bin/fxml.py"
      ],
      install_requires=[
        "numpy>=1.8.1",
        "scipy>=0.13.3",
        "scikit-learn>=0.17",
        "Cython>=0.23.4",
      ],
      include_dirs=[numpy.get_include()],
      author='Andrew Stanton')
