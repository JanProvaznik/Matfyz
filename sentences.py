with open("a.txt",'r') as ifile:
    with open("b.txt","w") as ofile:
        char = ifile.read(1)
        while char:
            if char==".":
                ofile.write(char)
                ofile.write("\n")
                char = ifile.read(1)
            else:
                ofile.write(char)
                char = ifile.read(1)