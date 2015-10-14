Daniel Kronovet

dbk2123

CSOR w4246 HW02

10/19/2015

## Problem 1

For this problem, we will use a modified breadth-first search algorithm, in which `s` is the start node and `t` is the destination node.

The first modification adds a new array, `numpaths`, which store the number of shortest paths for any given node `u`.

The second modification reorganizes the innermost loop such that some processing occurs for each node `v` regardless of whether that `v` has already been discovered.  This processing includes checking to see if distance `s-u-v` is less or equal to any previous `s-v` paths. If it is less than, then this path becomes the shortest path and `numpaths[v]` is set to 1. If it is equal, then `numpaths[v]` is incremented by one. This change is important because it allows for the discovery of multiple shortest paths by allowing for the reuse of nodes already discovered.

The solution given works for undirected graphs with weighted edges. For an unweighted graph, set all `w=1`. This solution preserves the O(n + m) running time of the original bfs algorithm, as the processing on each edge takes O(1) time.

```
modbfs(G=[V, E], s, t):
    array dist[V] = inf
    array disc[V] = 0
    array numpaths[V] = 0
    queue q
    disc[s] = 1
    dist[s] = 0
    enqueue(q, s)
    WHILE size(q) > 0 DO
        u = dequeue(q)
        FOR v, w in E[u] DO
            IF dist[v] > dist [u] + w DO
                dist [v] = dist [u] + w
                numpaths [v] = 1
            ELSIF dist [v] == dist [u] + w DO
                numpaths [v] += 1
            ENDIF
            IF disc [v] == 0 DO
                disc [v] = 1
                enqueue(q, v)
            ENDIF
        ENDFOR
    ENDWHILE
    return numpaths[t]
```


## Problem 2

For this problem, we will use an extended version of Dijkstra’s algorithm.

The first extension involves the creation of an additional array using the results from Dijkstra’s algorithm. This array, diff, contains the edge distances between each node `v` and its previous node u in the shortest path from `s-v`.

The second extension loops through every proposed road edge `(u,v,l)` and calculates the shortest `s-t` path using this new road. The greedy algorithm will check this shortest path and compare this new path to the existing shortest path. If the new path is shorter, than the new path will replace the old path. Once all paths have been analyzed, the shortest path is returned.


```
chooseroad(G=[V, E], E', s, t)
    dist, prev = dijkstra(G=[V, E], s) # Any implementation of Dijkstra will do

    array diff = []
    FOR v in V DO:
        diff[v] = dist[v] - dist[prev[v]]
    ENDFOR

    tuple bestroad = nil
    int bestsavings = 0
    FOR u, v, l in E' DO
        oldprev = prev[u]
        olddiff = diff[u]
        totaldist = dist[t]
        prev[v] = u
        diff[v] = l
        x = t
        WHILE prev[x] != s DO
            totaldist -= diff[x]
            x = prev[x]
        ENDWHILE
        IF totaldist < bestsavings DO
            bestroad = (u,v,l)
        ENDIF
        prev[v] = oldprev # Restore initial values
        diff[v] = olddiff
    ENDFOR

    return bestroad
```

## Problem 3

In this problem, we use a modified version of Dijkstra's algorithm. First, we will assume the algorithm is implemented using a binheap (Dijkstra v3 from class).

The modification includes the addition of a new array, `best`, which records the number of edges in the shortest `s-v` path for an arbitrary `v`. Then, at every iteration, we check the edges adjacent to the new node v (the inbound edges, `indegree(v)`). If any of the adjacent nodes `x` have been discovered, we examine the length of the path `s-x-v`. If this path is the same distance as the default `s-u-v` path (it cannot be shorter), we compare the number of edges in the two paths. If `s-x-v` has fewer edges than `s-u-v`, it replaces `s-u-v` as the correct `s-v` path.

This modification does not affect the running time of Dijkstra's algorithm, which in this case is O(mlogn). This is because we **already** loop through `deg(u)` every time we extract `u` from the heap. All we are doing is adding a few O(1) operations to the loop, which does not affect the overall time complexity.

```
chooseroad(G=[V, E], s)
    array dist[V] = inf
    array prev[V] = nil
    array best[V] = inf
    dist[s] = 0
    best[s] = 0
    set S = {}
    binminheap heap(V, dist)
    WHILE heap DO
        u, udist, uprev = extract(heap)
        S = S + {u}
        dist[u] = udist
        prev[u] = uprev
        best[u] = best[uprev]+1 IF uprev ELSE 0
        FOR v, w in E[u] DO
            IF v in S DO
                int altdist = dist[v] + w(v, u)
                IF altdist == dist[u] and best[u] > best[v]+1 DO
                    best[u] = best[v]+1
                    prev[u] = v
                ENDIF
            ELSE DO
                update(heap, u, v, w) # Update heap with new dist for v
            ENDIF
        ENDFOR
    ENDWHILE
```

## Problem 4

In this problem, we use a dynamic programming approach to determining the optimal segmentation for string `y`. Note that `y[i:j]` represents a substring of `y`, spanning characters `i` to `j`.

Given that each call to `q()` is an O(1) operation, as is every call to `M[]`, finding an optimal value for `M[j]` is an O(n) operation, requiring a loop through every `i`, subject to `1 <= i <= j`. As we must find the optimal value for all `1 <= j <= n`, this algorithm runs in O(n^2) time.

```
wordsearch(y)
    array M = [0]
    FOR j = 1 to n DO
        M[j] = max(i){q(y[i:j]) + M(i-1)} # 1 <= i <= j
    ENDFOR
    return M
```

## Problem 5

In this problem, we devise an algorithm to find the optimal partitions for a dataset, to minimize the maximum difference between any single partition and the mean.

The key insight here is that we are interested in how the **maximum imbalance** changes as we adjust our segmentation. In other words, we want to minimize the maximum imbalance. We can assess change in maximum imbalance as a function of segmentation by comparing the imbalance of the **proposed** segment to the largest imbalance among all earlier partitions, leading to the expression `min(c){max(curr_imbalance(c), max_prior_imbalance(c))}`, in which both terms are a function of `c`, for any given `j`.

Note that we represent `w(i)` as `sum(A[i:j])`, an equivalent expression for the sum of all values of `A` indexed by `i:j`.

The second challenge is bounding the number of partitions by k. We must optimize across two parameters, implying the need for a matrix `M` to store results of subproblems. We achieve this via two loops, one over `i = 1...n`, and the other over `j = 1...k`. For any combination of `i,j`, we must decide the bounds of partition j, which we do by comparing the imbalance of proposed partition `A[c:j]` to the prior max imbalance given by `M[i-1:j-c]`. Note that we must decrement i as well as j to take into account that prior max imbalances were calculated in an environment with one fewer partitions.

Note that the outer loop must be through `k`. To invert the order would result in the algorithm attemping to partition one data point into `k` partitions.

```
balancedpartition(A, k)
    int n = len(A)
    int avg = sum(A) / k+1
    matrix M[0:n, 0:k] = inf

    FOR i = 1 to k DO
        FOR j = 1 to n DO
            M[i,j] = min(c){max(abs(sum(A[c:j])-avg), M[i-1,j-c])}  # 1<=c<=j
        ENDFOR
    ENDFOR

```





























