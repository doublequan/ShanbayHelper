# ShanBayHelper

Windows application designed for adding huge number of words into shanbay account.

Used Python libs: PyQt4, selenium, py2exe, etc.

python source code includes:

	run.py
	ShanbayHelperBackend.py
	ShanbayHelperGUI.py

For py2exe compiling:

	mysetup.py

Compiled x64 version for windows7 or above version: (absent)

	/dist/*
or

	dist.rar

Please note that this version cannot be used in 32bit windows

### compiling time and runtime errors regarding PyQt4 and py2exe

please visit my article [HERE](http://doublequan.github.io/2016/03/27/python-PyQt-py2exe/ "使用Py2exe打包PyQt4程序到exe").

### for selenium 

Used Chrome brower in the program. Make sure you have installed Chrome brower and put **chromedriver.exe** in the dictionary.

	/dist/chromedriver.exe

If you met the error: 

	selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome version must be >= 46.0.2490.0

Please update your Chrome version.

