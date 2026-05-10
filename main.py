import os
from utils import*
from min_cut_max_flow import *
from min_cost_flow import *
from negative_cycle import *


if __name__ == "__main__":
    test_files= [f for f in os.listdir("tests") ]
    for test in test_files:

        print(f"\n\n\n--- {test} ---")

        lignes= open(f'tests/{test}').readlines()


        E, s, t, n, m = formate_input_datas(lignes)

        print("--- algo ford fulkerson ---")
        max_flow_min_cut,max_flow_min_cut_value,min_cut= max_flow_min_cut_ford_fulkerson(E, s, t)
        content= formate_output_datas(max_flow_min_cut,s,t)
        save_dot_file(content, f'{test}_max_flow')
        print(f"max flow value : {max_flow_min_cut_value}")
        print(f'min cut : {min_cut}')
        
        print("--- algo Bellman Ford ---")
        max_flow_min_cost, max_flow_min_cost_value , min_cost= min_cost_flow_Bellman_Ford(E, s, t,n)
        content= formate_output_datas(max_flow_min_cost,s,t)
        save_dot_file(content, f'{test}_min_cost_BF')
        print(f"max flow value : {max_flow_min_cost_value}")
        print(f'min cost : {min_cost}')

        print("--- algo Dijkstra ---")
        max_flow_min_cost, max_flow_min_cost_value , min_cost= min_cost_flow_dijkstra(E, s, t,n)
        content= formate_output_datas(max_flow_min_cost,s,t)
        save_dot_file(content, f'{test}_min_cost_D')
        print(f"max flow value : {max_flow_min_cost_value}")
        print(f'min cost : {min_cost}')