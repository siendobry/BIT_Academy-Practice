def addNode(p, x):
    x.next = p
    return x


def selsort(p):
    if p is None:
        return
    if p.next is None:
        return p
    curr = p
    prev = None
    r = None
    while p is not None:
        currMin = p
        while curr.next is not None:
            if curr.next.val > currMin.val:
                currMin = curr.next
                prev = curr
            curr = curr.next
        if currMin == p:
            p = p.next
        else:
            prev.next = currMin.next
        currMin.next = None
        r = addNode(r, currMin)
        curr = p
        prev = None
    return r

