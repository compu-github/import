# -*- coding: utf-8 -*-
import builtins
import math

import scipy

from import_monster import methods_importer

print(methods_importer("__import__", ["builtins"]))
print(methods_importer("nothing", ["builtins"]))
print(methods_importer("sum", [math, builtins, scipy]))
