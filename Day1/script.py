import re
import sys

with open("Day1\Input\input","r") as file:
    input=file.read().strip()

total=0;
for i,items in enumerate(input.split('\n')):

    digits=[]
    for item in items:
        if item.isdigit():
            digits.append(int(item))
    total+=digits[0]+digits[-1]

print(total)
