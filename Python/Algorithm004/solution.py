def indice_quadruplet(nums):
    target=int(input("target: "))
    n= len(nums)
    list_1 = []
    
    if n<4 :
        raise TypeError("We can't find a such quadruplet")
    else:
        
        for i in range(n):

            for j in range(i+1,n):

                for k in range(j+1 , n):

                    for l in range(k+1 , n):

                        if nums[i]+nums[j]+nums[k]+nums[l]== target:

                            list_1.append([nums[i],nums[j],nums[k],nums[l]])
                        #else:
                         #   print("For this target, indices do not exist")

    return list_1