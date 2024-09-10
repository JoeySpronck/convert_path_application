import os

current_os = "w" if os.name == "nt" else "l"

def convert_path(path, to=current_os):
    '''
    This function converts paths to the format of the desired platform. 
    By default it changes paths to the platform you are currently using.
    This way you do not need to change your paths if you are executing your code on a different platform.
    It may however be that you mounted the drives differently. 
    In that case you may need to change that in the code below. 
    For example, change the Z for blissey (where I mounted it) to X (how you may have mounted it)
    If you add a linux path on a linux platform, or windows on windows, this function by default doesnt do anything.
    '''
    if to in ["w", "win", "windows"]:
        path = path.replace("/data/pathology", "Z:")
        path = path.replace("/data/pa_cpgarchive1", "W:")
        path = path.replace("/data/pa_cpgarchive2", "X:")
        path = path.replace("/data/pa_cpg", "Y:")
        path = path.replace("/data/temporary", "T:")
        path = path.replace("/", "\\")
    if to in ["u", "unix", "l", "linux"]:
        path = path.replace("Z:", "/data/pathology")
        path = path.replace("W:", "/data/pa_cpgarchive1")
        path = path.replace("X:", "/data/pa_cpgarchive2")
        path = path.replace("Y:", "/data/pa_cpg")
        path = path.replace("T:", "/data/temporary")
        path = path.replace("\\", "/")
    return path