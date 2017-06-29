import requests
#function that takes a list and return a list that containt new list but no duplicates

a_list = [1,1,3,4,5,2,3,5]

def deduplicate_list(alist):
	_list = []
	for i in alist:
		if i not in _list:_list.append(i)
	sorted_list = bubbleSort(_list)
	return sorted_list


def bubbleSort(new_list):
	for i in range(len(new_list) - 1 , 0 , -1):
		for k in range(i):
			if new_list[k] > new_list[k + 1]:
				tmp = new_list[k]
				new_list[k] = new_list[k + 1]
				new_list[k + 1] = tmp
	return new_list
	
	
#Using sets
def deduplicate_list_V2(alist):
	return list(set(alist))
				
	
		
print(deduplicate_list(a_list))
print(deduplicate_list_V2(a_list))