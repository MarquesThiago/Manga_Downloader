import os, sys 
sys.path.insert(0, './../Error/')
from .Pattern.Controllers.alternate_page import (KeyError, NotFoundButtonAlternPg )

def ErrorIncorrectParseKey():
    raise KeyError("Not indentificaed key persed")

def ErrorButtonAlternate():
    raise NotFoundButtonAlternPg("Not Found Button to Alternage Page")