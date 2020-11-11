def levelOrder(root):
    lst = []
    if not root:
        return
    q = collections.deque()
    q.appendleft(root)
    while q:
        node = q.pop()
        lst.append(node.val)
        if node.left is not None:
            q.appendleft(node.left)
        if node.left is not None:
            q.appendleft(node.right)
    return lst

def levelOrder2(root):
    levels = []
    if not root:
        return levels
    level = 0
    queue = deque([root,])
    while queue:
        levels.append([])
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels