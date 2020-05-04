
try:
    from ucollections import namedtuple
except ImportError:
    from collections import namedtuple

MyTuple = namedtuple('MyTuple',['size'])
