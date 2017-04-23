class KosarajuSCC:
    def __init__(self, g):
        '''
        Calcula las Componentes Fuertemente Conexas del grafo g.
        :param g: grafo implementando la interfaz de la clase Digraph 
        '''
        self.components = {}
        order = self.dfs(g)
        order.reverse() # se ordena de ultimo terminado de visitar a primero terminado de visitar
        print(order)
        self.find_SCC(g.reverse(),order) # dfs a g transpuesta tomando los vertices en orden inverso

    def dfs(self, g):
        stack = []
        visited = {v: False for v in g}
        ordered = {v: False for v in g} # para saber si ya esta ordenado
        order = []  # el primero es el que primero termina de ser visitado
        for v in g: # por si no es conexo
            if visited[v]:
                continue
            stack.append(v)
            while stack: #len(stack) != 0
                v_now = stack[-1]
                if ordered[v_now]:
                    stack.pop()
                    continue
                if visited[v_now]:      # si ya lo visite y esta en la pila es que estoy volviendo. Lo agrego al orden
                    order.append(v_now)
                    stack.pop()
                    ordered[v_now] = True
                    continue
                visited[v_now] = True
                for adj in g.adj_list(v_now):
                    if not visited[adj]:
                        stack.append(adj)
        assert len(order) == len(g)
        return order

    def find_SCC(self, g, order):
        c_id = -1 #component id
        stack = []
        visited = {v: False for v in g}
        for v in order:
            if visited[v]:
                continue
            stack.append(v) # nueva raiz
            c_id += 1       # nueva CFC
            self.components[c_id] = set()
            while stack:
                v_now = stack.pop()
                self.components[c_id].add(v_now)
                visited[v_now] = True
                for adj in g.adj_list(v_now):
                    if not visited[adj]:
                        stack.append(adj)

    def __str__(self):
        return str({id: sorted(list(self.components[id])) for id in self.components})

    def count(self):
        return len(self.components)

    def get_component(self, i):
        """
        Devuelve la componente fuertemente conexa i. Si hay menos, lanza IndexError
        :param i: la componente que se quiere
        :return: una lista ordenada con los vertices en la componente
        """
        if i >= self.count():
            raise IndexError
        return sorted(list(self.components[i]))

