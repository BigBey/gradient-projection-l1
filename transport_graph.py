class Node:
    __slots__ = ["index", "neighbors", "_active"]

    def __init__(self, i):
        self.neighbors = set()
        self.index = i
        self._active = True

    def add_neighbor(self, i):
        self.neighbors.add(i)

    def has_neighbor(self, i):
        if i in self.neighbors:
            return True
        return False

    def disactivate(self):
        self._active = False

    def activate(self):
        self._active = True

    def is_active(self):
        return self._active


class Edge:
    __slots__ = ["pair", "_active", "data"]

    def __init__(self, pair, data):
        self.pair = pair
        self.data = data
        self._active = True

    def disactivate(self):
        self._active = False

    def activate(self):
        self._active = True

    def is_active(self):
        return self._active


class TransportEdgeData:
    __slots__ = ["length","cost","throughput"]

    def __init__(self, length, cost, throughput):
        self.length = length
        self.cost = cost
        self.throughput = throughput

    def __eq__(self, other):
        if self.length == other.length:
            return True
        return False

    def __lt__(self, other):
        if self.length < other.length:
            return True
        return False


class TransportEdge(Edge):
    def __init__(self, pair, data: TransportEdgeData):
        super().__init__(pair,data)

    def __eq__(self, other):
        return self.data == other.data

    def __le__(self,other):
        return self.data < other.data


class TransportGraph:
    __slots__ = ["nodes_list", "graph_dict"]

    def __init__(self):
        self.nodes_list = []
        self.graph_dict = []

    def add_node(self):
        index = len(self.nodes_list)
        node = Node(index)
        self.graph_dict.append({})
        self.nodes_list.append(node)

    def add_pair(self, i, j, data: TransportEdgeData, bi_direct=False):
        self.nodes_list[i].add_neighbor(j)
        edge = TransportEdge((i,j),data)
        self.graph_dict[i][j] = edge
        if bi_direct:
            self.add_pair(j, i, data, False)

    def disactivate_node(self,i):
        self.nodes_list[i].disactivate()

    def activate_node(self,i):
        self.nodes_list[i].activate()

    def disactivate_node(self, i):
        self.nodes_list[i].disactivate()

    def activate_node(self, i):
        self.nodes_list[i].activate()

    def disactivate_edge(self, i, j):
        if i < len(self.nodes_list) and j in self.graph_dict[i]:
            self.graph_dict[i][j].disactivate()
            return True
        return False

    def activate_edge(self, i, j):
        self.graph_dict[i][j].activate()

    def get_node(self, i):
        return self.nodes_list[i]

    def get_edge(self, i, j):
        return self.graph_dict[i][j]

    def __getitem__(self, node):
        if node in self.nodes_list:
            return self.nodes_list[node]
        else:
            return None

    def __iter__(self):
        return self.nodes_list.__iter__()
