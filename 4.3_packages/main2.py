from sys import path

# You can use package from directory or zip
path.append('packages/extra_pckg.zip')

import extra.iota
from extra.good.alpha import FunA
import extra.good.best.sigma as egbs

print(extra.iota.FunI())
print(FunA())
print(egbs.FunS())


