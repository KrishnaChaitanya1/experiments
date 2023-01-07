if __name__ == "__main__":
    with open(r"C:\Users\kchai\Downloads\UKPet.txt") as f:
        lines = f.readlines()
        l1 = [line.replace("\n", ",") for line in lines]

    with open(r"C:\Users\kchai\Downloads\UKPet_.txt", "w") as f:
        f.write("\n".join(l1))