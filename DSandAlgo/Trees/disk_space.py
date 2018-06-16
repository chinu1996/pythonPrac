def disk_space(T, p):
    """Return total disl space for subtree T rooted at p"""
    subtotal = p.element().space()          #space used at postion p
    for c in T.children(p):
        subtotal+= disk_space(T, c)         #add child's space to subtotal
    return subtotal