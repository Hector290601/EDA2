from hash import *

def findHs(key, arr):
    count = 0
    hs = hash(key, len(arr))                        # 2, una creación de memoria y una asignación de valor
    if str(type(arr[hs])) == "<class 'list'>":      # 6, dos accesos a memoria y cuatro operaciones básicas
        for  i in range(len(arr[hs])):              # 6n-6, tres accesos a memoria y tres operaciones básicas
            count += 1                              # 2, un accceso a memoria y una operación (6n-6) = 12n-12
            if arr[hs][i] == key:                   # 5, cuatro accesos a memoria y una operación (6n-6) = 30n-30
                #return hs, i, count
                return count                        # 2, un acceso a memoria y una operación básica (6n-6) = 12n-12
        #return hs, -1, count
        return count                                # 2, un acceso a memoria y una operación básica
    elif str(type(arr[hs])) == "<class 'int'>":     # 6, un dos accesos a memoria y cuatro operaciones básicas
        count += 1                                  # 2, un acceso a memoria y una operación
        if arr[hs] == key:                          # 4, tres accesos a memoria y una comparación
            #return hash(key, len(arr)), count
            return count                            # 2, un acceso a memoria y una operación básica
        else:                                       # 1, una operación básica
            #return -1, count
            return count                            # 2, un acceso a memoria y una operación básica

#2+6+6n-6+12n-12+30n-30+12n-12+2+6+2+4+2+1+2 = 60n - 33

def findHsWs(key, arr):
    count = 0
    hs = wsHash()
    if str(type(arr[hs])) == "<class 'list'>":
        for i in range(len(arr[hs])):
            print(len(arr[hs]))
            print("Entrando al for")
            count += 1
            if arr[hs][i] == key:
                #return hs, i, count
                return count
        #return hs, -1, count
        return count
    elif str(type(arr[hs])) == "<class 'int'>":
        count += 1
        if arr[hs] == key:
            #return hash(key, len(arr)), count
            return count
        else:
            #return -1, count
            return count

def randomKeyExistant(arr):
    key = 0
    while key == 0:
        key = arr[random.randint(0, (len(arr)-1))]
        if str(type(key)) == "<class 'list'>":
            rnd = random.randint(0, (len(key)-1))
            key = key[rnd]
    return key

def fristKeyExistant(arr):
    key = 0
    while key == 0:
        key = arr[random.randint(0, (len(arr)-1))]
        if str(type(key)) == "<class 'list'>":
            key = 0
    return key

def worseKeyExistant(arr):
    mx = 0
    for i in arr:
        if str(type(i)) == "<class 'list'>":
            for j in i:
                if j > mx:
                    mx = j
        else:
            if i > mx:
                mx = i
    print(mx+1)
    return mx+1

def toPlotHf(arr, wsArr):
    base = findHs(randomKeyExistant(arr), arr)
    best = findHs(fristKeyExistant(arr), arr)
    worse = findHsWs(worseKeyExistant(wsArr), wsArr)
    return base, best, worse


if __name__ == '__main__':
    arr = test(100)
    print(toPlotHf(arr))
