#冒泡：两两比较

def bubble_sort(alist):

    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

#选择排序：选小放前面
def select_sort(alist):
    n=len(alist)
    for j in range(n-1):
        min_index=j
        for i in range(j+1,n):
            if alist[min_index]>alist[i]:
                min_index=i
        alist[min_index],alist[j]=alist[j],alist[min_index]

#插入排序:有序无序,选取有序后一位，比较插入前面
def insert_sort(alist):
    n=len(alist)
    for i in range(1,n):
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
        #及时退出
            else:
                break

#快速排序：在alist本身操作，分区，递归，用到指针low，high
def quick_sort(alist,first,last):
    #这边我为什么一开始用等于号
    if first>=last:
        return
    n=len(alist)
    low=first
    high=last
    mid=alist[first]


    while low<high:
        #这边等于关注一下，如果下面也用=号，会出现什么情况
        while low<high and alist[high]>=mid:
            high-=1
        alist[low]=alist[high]
        while low<high and alist[low]<mid:
            low+=1
        alist[high]=alist[low]
    alist[low]=mid
    #传入的参数，关注一下
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)

#归并排序，先分裂，后合并，递归，新列表
def guibing_sort(alist):
    n=len(alist)
    mid=n//2

    if n<=1:
        return alist
    left_alist=guibing_sort(alist[:mid])
    right_alist=guibing_sort(alist[mid:])
    result = []
    left,right=0,0
    while left<len(left_alist) and right<len(right_alist):
        if left_alist[left]<=right_alist[right]:
            result.append(left_alist[left])
            left+=1
        else:
            result.append(right_alist[right])
            right+=1
    result+=left_alist[left:]
    result+=right_alist[right:]
    return result

#二分查找
#递归
def binary_search(alist,k):
    n=len(alist)
    mid=n//2
    if not alist:
        return False
    if k==alist[mid]:
        return True
    elif k>alist[mid]:
        return binary_search(alist[:mid],k)
    else:
        return binary_search(alist[mid+1:],k)

#非递归
#这个算法当时为什么绕不过来
def binary_search2(alist,k):
    n=len(alist)
    l=0
    r=n-1
    while l<=r:
        mid=l+(r-1)//2
        if alist[mid]==k:
            return True
        elif alist[mid]<k:
            l=mid+1
        else:
            r=mid-1
    return False

#时间复杂度
#冒泡：

