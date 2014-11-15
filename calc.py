class PathGameDiv2:
    def calc(self, board):
        col = len(board[0])
        # dist[x][y] defines the min distance from (x, y) to the right-most column,
        # either @ row 0 or row 1; it doesn't matter which
        # We first initialize all distance to the rightmost column to infinity
        dist = [[float('inf') for x in xrange(col)] for x in xrange(2)]

        w = 0

        # We then initialize the distance from the rightmost column
        # Note the we initialize a white cell to 1, not 0.  This is because
        # this will represent the min number of white cells
        for x in xrange(2):
            if board[x][col-1] != '#':
                dist[x][col-1] = 1
                w += 1

        for y in xrange(col-2, -1, -1):
            for x in xrange(0, 2):
                if board[x][y] != '#':
                    w += 1
                    # We can get the min distance to column to our right by either
                    # trying at the current row x or row !x (!x is 1 if x is 0; !x
                    # is 0 if x is 1)
                    r_xy = dist[x][y+1] + 1
                    if board[not x][y] != '#':
                        r_xy = min(r_xy, 2 + dist[not x][y+1])
                    dist[x][y] = r_xy

        # Since dist[0][0]/dist[1][0] indicates the min distance from left-most
        # column starting at either row 0 or row 1 to the rightmost column, either
        # arriving at row 0 or row 1, without going through the black cells, they
        # will be a color white path.  We just subtract this white path (min # of
        # white cells) from the total number of white cells to get the max cells
        # that can be colored black
        return w - min(dist[0][0], dist[1][0])

pgd = PathGameDiv2()
board = [["#", ".", ".", ".", "."], [".", ".", ".", "#", "."]]
print "Largest number of cells to color board %s black is %s" % (board, str(pgd.calc(board)))

board = [["#"], ["."]]
print "Largest number of cells to color board %s black is %s" % (board, str(pgd.calc(board)))

board = [["."], ["."]]
print "Largest number of cells to color board %s black is %s" % (board, str(pgd.calc(board)))

board = [[".", ".", ".", ".", "#", ".", "#", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".",".", ".", ".", ".", "."],
         [".", ".", "#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".","#", ".", ".", ".", "."]]
print "Largest number of cells to color board %s black is %s" % (board, str(pgd.calc(board)))
