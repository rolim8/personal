class Block:
    blk_color = [(255, 255, 255),
                 (255, 255, 0),
                 (255, 0, 255),
                 (0, 255, 255),
                 (255, 0, 0),
                 (0, 255, 0),
                 (0, 0, 255),
                 (32, 32, 32)]
    BLANK = 7
    type_coord = [[[-1, 0], [0, 0], [1, 0], [2, 0]] \
        , [[-1, 0], [0, 0], [1, 0], [0, 1]] \
        , [[-1, 0], [0, 0], [-1, 1], [0, 1]] \
        , [[-1, 0], [0, 0], [0, 1], [1, 1]] \
        , [[0, 0], [1, 0], [-1, 1], [0, 1]] \
        , [[-1, 0], [0, 0], [1, 0], [1, 1]] \
        , [[-1, 0], [0, 0], [1, 0], [-1, 1]]]
    type_rotate = []

    def __init__(self, x, y, blk, angle):
        self.x = x
        self.y = y
        self.blk = blk
        self.angle = angle

    @staticmethod
    def rotate(no):
        rt_all = []
        rt = Block.type_coord[no][:]
        cx, cy = 0, 0
        for b in range(4):
            rt[b][0], rt[b][1] = rt[b][0] * 4, rt[b][1] * 4
            cx += rt[b][0]
            cy += rt[b][1]
        cx = (cx) // 8 * 2 if no != 6 else (cx + 4) // 8 * 2
        cy = (cy) // 8 * 2 if no != 6 else (cy - 4) // 8 * 2
        rt_all.append(rt)
        for r in range(3):
            rt_new = []
            for b in range(4):
                rt_new.append([cx + (cy - rt[b][1]), cy - (cx - rt[b][0])])
            rt_all.append(rt_new)
            rt = rt_new
        for r in range(4):
            for b in range(4):
                rt_all[r][b][0] //= 4
                rt_all[r][b][1] //= 4
        return rt_all

    @staticmethod
    def init_rotate():
        for r in range(7):
            Block.type_rotate.append(Block.rotate(r))

