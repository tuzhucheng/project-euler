# Lookup table used to store number of routes to that point
look_up = [[-1 for x in range(21)] for x in range(21)]

def getRouteCount(x, y):
    # Base case is if point is on the left or top border, in which case number of path from origin is one
    if x == 0 or y == 0:
        return 1

    if look_up[x][y] == -1:
        n = getRouteCount(x-1, y) + getRouteCount(x, y-1)
        look_up[x][y] = n
        return n
    else:
        return look_up[x][y]

def main():
    print("Number of routes is {}.".format(getRouteCount(20, 20)))

if __name__ == "__main__":
    main()

