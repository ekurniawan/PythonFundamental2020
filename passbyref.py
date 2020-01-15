def banner(message,border='-'):
    line = border*len(message)
    print(line)
    print(message)
    print(line)

banner("Hello PyThon")
banner("Hello Django","*")

