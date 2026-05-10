from collections import deque
from utils import * 


def BFS(Rf, s):
    """
    input:
        Rf: residual dictionary (edge : value)
        s: vertex
        t: vertex
    output:
        path from s to t in Rf
    """
    R_pos=[e for e in Rf if Rf[e]>0]
    q= deque([s])
    explored_vertices={s}
    prev={}
    while q :
        u= q.popleft()
        for start,end,cap,cost in R_pos:
            if start ==u:
                if end not in explored_vertices:
                    q.append(end)
                    explored_vertices.add(end)
                    prev[end] = (start,end,cap,cost)
    return prev



def max_flow_min_cut_ford_fulkerson ( E, s,t):
    """
    input:
        E: list of edges (start,end,capacity,cost)
        s: vertex
        t: vertex
    output:
        flow dictionary (edge: value) of the maximum flow from s to t
    """
    f= {e:0 for e in E }
    Rf= make_Rf(E,f)
    prev_edges= BFS(Rf,s)
    gamma=extract_path(prev_edges,s,t)
    while gamma :
        delta = min ([Rf[e] for e in gamma])
        for (u, v, cap, cost) in gamma:
            if (u, v, cap, cost) in E:
                f[(u, v, cap, cost)] += delta
            else:
                f[(v,u,cap,-cost)] -= delta
        Rf= make_Rf(E,f)
        prev_edges= BFS(Rf,s)
        gamma=extract_path(prev_edges,s,t)
    max_flow_value= sum([f[e] for e in E if e[0]==s])
    reachable=set(prev_edges.keys()) | {s}
    min_cut=[e for e in E if e[0] in reachable and e[1] not in reachable]
    return f ,max_flow_value, min_cut




