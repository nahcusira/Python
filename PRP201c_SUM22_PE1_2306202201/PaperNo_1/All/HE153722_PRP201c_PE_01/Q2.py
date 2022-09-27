try:
    fname = input("Enter file: ")
    if len(fname) < 1 :
        fname = "Text.txt"
    lines = open(fname, "r")
    for line in lines:
        words = line.split(', ')
        for word in words:
            if word == "\n":
                continue
            print(word.replace("\n", ""))
except Exception:
    print("File not found or unreadable.")