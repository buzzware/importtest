import sys
sys.path.append('/flash/mpy')
sys.path.append('/flash/common')

from my_tuple import MyTuple
tuple = MyTuple(3)
print(tuple)

from sub.thing import Thing
thing = Thing()
print(thing)

from sub.Animal import Animal
animal = Animal()
print(animal)

