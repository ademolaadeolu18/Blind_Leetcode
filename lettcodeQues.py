# find second min in a list


def secondMin(arr):
    min1 = min(arr)
    min2 = float("inf")

    for i in range (len(arr)):
        if arr[i] < min2 and arr[i] > min1:
            min2 = arr[i]
    
    return min2



print(secondMin([-1,5,6,2,-1,3]))



# find the highest average score

def highestAverage(arr):
    avg_dic = {}
    for dic in (arr):
        key, value = dic[0], dic[1]  
        if key in avg_dic:
            avg_dic[key].append(int(value))
        else:
            avg_dic[key] = [int(value)]

    max_avg = 0

    for grades in avg_dic.values():
        max_avg = max( max_avg, sum(grades)/len(grades))

    return max_avg


arr = [["Bob","87"], ["Mike", "35"],["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "99"]]


print(highestAverage(arr))


#linkeddlist
def reverseList(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


