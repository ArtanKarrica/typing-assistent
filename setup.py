from setuptools import setup

APP = ['main.py']  # Your script name here
OPTIONS = {
    'argv_emulation': True,
    'packages': ['httpx', 'pynput', 'pyperclip'],
    'excludes': ['Xlib', 'PyQt4', 'PyQt5', 'qtpy', 'gtk', 'brotlicffi', 'click', 'pygments', 'rich', 'h2', 'socksio', 'trio', '_gdbm', '_io', '_overlapped', '_typeshed', 'jnius', 'curio', 'exceptiongroup'],
}


setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
