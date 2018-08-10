from random import shuffle, randrange
def make_maze(w, h):
    maze= [[[False for i in range(4)] for j in range(w)] for k in range(h)] #up,left,down,right is the order of sides, True means there is wall
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|    "] * (w+1) for _ in range(h)] + [[]]
    hor = [["+----"] * w + ['+'] for _ in range(h + 1)]
    startrow=randrange(h)
    finishrow=randrange(h)
    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                if((xx==-1 and yy==startrow) or (xx==w and yy==finishrow)):
                    if xx == x: hor[max(y, yy)][x] = "+    "
                    if yy == y: ver[y][max(x, xx)] = "     "
                continue
            if xx == x: hor[max(y, yy)][x] = "+    "
            if yy == y: ver[y][max(x, xx)] = "     "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    for i in range(h):
        for j in range(w):
            if(hor[i][j]=="+----"):
                maze[i][j][0]=True
            if(ver[i][j]=="|    "):
                maze[i][j][1]=True
            if(hor[i+1][j]=="+----"):
                maze[i][j][2]=True
            if(ver[i][j+1]=="|    "):
                maze[i][j][3]=True  
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    #print(s)
    return maze
if __name__ == '__main__':
    print(make_maze(16,5))
