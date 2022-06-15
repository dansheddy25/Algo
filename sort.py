
def sort(list):
    j = len(list)
    while i <= j:
        if list[i] > list[i +1]:
            list[i], list[i +1] = list[i +1], list[i] 
        i+=1

num = [2,5,1,3]

verify = sort(num)
print(verify)

