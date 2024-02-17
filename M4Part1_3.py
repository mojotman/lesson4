

def weigth_graph(graph,startM=[], visited=[]):
	if len(startM)==0:
		return
	view=[]
	for start in startM:
		if start not in graph.keys():
			print("такой точки нет")
			return(-1)
		if start not in visited:
			visited.append(start)
		for v in graph[start]:
			if v not in visited:
				visited.append(v)
				view.append(v)
	weigth_graph(graph,view,visited)
	return(visited)


graph={
	1: set([2,3]),
	2: set([4,5]),
	3: set([6,7]),
	4: set([8]),
	5: {},
	6: {},
	7: {},
	8: {},
}

print(graph)



print(weigth_graph(graph,[1],[]))




