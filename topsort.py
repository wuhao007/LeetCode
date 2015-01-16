class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        def dfs(node, color, ret):
            color[node] = 1
            for child in node.neighbors:
                if color[child] == 0:
                    dfs(child, color, ret)
            ret.insert(0, node)
            color[node] = 2
            return ret
        color = {}
        for node in graph:
            color[node] = 0
        ret = []
        for node in graph:
            if color[node] == 0:
                dfs(node, color, ret)
        return ret
