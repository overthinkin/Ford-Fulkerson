# Ford-Fulkerson Algorithm

#### 		1. 알고리즘 소개

#### 		2. 동작 방식

#### 		3. 성능 분석

#### 		4. 코드 실행 결과 

#### 		5. MaxFlow 문제를 푸는 다른 알고리즘 소개

#### 		6. 참고 자료 출처

------

## [알고리즘 소개]

Ford-Fulkerson Algorithm은 네트워크에서 최대 유량 문제를 Greedy 알고리즘 방식으로 해결하는 알고리즘이다. 

최대 유량 문제는 가중치와 방향이 있는 그래프에서 시작점(Source)에서 끝점(Sink)까지 모든 경로에 대해 남은 Capacity를 파악하여 흘려보내는 작업을 반복하여 최대한 많은 양을 보낼 수 있도록 해야하는 문제이다.

Greedy 방식은 현재 상황에서 최적의 값을 찾는 것으로, 이전과 이후의 상황은 고려하지 않는다는 특징을 갖고 있다. 따라서 값을 빠른 시간에 찾을 수 있다. 하지만 그 값이 최고로 최적화된 값인지는 보장하기 어렵다. 그러나 부분의 문제를 최적화하여 찾아준다면 결과값도 최적이라고 볼 수 있기 때문에(Optimal Substructure) Greedy 방식으로 값을 찾는 것 또한 최적화 문제다.



## [동작 방식]

Ford-Fulkerson Algorithm의 구조
n개의 노드를 가진 가중치 그래프가 존재할 때,
노드와 노드 사이의 용량 `Capacity`와 
노드와 노드 사이에서 흐르는 유량 `Flow`가 있다.
(단, Flow의 값은 Capacity보다 작거나 같다. F ≤ C)

#### Ford-Fulkerson Algorithm의 작동 방식

각 경로에서 최대 흐름을 전송하고 난 후 여분의 Capacity로 만들 수 있는 네트워크(**Augmenting Path**)를 찾아 더 많은 양을 흘려보낼 수 있도록 한다.

#### Residual Network 작성 방법

Augmenting Path를 토대로 실제 흘린 값을 역방향, 더 흘릴 수 있는 값을 원래 흐름 방향으로 정하여 새로운 네트워크를 그리면 새로운 길을 더 찾을 수 있다.
새로운 길에서 남은 용량이 있다면 유량을 추가하여 최대 유량을 늘리게 되는 방식이다.

#### 그래프로 Ford-Fulkerson Algorithm BFS 방식 계산해보기

 사진1

노드 10개 (qwertyuiop) / 간선 12개 / 유량은 보라색 글씨로 표기했다.

사진2

깊이우선 탐색으로 최초로 찾은 길 2개에서 흘려보낸 유량은 총 13이다.

사진3

Residual Network를 통해 형광초록색으로 표기한 길에서 사용하고 남은 용량을 새로운 길(주황색)이 사용할 수 있다.

사진4

길 3가지에서 흘려보낸 양은 총 20이다.

사진5

사진1-4까지의 과정을 수행한 뒤의 Residual Network 그래프이다.

사진6

남은 길(보라색)에 최소 용량 3을 sink까지 보낼 수 있다.

사진7

 Ford-Fulkerson Algorithm으로 총 4가지의 길을 통해 최대유량을 보낸 것을 확인했다.

사진8

최대유량을 source에서 흘려보낸 양과 sink에서 받은 양을 계산하여 검증했다.



#### psudo코드

```C
initialize flow f to 0 //아직 아무 값도 흘려보내지 않았기 때문에 모든 간선의 최초 유량을 0으로 초기화
while there exists and augmenting path p //길 p이 존재하는 동안 계속 반복한다
	do augment flow f along p //모든 flow f를 길 p에 추가한다
return f  //전체 흐름 값을 알 수 있다
```

#### 더 자세한 psudo코드

```C
for each edge(u,v) ∈ E[G] //그래프 G에 있는 간선에는 용량이 있다
	do f[u,v] = 0 //유량은 모두 0으로 초기화
	   f[v,u] = 0 //Residual Network를 위한 값도 초기화

while there exist a path p from s to t in the residual network G(f) //Residual Network에 길 p가 존재한다면 다음을 반복한다
	do cf(p) = min{cf(u,v) | (u,v) is in p} //p가 존재할때 그 경로 중 가장 작은 값을 추가
		for each edge(u,v) in p //각 간선이 길 p에 있다면 반복한다
			do f[u,v] = f[u,v] + cf(p) //반복해서 더한다
			   f[v,u] = -f[u,v]	//Residual Network에 값을 입력	
```



## [성능 분석]

Ford-Fulkerson Algorithm의 시간복잡도는 최대 유량 F가 간선의 개수 E와 노드의 개수 V를 더한 것만큼 이동한 것과 같다. 
$$
O( (|E|+|V|) * F )
$$

Ford-Fulkerson Algorithm은 경로를 탐색하는 방법을 지정하지 않고 수행했다. 따라서 깊이우선탐색(DFS)으로 경로를 탐색했을 때 ***최악의 경우 수행시간이 초과*** 하여 문제를 해결하지 못한다. 그 외에 **너비우선탐색(BFS)으로 경로를 찾는** Ford-Fulkerson 방식을 **Edmonds-Karp Algorithm**이라고 부른다.

**Edmonds-Karp Algorithm**의 시간복잡도는 정점의 개수에 간선의 제곱 값을 곱한 만큼의 시간이 걸린다.
$$
O( |V| * (|E|^2) )
$$


## [코드 실행 결과] 

Ford-Fulkerson의 방식 중 BFS로 경로를 탐색하는 것이 더 효율적이기 때문에 **Edmonds-Karp Algorithm**을 구현하였다

```python
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
```

결과사진

과 그림의 결과를 비교했을 때 최대유량 값이 동일한 것을 확인하였다.



## [최대 유량 문제를 해결하는 다른 알고리즘]

#### 디닉 알고리즘 (Dinitz' Algorithm) 

디닉 알고리즘은 포드풀커슨의 DFS, BFS 방식을 혼용한 탐색 방법을 사용한다.





## [참고 자료 출처]

https://www.youtube.com/watch?v=RppuJYwlcI8
https://wooono.tistory.com/401
https://ratsgo.github.io/data%20structure&algorithm/2017/11/29/maxflow/
https://koosaga.com/18
https://gazelle-and-cs.tistory.com/63
https://www.youtube.com/watch?v=-jKuV-iH6qE
https://blog.naver.com/na_qa/221472420613
https://github.com/KrisYu/Graph

