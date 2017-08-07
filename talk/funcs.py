
from views import *

def getcat():
    r = Cat.objects.all()
    r = list(r)
    return r