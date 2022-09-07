# Hello, this is my attempt at the code challenge for the PhD position at Juelich
import ast
import sys

import numpy as np
import pandas as pd


input_graph = input("Please enter the graph you want to analyze: ")
input_graph = ast.literal_eval(input_graph)
node = input("Please enter the node you want to calculate the depth of: ")

def CreateAdjacencyMatrix(graph):
    elements = list(sorted({ele for val in graph.values() for ele in val}))
    for i in graph.keys():
        elements.append(i)
    elements = np.unique(elements)
    adjacencymatrix = pd.DataFrame(np.zeros((len(elements), len(elements))), columns = sorted(elements), index = sorted(elements))
    for key in graph:
        for value in graph[key]:
            if value in graph[key]:
                adjacencymatrix.loc[key, value] += 1
    return adjacencymatrix


am = CreateAdjacencyMatrix(input_graph)

def depth_calculator(adjacencymatrix, node):
    output = {}
    for i in adjacencymatrix.index:
        if adjacencymatrix.loc[i, node] == 1:
            output[i] = [i]
    for i in output.keys():
        while 'root' not in output[i]:
            for j in adjacencymatrix.columns:
                if adjacencymatrix.loc[j, output[i][-1]] == 1:
                    output[i].append(j)
    result = []
    for i in output.keys():
        result.append(len(output[i]))
    return (print('The depth between node ' + str(node) + ' and the DAG\'s root is ' + str(min(result))))

result = depth_calculator(am, node)


