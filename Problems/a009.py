n = input()

print(*[chr((int(ord(x) - 7))) for x in n], sep="")
