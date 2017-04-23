class KosarajuSCC:
    def __init__(self, g):
        '''
        Calcula las Componentes Fuertemente Conexas del grafo g.
        :param g: grafo implementando la interfaz de la clase Digraph 
        '''
        self.components = {}
        order = self._dfs(g)
        self._find_SCC(g.reverse(),order) # dfs a g transpuesta tomando los vertices en orden inverso

    def _dfs(self, g):
        """
        Hace un recorrido dfs guardando en la lista "ordered" el orden en el que se termina de visitar 
        un nodo, de primero a ultimo
        :param g: grafo implementando la interfaz de la clase Digraph 
        :return: una lista "ordered" con los indices de los nodos en orden de finalizacion de la visita dfs
        """
        stack = []
        visiting = {v: False for v in g} # si se empezo a visitar
        ordered = {v: False for v in g} # para saber si ya esta ordenado
        order = []  # el primero es el que primero termina de ser visitado
        for v in g: # por si no es conexo
            if visiting[v]:
                continue
            stack.append(v)
            while stack: # len(stack) != 0
                v_now = stack[-1]
                if ordered[v_now]:
                    stack.pop()
                    continue
                if visiting[v_now]:      # si ya lo visite y esta en la pila es que estoy volviendo en el arbol.
                    order.append(v_now)  # Lo agrego al orden
                    stack.pop()
                    ordered[v_now] = True
                    continue
                visiting[v_now] = True
                for adj in g.adj_list(v_now):
                    if not visiting[adj]:
                        stack.append(adj)
        assert len(order) == len(g)
        return order

    def _find_SCC(self, g, order):
        """
        Realiza el segundo recorrido dfs del algoritmo de Kosaraju.
        :param g: grafo implementando la interfaz de la clase Digraph. (debe ser el grafo transpuesto
                  al original)
        :param order: lista de nodos que representa el orden en el que se termina de visitar cada uno
                      en el primero recorrido dfs.
        :return: un diccionario de sets. Las claves son los ids de cada CFC empezando por el 0. Los valores
                 son sets de nodos que estan incluidos en esa CFC
        """
        c_id = -1 # component id
        stack = []
        visited = {v: False for v in g}
        while order:
            v = order.pop() # recorro de ultimo terminado de visitar en el recorrido anterior a primero
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
        return str({id: sorted(list(cfc)) for id, cfc in self.components.items()})

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

