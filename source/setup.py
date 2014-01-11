from distutils.core import setup
import py2exe

setup(
    windows=[{"script":"main.py", "icon_resources": [(1, "ac4.ico")]}],
    data_files = [('imageformats', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll'])],
    options={"py2exe": {"packages":["gzip"],"includes":["sip"]}}
)