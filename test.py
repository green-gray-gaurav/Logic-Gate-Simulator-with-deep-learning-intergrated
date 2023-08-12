iter = [-1]
limits = [4]
iter_index = len(iter)-1
while(True):
    
    if(iter[iter_index] == limits[iter_index]-1):
        iter[iter_index]=0
        if(iter_index==0):
            break
        iter_index-=1
        continue
    iter[iter_index]+=1
    if not iter_index == len(iter)-1 and iter[iter_index+1] == 0:
        iter_index+=1
    
    print(iter)

    