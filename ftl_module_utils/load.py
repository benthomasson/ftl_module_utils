
import sys


def patch():
    module = __import__('ftl_module_utils')
    print(module)
    sys.modules['ansible'] = module
