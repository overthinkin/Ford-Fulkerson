import Edmonds_Karp

g = Edmonds_Karp.FlowNetwork()

[g.add_vertex(v) for v in 'qwertyuiop'] #한줄로 쓴 for 반복문 

# 간선의 개수만큼 add_edge함수를 사용한다
# 그림에서 사용한 노드는 10개 간선은 12개다
# 그래프에서 source는 'q'이고 sink는 'p'이다.

g.add_edge('q','w',9) 
g.add_edge('w','t',10) 
g.add_edge('t','y',8)  
g.add_edge('y','p',20)

g.add_edge('q','e',7)
g.add_edge('e','i',12)
g.add_edge('i','o',10)
g.add_edge('u','e',4)

g.add_edge('q','r',10)
g.add_edge('r','u',8)
g.add_edge('u','o',5)
g.add_edge('o','p',15)



print (g.get_edges('q')) #source인 q에 있는 간선들을 찾는다
print (g.find_path('q','p', [])) #BFS방식으로 찾은 길을 출력한다 
print(g.max_flow('q','p')) #최대 유량을 출력한다