t = int(input())

classes = {}

def compareClass(name1, name2):
	class1 = classes[name1]
	class2 = classes[name2]
	if len(class1) < len(class2):
		temp = class1
		class1 = class2
		class2 = temp
		temp = name1
		name1 = name2
		name2 = temp
	done = False
	for i in range()


for i in range(0, t):
	n = int(input())
	classes = {}
	names = []
	for j in range(0, n):
		name, clas = [s for s in input().replace(':', '').split(' ')]
		classes[name] = clas.split('-')
		names.append(name)
	sort(name, compareClass)