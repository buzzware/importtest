import os
import site
import sys

thisPath = os.path.dirname(__file__)
site.addsitedir(os.path.normpath(thisPath))
site.addsitedir(os.path.normpath(thisPath)+'/../common')


from my_tuple import MyTuple
tuple = MyTuple(3)
print(tuple)

from sub.thing import Thing
thing = Thing()
print(thing)

from sub.Animal import Animal
animal = Animal()
print(animal)

