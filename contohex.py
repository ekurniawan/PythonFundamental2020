def convert(bil):
    try:
        data = int(bil)
        print("Conversion Success")
    except ValueError:
        print("Error Convert")
        data = -1
    return data

print(convert("ss"))