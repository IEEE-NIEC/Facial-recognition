
import json


def creatFile():
	data = {}
	with open('data.txt', 'w') as outfile:  
		json.dump(data, outfile)


def dumpData(name):
	with open('data.txt') as json_file:  
		data = json.load(json_file)
	# print(data)
	# print(type(data))
	if (bool(data)==False):
		data.update({1:name})

	else:
		for id in data:
			pass
		# print(id)
		id=int(id)
		id=id+1
		# print(id)
		data.update({id:name})

	with open('data.txt', 'w') as f:
		json.dump(data, f)

	print(data)
	return id
 
