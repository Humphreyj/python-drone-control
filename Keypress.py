import pygame


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def getKey(keyName):
    answer = False
    for event in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    # this line formats the keypress in the required format by pygame
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        answer = True
    pygame.display.update()

    return answer


def main():
    while getKey("w"):

        print("You have pressed W")


if __name__ == '__main__':
    init()
    while True:
        main()
