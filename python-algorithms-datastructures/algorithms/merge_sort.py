def merge(left, right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i+=1
        else:
            result.append(right[j]); j+=1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def merge_sort(arr):
    arr = list(arr)
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    print(merge_sort([3,6,1,0,9,2]))