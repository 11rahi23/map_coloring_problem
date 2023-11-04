import random
graph={"WA": ["NT", "SA"],
		"SA": ["WA", "NT", "Q", "NSW", "V"],
		"NT": ["WA", "SA", "Q"],
		"Q": ["NT", "SA", "NSW"],
		"NSW": ["SA", "Q", "V"],
		"V": ["SA", "NSW"],
		"T": []}

colors=["red", "green", "blue"]

assignment={i:None for i in graph}

def completion_check(assignment):
	for i in assignment:
		if assignment[i]==None:
			return False
	return True

def consistency_check(variable, neighbour, value, assignment):
	assignment[variable]=value
	print("assignment in consistency_check", assignment)
	if assignment[neighbour]==assignment[variable]:
		print("inconsistent")
		assignment[variable]=None
		return False
	print("consistent")
	assignment[variable]=None
	return True

def select_unassigned_variable(tree):
	neighbour=tree.pop(-1)
	var=tree[-1]
	print("var, neighbour: ", var, neighbour)

	return var, neighbour


def cutset_conditioning(graph):
	var=0
	for i in graph:
		var+=1
	print("variables: ", var)

	connections = {}
	for i in graph:
		
		connections[i]=len(graph[i])
	print ("connections: ", connections)

	connections=dict(sorted(connections.items(), key=lambda item: item[1]))

	cutoff=list(connections.keys())[-1]
	print(cutoff)

	tree=[]

	for neighbour in graph[cutoff]:
		tree.append(neighbour)

	print(tree)

	return cutoff, tree

def tree_csp(tree, colors):

	if completion_check(assignment):
		return assignment
	var, neighbour=select_unassigned_variable(tree)
	print("var, neighbour: ", var, neighbour)

	for color in colors:
		if consistency_check(var, neighbour, color, assignment):
			assignment[var]=color
			result=tree_csp(tree, colors)
			if result !=None:
				return result
		
	return failure


def init(assignment):
	cutoff, tree= cutset_conditioning(graph)
	assignment["T"]=colors[random.randint(0,2)]
	assignment[cutoff]=colors[random.randint(0,2)]
	print(assignment[cutoff])
	colors.remove(assignment[cutoff])
	print("remaining colors: ", colors)
	assignment[tree[-1]]=colors[0]
	result=tree_csp(tree, colors)

	print("result: ", result)

	return result


init(assignment)
