import do_four as df
design1 = '+ - - - - '
design2 = '|         '
def grid_border(s):
    print(s * 4, end='+')

def grid_shape(s):
    print(s * 4, end='|')

grid_border(design1)
df.do_four(grid_shape, design2)