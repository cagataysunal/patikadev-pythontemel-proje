def flatten(top_l):
    def flat_list_generator(top_l):
        for elem in top_l:
            if isinstance(elem, list):
                yield from flatten(elem)
            else:
                yield elem
    return list(flat_list_generator(top_l))


def deep_reverse(l: list):
    l.reverse()
    for i in l:
        if isinstance(i, list):
            deep_reverse(i)
    return l
