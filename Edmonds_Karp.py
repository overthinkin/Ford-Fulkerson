class Edge(object): #노드와 간선 용량을 저장하는 변수 Edge를 만든다
    def __init__(self, u, v, w):
        self.source = u #Edge에는 시작점 source와
        self.sink = v   #끝점 sink가 있다.
        self.capacity = w #source와 sink를 연결하는 간선에는 용량 w를 지정한다.

    def __repr__(self): #노드와 간선의 형태를 다음과 같은 모습으로 리턴한다.
        return '%s -> %s : %s ' %(self.source, self.sink, self.capacity) 

class FlowNetwork(object):
    def __init__(self):
        self.adj = {} #간선을 의미한다
        self.flow = {} #흐르는 유량을 의미한다

    def add_vertex(self, vertex): 
        self.adj[vertex] = [] 

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w = 0): #노드와 간선을 추가하는 함수를 작성한다
        if u == v:
            raise ValueError('u == v') #간선이 나 자신을 가리키고 있다면 오류라고 지정한다
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0) #Residual Network을 위해 redge에 정보를 저장한다.
        edge.redge = redge 
        redge.redge = edge 
        self.adj[u].append(edge)
        self.adj[v].append(redge) #Residual Network에서 역방향으로 표시하는 것을 설정해준다.
        self.flow[edge] = 0 
        self.flow[redge] = 0 #간선 추가단계에서는 아무것도 흐르지 않았기 때문에 0으로 초기화한다.
        
    def find_path(self, source, sink, path): #너비우선탐색 BFS로 경로를 탐색하는 함수
        queue = [(source, path)] 
        while queue: #큐가 비어있지 않다면 즉, 큐가 존재한다면 아래를 반복한다 
            (source, path) = queue.pop(0) #큐 맨앞의 것을 꺼내 source와 path를 확인한다
            for edge in self.get_edges(source): #노드에 간선이 존재하는 동안 반복한다
                residual = edge.capacity - self.flow[edge] #Residual Network 값은 (용량 - 흘린 유량) 이다.
                if residual > 0 and edge not in path and edge.redge not in path: #경로의 용량을 모두 사용했다면
                    if edge.sink == sink: #끝점 sink에 있는 값이 흘려보낸 양과 같은지 확인한다
                        return path + [edge] #맞다면 경로를 리턴한다
                    else:
                        queue.append((edge.sink, path + [edge])) #아니라면 큐에 sink와 간선의 개수를 추가한다


    def max_flow(self, source, sink):
        path = self.find_path(source, sink, []) #BFS 경로탐색 방식 함수를 사용한다.
        while path != None: #경로가 존재하는 동안 반복한다
            print('path', path) #경로를 표시한다
            residuals = [edge.capacity - self.flow[edge] for edge in path] #Residual Network를 계산한다
            flow = min(residuals) #유량 flow는 길 path에 존재하는 Residual 최소값과 같다
            for edge in path: #경로에 용량이 남은 간선이 존재한다면
                self.flow[edge] += flow #유량을 더한다
                self.flow[edge.redge] -= flow #Residual Network을 위해 역으로 계산한다
            path = self.find_path(source, sink, []) #BFS함수로 길을 찾는다

        return sum(self.flow[edge] for edge in self.get_edges(source)) #유량의 총합(최대유량)을 반환한다