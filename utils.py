def formate_input_datas(lignes):
    """
    input:
        lignes: list 
    output:
        list of edges (start,end,capacity,cost)
        source vertex
        sink vertex
    """
    n, m, s, t = map(int, lignes[0].split())
    E = []
    for ligne in lignes[1:m+1]:
        u, v, cap, cost = map(int, ligne.split())
        E.append((u, v, cap, cost))
    return E, s, t, n, m

def formate_output_datas(f,s,t):
    """
    input:
        f: flow dictionary (edge: value)
        s: vertex
        t: vertex
    output:
        string of the graph in dot
    """
    lines=[
        'digraph G {',
        '  graph [nodesep="0.3", ranksep="0.3", fontsize=12]',
        '  node [shape=circle, fixedsize=true, width=.3, height=.3, fontsize=12]',
        '  edge [arrowsize=0.6]',
        f'  {s} [style=filled, fillcolor=blue, label="{s}(S)"]',
        f'  {t} [style=filled, fillcolor=red, label="{t}(T)"]',
    ]    
    for (u, v, cap,cost) in f:
        lines += [f' {u} -> {v} [label=<<font color="green">{f[(u, v, cap,cost)]}/{cap}</font>,<font color="red">{cost}</font>>]']

    lines += ['}']
    return '\n'.join(lines)


def save_dot_file(content, filename):
    """
    input:
        content: string of the graph in dot 
        filename: name of the foutput file
    """
    with open(f"output/{filename}.dot", "w") as file:
        file.write(content)

def make_Rf(E, f):
    """
    input:
        E: list of edges (start,end,capacity,cost)
        f: flow dictionary (edge: value)
    output:
        residual dictionary (edge : value)
    """
    Rf = {}
    for (u, v, cap, cost) in E:
        Rf[(u, v, cap,  cost)] = cap - f[(u, v, cap,  cost)]
        Rf[(v, u, cap, -cost)] = f[(u, v, cap,  cost)]
    return Rf

def extract_path( prev_edges, s, t):
    """
    input:
        prev_edges: dico (vertex : edge)
        s: vertex
        t: vertex
    output:
        liste of edge : path from s to t in Rf
    """    
    path = []
    current = t
    while current != s:
        if current not in prev_edges:
            return None
        prev_edge=prev_edges[current]
        path.append(prev_edge)
        current=prev_edge[0]
    path.reverse()
    return path
