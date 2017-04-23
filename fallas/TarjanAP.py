from random import randint

class TarjanAP:
    def __init__(self, G):
        self.parents =         [None] * G.V()
        self.visited =         [False] * G.V()
        self.processed =       [False] * G.V()
        self.dfs_depth =       [None] * G.V()
        self.min_dfs_depth =   [None] * G.V()
        self.is_articulation = [False] * G.V()

        self.current_dfs_depth = 1
        self.dfs_stack = []
        self.dfs_tree = {}
        self.G = G

        self.articulation_points = None

    def getArticulationPoints(self):
        if (self.articulation_points != None):
            return self.articulation_points

        self.articulation_points = []
        for root in self.G:
            if self.processed[root]:
                continue

            self.dfs_stack.append(root)
            is_dfs_leaf = False

            while self.dfs_stack:
                current_vertex = self.dfs_stack[-1]

                if not self.visited[current_vertex]:
                    is_dfs_leaf = True
                    self.visited[current_vertex] = True
                    self.dfs_depth[current_vertex] = self.current_dfs_depth
                    self.min_dfs_depth[current_vertex] = self.current_dfs_depth
                    self.current_dfs_depth += 1

                for neighbor in self.G.adj_list(current_vertex):

                    if self.processed[neighbor]:
                        continue

                    if not self.visited[neighbor]:

                        self.parents[neighbor] = current_vertex
                        self.dfs_tree[current_vertex] = self.dfs_tree.get(
                            current_vertex,
                            []
                        )
                        self.dfs_tree[current_vertex].append(neighbor)

                        is_dfs_leaf = False
                        self.dfs_stack.append(neighbor)

                        break

                    if self.parents[current_vertex] != neighbor:
                        self.min_dfs_depth[current_vertex] = min(
                            self.dfs_depth[neighbor],
                            self.min_dfs_depth[current_vertex]
                        )

                if not is_dfs_leaf:
                    continue

                self.dfs_stack.pop()

                for child in self.dfs_tree.get(current_vertex, []):

                    if self.min_dfs_depth[child] >= self.dfs_depth[current_vertex] \
                    and current_vertex != root \
                    and not self.is_articulation[current_vertex]:
                        self.articulation_points.append(current_vertex)
                        self.is_articulation[current_vertex] = True

                    self.min_dfs_depth[current_vertex] = min(
                        self.min_dfs_depth[current_vertex],
                        self.min_dfs_depth[child]
                    )

                self.processed[current_vertex] = True

            if len(self.dfs_tree.get(root, [])) > 1:
                self.articulation_points.append(root)

        return self.articulation_points
