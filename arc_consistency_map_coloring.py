graph={"WA": ["NT", "SA"],
		"SA": ["WA", "NT", "Q", "NSW", "V"],
		"NT": ["WA", "SA", "Q"],
		"Q": ["NT", "SA", "NSW"],
		"NSW": ["SA", "Q", "V"],
		"V": ["SA", "NSW"],
		"T": []}
#print(graph)

color = {i:["green", "blue", "red"] for i in graph}
#print (color)

def generate_arcs(graph):
	arcs=[]
	for i in graph:
		print ("i: ", i)
		for neighbour in graph[i]:
			print("Neighbour of" ,i, "is: ", neighbour)
			if (neighbour,i) not in arcs:
				arcs.append([i,neighbour])
				print(arcs)
	return arcs


# generate_arcs(graph)
# print(arcs)

def constraint(i,j):
	if i==j:
		return True
	else:
		return False

def revise(i,j):
	revised=False
	print("i,j in revise:", i,j)
	for x in color[i]:
		print("x", x)
		print("color[", i,"]", color[i])
		for y in color[j]:
			print("y",y)
			if constraint(x,y):
				print("constraint detected")
				color[i].remove(x)
				print("now color[",i,"]", color[i])
				revised=True
	return revised

def arc_consistency(graph):
	arcs=generate_arcs(graph)
	queue=[]
	queue.append(arcs[0])
	print("queue", queue)

	while queue:
		pair=queue.pop(0)
		i=pair[0]
		j=pair[1]
		print("i,j", i,j)
		if revise(i,j):
			if color[i]==0:
				return False
			for neighbour in graph[i]:
				queue.append([neighbour,i])
			print("now queue", queue)
			print("now color profile: ", color)
	return True


arc_consistency(graph)
print(color)

