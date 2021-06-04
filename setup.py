# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('main.py', targetName='todo.exe', base = "Win32GUI")]
excludes = ['email', 'html', 'http', 'logging', 'tkinter', 'unittest', 'multiprocessing', 'lib2to3', 'xml', 'test']
include = ['reminders']
include_files = ['dbs', 'web_notify.ico', 'web.png']
zip_include_packages = ['collections', 'importlib', 'date']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': include,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'Todo',
        'include_files': include_files,
    }
}

setup(name='todo',
      version='0.0.12',
      description="It's russian todo app!",
      executables=executables,
      options=options)
