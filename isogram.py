def is_isogram(string):
    special = ["-", "_", " "]
    for i in special:
        string = string.replace(i, "")
    string=string.lower()
    return sum([string.count(y) > 1 for y in set(list(string))]) == 0
