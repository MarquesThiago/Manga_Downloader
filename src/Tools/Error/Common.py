import sys, os 
sys.path.insert(0, "./")
from .Pattern.Common import (ErrorUnknown)

def errorStranger():
    raise ErrorUnknown("Error Unknown!!!")