#https://leetcode.com/problems/unique-paths-iii/

from collections import deque

class Graph:

    def __init__(self, no_of_vertex):
        self.adj_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.adj_list[vertex1] = list()
        if vertex2 not in self.adj_list:
            self.adj_list[vertex2] = list()
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def get_adj_list(self):
        return self.adj_list

    def get_connections(self, vertex):
        return self.adj_list[vertex]

def is_valid_cell(i, j, grid):
    if grid[i][j] != -1:
        return True
    return False

def get_vertex(i, j, n):
    return (n * i) + j

def calc(node, visited, adj_list, end):

    visited.append(node)
    if node == end:
        if sorted(visited) == sorted(adj_list.keys()):
            return 1
        else:
            return 0

    result = 0
    if node in adj_list:
        for c in adj_list[node]:
            if c not in visited:
                result += calc(c, visited, adj_list, end)
                visited.pop()

    return result


class Solution:
    def uniquePathsIII(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        start = None
        end = None
        graph = Graph(m * n)

        for i in range(0, m):
            for j in range(0, n):
                vertex = get_vertex(i, j, n)

                if grid[i][j] == 1:
                    start = vertex
                elif grid[i][j] == 2:
                    end = vertex
                elif not is_valid_cell(i, j ,grid):
                    continue

                #check right
                if j + 1 < n and is_valid_cell(i, j + 1, grid):
                    graph.add_edge(vertex, get_vertex(i, j+1, n))

                #check bottom
                if i + 1 < m and is_valid_cell(i + 1, j, grid):
                    graph.add_edge(vertex, get_vertex(i + 1, j, n))

        return calc(start, deque(), graph.get_adj_list(), end)


s = Solution()
print(s.uniquePathsIII([[0,1],[2,0]]))
