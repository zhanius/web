#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print("Weird" if n%2!=0 else "Not Weird")