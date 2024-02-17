def binnar_find(N,ex):
	if len(N)==1:
		if N[0]>=ex:#если в массиве 1 число, то верни индекс слева или справа
			return (0)
		else:
			return(1) 
	elif len(N)==0:
		return(0) #массв сорт пуст - верни первый индекс
	else:
		mid=len(N)//2
		left=N[:mid]
		right=N[mid:]
		if left[-1]>=ex:
			return(binnar_find(left,ex))
		elif right[-1]>=ex:
			return(mid+binnar_find(right,ex))
		else:
			return(len(N)) #если число больше массива-верни последний индекс

def inser_sort(sort=[],not_sort=[]):
	if len(not_sort)==0:
		return(sort)
	else:
		value=not_sort.pop(0)
		j=binnar_find(sort,value)
		newsort=[]
		for i in range(len(sort)+1):
			if i<j:
				newsort.append(sort[i])
			elif i==j:
				newsort.append(value)
			else:
				newsort.append(sort[i-1])
		return(inser_sort(newsort,not_sort))


N=input("введите массив чисел через пробел: ")
N=[float(i) for i in N.split()]
N=inser_sort([],N)
print("ваш отсортированный массив: "+ str(N))


