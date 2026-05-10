from utils import *

def negative_cycle(Rf, n):
    """
    input:
        Rf: residual dictionary (edge : value)
        n : int nb of vertices
    output:
        boolean : it exists a negative cycle
    """
    Rf_pos = [e for e in Rf if Rf[e] > 0]
    dist = [0] * n      
    prev_edges = {}
    for i in range(n - 1):
        for (start, end, cap, cost) in Rf_pos:
            if dist[start] + cost < dist[end]:
                dist[end] = dist[start] + cost
                prev_edges[end] = (start, end, cap, cost)
    for (start, end, cap, cost) in Rf_pos:
        if dist[start] + cost < dist[end]:
            return True
    return False

