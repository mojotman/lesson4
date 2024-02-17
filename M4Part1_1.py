def binnar_find(N,ex):
	if len(N)==1:
		if N[0]==ex:
			return (0)
		else:
			print("данного числа нет в массиве")
			return(-1)
	elif len(N)==0:
		print("массив не задан")
		return(-1)
	else:
		mid=len(N)//2
		left=N[:mid]
		right=N[mid:]
		if left[-1]>=ex:
			return(binnar_find(left,ex))
		elif right[-1]>=ex:
			return(mid+binnar_find(right,ex))
		else:
			print("данного числа нет в массиве")
			return(-1)


N=input("введите массив чисел через пробел: ")
N=sorted([float(i) for i in N.split()])
print("ваш отсортированный массив: "+ str(N))
ex=float(input("введите число, что хотите найти: "))


i=binnar_find(N,ex)
print("индекс данного числа в массиве равен: "+str(i))