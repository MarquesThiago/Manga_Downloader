import os, sys 
sys.path.insert(0, './../Error/')
from .Pattern.Connection import * 

def errorMotFoundDriver(): 
    raise NotFoundDriver("Don't Found Driver in Path")

def errorNotFoundBrowser():
    raise NotFoundBrowser("Don't Found Browser")

def errorbrowserNotSupported():
    raise BrowserNotSupported("Application not support your Version Browser")

def errorFlagInvalied():
    raise FlagInvalied("Flag invalied")

