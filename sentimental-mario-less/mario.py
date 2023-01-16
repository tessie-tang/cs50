

while True:
    height = input("Height: ")
    if not height.isnumeric():
        continue
    height = int(height)
    if (height > 0 and height < 9):
        break

for i in range(1, height + 1):
    line = ""
    for j in range(1, height + 1):
        if (j <= (height - i)):
            line += " "
        else:
            line += "#"
    print(line)
