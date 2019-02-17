#!/usr/bin/env python
print("\n".join(list(map(lambda x: ((x + " shark " + "doo! " * 6).rstrip() + "\n") * 3 + x + " shark!\n",
                         [i for i in ["Baby", "Daddy", "Mommy", "Grandpa", "Grandma"]]))).strip())
