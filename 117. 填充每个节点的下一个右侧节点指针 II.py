class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        l = [(root, 1)]
        ans = []
        while len(l) != 0:
            node, idx = l.pop(0)
            ans.append((node, idx))
            if node.left is not None and node.left.val is not None:
                l.append((node.left, idx + 1))
            if node.right is not None and node.right.val is not None:
                l.append((node.right, idx + 1))
        res = [[] for _ in range(ans[-1][-1])]
        for node, idx in ans:
            res[idx - 1].append(node)

        for nodes in res:
            for idx, node in enumerate(nodes):
                if idx + 1 < len(nodes):
                    node.next = nodes[idx + 1]
                else:
                    node.next = None
        return root
