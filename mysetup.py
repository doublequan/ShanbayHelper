# mysetup.py
from distutils.core import setup
import py2exe
import sys

#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 2,
        }
 
setup(
      name = 'ShanbayHelper',
      version = '1.0',
      windows = ['run.py',], 
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )


#command-line exe
#setup(console = ["Process_Management.py"])

#nono command-line windows exe
#setup(windows = ["run.py"], options = {'py2exe':{'includes':'sip'}})

# execute cmd command : python setup.py py2exe