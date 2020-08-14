def ColIdxToXlName(idx):
    if idx < 1:
        raise ValueError("Index is too small")
    result = ""
    while True:
        if idx > 26:
            idx, r = divmod(idx - 1, 26)
            result = chr(r + ord('a')) + result
        else:
            return chr(idx + ord('a') - 1) + result

print(ColIdxToXlName(int(input())))