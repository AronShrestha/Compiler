books = [12,34,67,90]



def checker(book,limit,m):
    no_of_std = 1
    pages=0
    for i in range(len(book)):
        if book[i]>limit:
            return False
        if book[i]+pages > limit :
            no_of_std+=1
            pages=book[i]
           
            if no_of_std>m:
                return False
        else:
            pages += book[i]
    
    return True
    
def allocations(books,m):
    low = 50
    high = 120
    mid  = low -int((low-high)/2)
    answer = []
    while low <= high:
 
      
        if checker(books,mid,m):
            answer.append(mid)
            high= mid-1
        else:
            low=mid+1
        mid  = low -int((low-high)/2)
        
    return answer


print(allocations(books,2))
        


        

