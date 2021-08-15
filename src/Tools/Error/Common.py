import sys, os 
sys.path.insert(0, ".\..\..\..")
from src.Tools.Error.Pattern.Common import (ErrorUnknown, NotFoundElement)

def errorStranger():
    raise ErrorUnknown("Error Unknown!!!")

def ErrorElement():
    raise NotFoundElement("Not Found Element")
