import foo.cat

foo.cat.miau()

from bar.dog import *

wuff()

import hownot

print "-----------------------------------------------------------------"
print "only importing the package will not make its modules available,\n\
when not specified in its __init__.py"

print "test for yourself in interavtive mode: there is no hownot.animal !"
