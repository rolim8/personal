import pygame
import random

from pygame.locals import *
from blocks import *

class TRS:
    screen = None
    map = [[Block.BLANK] * 10 for i in range(20)]
    STATUS = 0
    cbk = None

    def __init__(self, screen):
        TRS.screen = screen

    @staticmethod
    def action(key_pressed):
        if (key_pressed[K_LEFT] and TRS.check_action(TRS.cbk.x - 1, TRS.cbk.y, TRS.cbk.blk, TRS.cbk.angle)):
            TRS.cbk.x -= 1
        elif (key_pressed[K_RIGHT] and TRS.check_action(TRS.cbk.x + 1, TRS.cbk.y, TRS.cbk.blk, TRS.cbk.angle)):
            TRS.cbk.x += 1
        elif (key_pressed[K_UP] and TRS.check_action(TRS.cbk.x, TRS.cbk.y, TRS.cbk.blk, TRS.cbk.angle + 1)):
            TRS.cbk.angle += 1
        elif (key_pressed[K_DOWN] and TRS.check_action(TRS.cbk.x, TRS.cbk.y + 1, TRS.cbk.blk, TRS.cbk.angle)):
            TRS.cbk.y += 1

    @staticmethod
    def new_blk():
        TRS.cbk = Block(5, 0, random.randint(0, 6), 0)

    @staticmethod
    def check_action(x, y, blk, angle):
        tr = Block.type_rotate[blk][angle % 4]
        for b in range(4):
            bx, by = x + tr[b][0], y + tr[b][1]
            if (bx < 0 or bx > 9 or by < 0 or by > 19 or TRS.map[by][bx] != Block.BLANK):
                return False
        return True

    @staticmethod
    def check_drop():
        if TRS.check_action(TRS.cbk.x, TRS.cbk.y + 1, TRS.cbk.blk, TRS.cbk.angle):
            TRS.cbk.y += 1
        else:
            TRS.STATUS = 2

    @staticmethod
    def check_clear():
        blk = Block.type_rotate[TRS.cbk.blk][TRS.cbk.angle % 4]
        row = list({TRS.cbk.y + blk[i][1] for i in range(4)})
        row.sort()
        row.reverse()
        for b in range(4):
            TRS.map[TRS.cbk.y + blk[b][1]][TRS.cbk.x + blk[b][0]] = TRS.cbk.blk
        del_rows = 0
        for r in row:
            if not (Block.BLANK in TRS.map[r]):
                TRS.map.pop(r)
                del_rows += 1
        for d in range(del_rows):
            TRS.map.insert(0, [Block.BLANK for i in range(10)])

    @staticmethod
    def print_game():
        TRS.screen.fill((0, 0, 0))
        for row in range(20):
            for col in range(10):
                pygame.draw.rect(TRS.screen, Block.blk_color[TRS.map[row][col]], ((col * 21, row * 21), (20, 20)), 0)
        blk = Block.type_rotate[TRS.cbk.blk][TRS.cbk.angle % 4]
        for b in range(4):
            pygame.draw.rect(TRS.screen, Block.blk_color[TRS.cbk.blk],
                             (((TRS.cbk.x + blk[b][0]) * 21, (TRS.cbk.y + blk[b][1]) * 21), (20, 20)), 0)
