import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
      print("Weird")
      sys.exit(0)
    if n > 2 and n < 5:
      print("Not Weird")
      sys.exit(0)
    if n > 6 and n <= 20:
      print("Weird")
      sys.exit(0)
    else:
      print("Not Weird")
      sys.exit(0)

