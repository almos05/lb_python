from classes import Field, Rook, Teleport

field = Field((10, 10))

field.gen()

while True:
    num_choose = input("\tChoose unit:\nRook - 1, Teleport - 2\n")

    if num_choose.strip() == "1":
        player = Rook(field)
        break
    elif num_choose.strip() == "2":
        player = Teleport(field)
        break

player.field.out()
while (command := input().lower().strip()) != 'e':
    player.move(command)
    field.out()
