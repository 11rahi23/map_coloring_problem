import random

graph={"WA": ["NT", "SA"],
		"SA": ["WA", "NT", "Q", "NSW", "V"],
		"NT": ["WA", "SA", "Q"],
		"Q": ["NT", "SA", "NSW"],
		"NSW": ["SA", "Q", "V"],
		"V": ["SA", "NSW"],
		"T": []}
#print(graph)

colors=["red", "green", "blue"]
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
		print("color[",i,"]", color[i])
		if all(constraint(x,y) for y in color[j]):
			print("constraint detected")
			color[i].remove(x)
			print("now color[",i,"]", color[i])
				#x=color[i][0]
				#print("x: ", x)
			revised=True
	return revised

def arc_consistency(graph):
	arcs=generate_arcs(graph)
	queue=[]
	for arc in arcs:
		queue.append(arc)
	index=0
	while 1:
		color["WA"]=[colors[random.randint(0,2)]]
		color["SA"]=[colors[random.randint(0,2)]]
		print("Initialized WA as: ", color["WA"])
		print("Initialized SA as: ", color["SA"])

		#queue.append(["SA","NT"])
		#queue.append(["SA", "WA"])
		print("queue", queue)

		while queue:
			pair=queue.pop(0)
			i=pair[0]
			j=pair[1]
			print("i,j", i,j)
			print("colors of ", i, "and ", j, "are ", color[i], color[j])
			if revise(i,j):
				if not color[i]:
					print("DOMAIN NULLIFIED!!!! Reinitializing....")
					arc_consistency(graph)
				for neighbour in graph[i]:
					queue.append([neighbour,i])
				print("now queue", queue)
		return True

		


arc_consistency(graph)
print(color)