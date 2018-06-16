def parenthesize(T, p):
    """Print the parenthesize representation of T rooted ar p."""
    print(p.element(), end="")  #use of end avoids trailing line
    if not T.is_leaf(p):
        first_time=True
        for c in T.children(p):
            sep = '('if first_time else ',' #determine proper seperator
            print(sep, end = '')
            first_time = False      #any further passes will not be the first
            parenthesize(T, c)      #recur on child
        print('(', end='')          #include closing parenthesis