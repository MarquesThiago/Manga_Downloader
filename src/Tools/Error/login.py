import os, sys 
sys.path.insert(0, "..\..\..")
from src.Tools.Error.Pattern.login import ErrorNotlogged

def ErrorNotLogged():
    raise ErrorNotlogged("User Not loggged")