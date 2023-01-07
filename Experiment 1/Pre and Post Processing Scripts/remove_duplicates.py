import pandas as pd

df = pd.read_csv(r"C:\Users\kchai\Downloads\UKPet.txt", header=None)

df.drop(1, axis=1, inplace=True)

df.drop_duplicates(inplace = True)

df.to_csv(r"C:\Users\kchai\Downloads\UKPet.txt", header = None, index = None, sep = ',', mode='w+', lineterminator='\n')