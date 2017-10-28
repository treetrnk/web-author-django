def recursive_parents(page):
    parents = []
    parents.append(page)
    if page.parent:
        parents.append(recursive_parents(page.parent))
    return parents
