if __name__ == "__main__":
    
    with open(r"C:\Users\kchai\Downloads\UK Pet.txt") as f:
        l2 = []
        list_of_emails = f.readlines()
        for i in list_of_emails:
            sublist = i.split(",")
            for item in sublist:
                sublist_2 = item.lstrip().rstrip()
                if sublist_2 == "":
                    pass
                else:
                    l2.append(sublist_2)
    
    with open(r"C:\Users\kchai\Downloads\UKPet.txt", "w") as f:
        f.write(",\n".join(l2))
