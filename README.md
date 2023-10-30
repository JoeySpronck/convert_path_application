# Simple convert path application
A simple application (`.pyw` file) and standalone function (in the `.py` file) that easily converts paths accroding to a adjustable mapping. 

I use the function in all my projects, allowing me to work on both linux and windows systsms without needing to change the paths all the time. The `current_os` variable makes sure that `convert_path(your_path)` will always return the path that corresponds to the system you are currently running your code in. 

If you are on a linux system and you need a windows path for example, you can also specify this as follows: `convert_path(your_path, 'w')` with `'w'`/`'windows'` for windows; for unix paths use `"u"`/`"unix"`/`"l"`/`"linux"`/`"m"`/`"mac"`.

The `.pyw` application is a nice addition you can use to quickly convert a path when you are not working in python. For example place a shortcut to it on your desktop. 

## Adjust to your needs
Adjust the `convert_path.py` file to your needs. This python file contains the (standalone) function that can be used in your projects, but is also used in the application. Change or add mappings according to your mounted drives. 

## Optionally build the app
You can directly use/ make a shortcut to the `convert_path_application.pyw` file. The `.pyw` extension is basically `.py`. But with the additional 'w', launching the execuatble or `.pyw` doesn't launch an additional command line window because its in 'windowed' mode.

You can also make an executable out of it, with its own application icon etc.
- `python -m pip install pyinstaller`
- `pyinstaller --onefile convert_path_application.pyw`
- After this you can find the executable in the `dist` directory

## Additional notes
For me a conda environment with pathlib installed did not work (could also be a version thing). Simply make a new conda env without it, and try again. The app itself runs in its own environment, the one from which it is created, therefore it complained about pathlib's backend stuff not being compatible. 




