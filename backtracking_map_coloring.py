from collections import OrderedDict
import operator
graph={"WA": ["NT", "SA"],
		"SA": ["WA", "NT", "Q", "NSW", "V"],
		"NT": ["WA", "SA", "Q"],
		"Q": ["NT", "SA", "NSW"],
		"NSW": ["SA", "Q", "V"],
		"V": ["SA", "NSW"],
		"T": []}

colors=["red", "green", "blue"]

assignment={i:None for i in graph}
#print(assignment)

def completion_check(assignment):
	for i in assignment:
		if assignment[i]==None:
			return False
	return True

def consistency_check(variable, value, assignment):
	assignment[variable]=value
	print("assignment in consistency_check", assignment)
	for neighbour in graph[variable]:
		if assignment[neighbour]==assignment[variable]:
			print("inconsistent")
			assignment[variable]=None
			return False
	print("consistent")
	assignment[variable]=None
	return True


def select_unassigned_variable(assignment):
	global colors
	counter={}
	queue=[]
	for i in assignment:
		if assignment[i]==None:
			print("i", i)
			queue.append(i)
			for neighbour in graph[i]:
				if assignment[neighbour]==None:
					print("neighbour of ", i, ": ", neighbour)
					queue.append(neighbour)
			break
	while queue:
		curr=queue.pop(0)
		print("curr", curr)
		counter[curr]=3
		for color in colors:
			if consistency_check(curr, color, assignment) is False:
				counter[curr]-=1

	counter=dict(sorted(counter.items(), key=lambda item: item[1]))
	print("counter", counter)	
	return list(counter.keys())[0]

	#####Degree Heuristic, tie-breaker. Choose the variable with the most constraints on remaining variables.
	#min_value=min(counter.items(), key=lambda item: item[1])
	#if counter.values().count(min_value)>1:
		#tie_breaker=[]
		#heu={}
		#for i in counter:
			#if counter[i]==min_value:
			#tie_breaker.append(i)
		#while tie_breaker:
			#curr=tie_breaker.pop(0)
			#heu[curr]=0
			#for neighbour in graph[curr]:
				#if assignment[neighbour]==None:
					#heu[curr]+=1
		#heu=dict(sorted(heu.items(), key=lambda item: item[1]))
		#return list(counter.keys())[0]		


#def order_domain_values(variable, assignment):
	#global colors
	#option={}
	#for color in colors:
		#if consistency_check(variable, color, assignment) is True:
			#for neighbour in graph[variable]:
				#if assignment[neighbour]==None:
					#temp_options=options(neighbour,color, assignment)
					#option[color]=temp_option+option[color]
	#option=dict(sorted(option.items(), key=lambda, item:item[1]))
	#return list(option.keys())[-1]


def backtrack(assignment):
	global colors
	if completion_check(assignment):
		return assignment
	var=select_unassigned_variable(assignment)
	print("var selected", var)
	for color in colors:
		if consistency_check(var, color, assignment):
			assignment[var]=color 
			result=backtrack(assignment)
			if result != None:
				return result
	return failure

backtrack(assignment)
print(assignment)










#print(completion_check(assignment))

