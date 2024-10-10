from pprint import pprint
import requests
from math import pi
from threading import Thread

def introspection_info(obj):
    intro = {
        'name': obj.__name__ if hasattr(obj, '__name__') else None,
        'type': type(obj),
        'magic_attrs': [a for a in dir(obj) if not callable(getattr(obj, a)) and a.startswith('_')],
        'magic_methods': [m for m in dir(obj) if callable(getattr(obj, m)) and m.startswith('_')],
        'attrs': [a for a in dir(obj) if not callable(getattr(obj, a)) and not a.startswith('_')],
        'methods': [m for m in dir(obj) if callable(getattr(obj, m)) and not m.startswith('_')],
        'module': obj.__module__ if hasattr(obj, '__module__') else __name__,
    }
    return intro
    

# pprint(introspection_info(requests))
# pprint(introspection_info(Thread))
pprint(introspection_info(pi))
# print(Thread.__module__)
# pprint(type(introspection_info))
# print(type(43).numerator)
# print(dir(requests))
# pprint(dir(pi))

