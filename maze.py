r = open('laser_maze.txt', 'r')
w = open('laser_maze_output.txt', 'w')
T = int(r.readline())
#print T

def genLine(maze, pos, direct):
    i, j = pos
    di, dj = direct
    M = len(maze)
    N = len(maze[0])
    i += di 
    j += dj
    block = set(['#', '^', '>', 'v', '<'])
    while 0 <= i < M and 0 <= j < N and maze[i][j] not in block: 
        maze[i][j] = 'L'
        i += di
        j += dj

def genMaze(maze, laser):
    clock = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direct = {'^':0, '>':1, 'v':2, '<':3}
    maze_choice = []
    for i in range(4):
        new_maze = [row[:] for row in maze]
        for key in laser:
            for pos in laser[key]:
                genLine(new_maze, pos, clock[(i + direct[key]) % 4])
        maze_choice += [new_maze[:]]
        #print new_maze
    return maze_choice

for t in range(T):
    M, N = map(lambda x : int(x), r.readline().split())
    #print M, N
    maze = [['#'] * N for _ in range(M)]
    laser = {'^':[], '>':[], 'v':[], '<':[]}
    for i in range(M):
        row = r.readline().strip()
        for j in range(N):
            maze[i][j] = row[j]
            if row[j] in laser:
                laser[row[j]] += [(i,j)]
            elif row[j] == 'S':
                maze[i][j] = '.'
                start = (i, j)
    maze_choice = genMaze(maze, laser)
    #print maze_choice[0]
    #print laser
    #print maze
    queue = [start]
    step = 0
    win = False
    while queue:
        size = len(queue)
        step += 1
        for k in range(size):
            this_maze = maze_choice[step % 4]
            #print this_maze
            i, j = queue.pop(0)
            if 0 < i:
                if this_maze[i - 1][j] == '.':
                    queue += [(i - 1, j)]
                    this_maze[i - 1][j] = '#'
                elif this_maze[i - 1][j] == 'G':
                    win = True
                    break
            if i < (M - 1):
                if this_maze[i + 1][j] == '.':
                    queue += [(i + 1, j)]
                    this_maze[i + 1][j] = '#'
                elif this_maze[i + 1][j] == 'G':
                    win = True
                    break
            if 0 < j:
                if this_maze[i][j - 1] == '.':
                    queue += [(i, j - 1)]
                    this_maze[i][j - 1] = '#'
                elif this_maze[i][j - 1] == 'G':
                    win = True
                    break
            if j < (N - 1):
                if this_maze[i][j + 1] == '.':
                    queue += [(i, j + 1)]
                    this_maze[i][j + 1] = '#'
                elif this_maze[i][j + 1] == 'G':
                    win = True
                    break
        if win:
            break
    print "Case #" + str(t + 1) + ': ' + (str(step) if win else 'impossible')
    w.write("Case #" + str(t + 1) + ': ' + (str(step) if win else 'impossible') + '\n')
'''
['S', '.', '.', '.', '.']
['.', '.', '.', '.', '.'] 
['.', '>', 'v', '.', '.']
['.', '^', '<', '.', '.'] 
['.', '.', '.', '.', 'G']

['S', '.', '.', '.', '.'] 
['.', '.', '.', '.', '.'] 
['.', '>', 'v', '.', '.']
['.', '^', '<', '.', '.'] 
['.', '.', '.', '.', 'G']

['S', '.', 'L', '.', '.'] 
['.', '.', 'L', '.', '.'] 
['L', '>', 'v', '.', '.']
['.', '^', '<', 'L', 'L'] 
['.', 'L', '.', '.', 'G']

['S', 'L', '.', '.', '.'] 
['.', 'L', '.', '.', '.']
['.', '>', 'v', 'L', 'L']
['L', '^', '<', '.', '.']
['.', '.', 'L', '.', 'G']
'''
r.close()
w.close()
