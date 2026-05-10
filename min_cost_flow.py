from utils import *
import heapq


def Bellman_Ford(Rf, s,n):
    """
    input:
        Rf: residual dictionary (edge : value)
        s: vertex
        n: int nb of vertices
    output:
        dico ( vertex : distance from s)
        dico ( vertex : previous edge in the path from s to vertex)
    """
    Rf_pos=[e for e in Rf if Rf[e]>0] # if the edge residual flow is none then the original edge is saturated we can't use it
    dist = [float('inf')] * n
    prev_edges = {}
    dist[s] = 0
    for i in range(n - 1):
        for (start, end, cap, cost) in Rf_pos:
            if dist[start] + cost < dist[end]:
                dist[end] = dist[start] + cost
                prev_edges[end] = (start, end, cap, cost)     
    return dist, prev_edges



def min_cost_flow_Bellman_Ford(E, s, t, n, ):
    """
    input:
        E: list of edges (start,end,capacity,cost)
        s: vertex
        t: vertex
        n: int nb of vertices
    output:
        flow dictionary (edge: value) of the minimum cost flow from s to t
        value of the minimum cost flow from s to t
        cost of the minimum cost flow from s to t
    """
    f = {e: 0 for e in E}
    total_flow_value = 0
    total_cost = 0
    Rf = make_Rf(E, f)
    dist, prev_edges = Bellman_Ford(Rf, s, n)
    while dist[t] != float('inf'):
        gamma = extract_path( prev_edges, s, t)
        delta = min(Rf[e] for e in gamma)
        for (u, v, cap, cost) in gamma:
            if (u, v, cap, cost) in E:
                f[(u, v, cap, cost)] += delta
            else:
                f[(v,u,cap,-cost)] -= delta
        total_flow_value += delta
        total_cost += delta * dist[t]
        Rf = make_Rf(E, f)                         
        dist, prev_edges = Bellman_Ford(Rf, s, n)
    return f,total_flow_value, total_cost



def Dijkstra(Rf, s, n, h):
    """
    input:
        Rf: residual dictionary (edge : value)
        s: vertex
        n: int nb of vertices
        h: list of potentials for each vertex
    output:
        dico ( vertex : distance from s)
        dico ( vertex : previous edge in the path from s to vertex)
    """
    Rf_pos = [e for e in Rf if Rf[e] > 0]
    dist = [float('inf')] * n
    prev_edges = {}
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist> dist[u]:     
            continue
        for (start, end, cap, cost) in Rf_pos:
            if start ==u:
                reduced_cost = cost + h[start] - h[end]
                new_dist = dist[u] + reduced_cost
                if new_dist< dist[end]:
                    dist[end] = new_dist
                    prev_edges[end] = (start, end, cap, cost)
                    heapq.heappush(heap, (dist[end], end))
    return dist, prev_edges


def min_cost_flow_dijkstra(E, s, t, n):
    """
    input:
        E: list of edges (start,end,capacity,cost)
        s: vertex
        t: vertex
        n: int nb of vertices
    output:
        flow dictionary (edge: value) of the minimum cost flow from s to t
        value of the minimum cost flow from s to t
        cost of the minimum cost flow from s to t
    """
    f = {e: 0 for e in E}
    total_flow_value = 0
    total_cost = 0
    Rf = make_Rf(E, f)
    h ,_= Bellman_Ford(Rf, s, n)
    dist, prev_edges = Dijkstra(Rf, s, n, h)
    while dist[t] != float('inf'):
        gamma = extract_path(prev_edges, s, t)
        delta = min(Rf[e] for e in gamma)
        for (u, v, cap, cost) in gamma:
            if (u, v, cap, cost) in E:
                f[(u, v, cap,  cost)] += delta
            else:
                f[(v, u, cap, -cost)] -= delta
        total_flow_value += delta
        real_cost = dist[t] + h[t] - h[s]
        total_cost += delta * real_cost
        for v in range(n):
            if dist[v] < float('inf'):
                h[v] += dist[v]
        Rf = make_Rf(E, f)
        dist, prev_edges = Dijkstra(Rf, s, n, h)
    return f, total_flow_value, total_cost

