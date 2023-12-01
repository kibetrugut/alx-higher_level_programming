#!/usr/bin/python3
if_name_=="_main_"
import sys
arguments = sys.argv[1:]
result = sum(int(arg) for arg in arguments)
print(result)

