import pandas as pd
import numpy as np

with open(r"C:\Users\kchai\Downloads\UKPet_.txt", "r+") as f:
    contents = list(f.readlines())          
    for i in range(400, len(contents), 400):
        if i % 400 == 0:
            contents.insert(i, "--------------------------------------- 400 --------------------------------------------------------------\n")

    f.seek(0)
    f.write("".join(contents))
    f.truncate()
    f.close()
