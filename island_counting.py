


def mark_island(map,r,c):
    if map[r][c] ==0:
        return
    map[r][c]=0
    if r>0:
        mark_island(map,r-1,c)
    if c>0:
        mark_island(map,r,c-1)
    if r<len(map)-1:
        mark_island(map,r+1,c)
    if c < len(map[r])-1:
        mark_island(map,r,c+1)


def count_islands(map)->int:
    count =0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 1:
                mark_island(map,r,c)
                count+=1

    return count


if __name__=="__main__":
    map = [
        [0,0,1,0],
        [1,1,0,1],
        [0,1,0,1],
        [0,1,0,0]]
    print(count_islands(map))