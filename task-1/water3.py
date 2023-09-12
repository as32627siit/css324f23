def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0,1] == 4

def successors(s):
    x, y, z = s
    if x>0:
        yield ((0,y,z), 1)
    if y>0:
        yield ((x,0,z), 1)
    if z>0:
        yield ((x,y,0),1)
    if x<8:
        yield((8,y,z), 8-x)
    if y<5:
        yield((x,5,z), 5-y)
    if z<3:
        yield((x,y,3), 3-z)
    
    return []
hee tits
