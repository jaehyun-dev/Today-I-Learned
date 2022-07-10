# 22.07.06

# Fibonacci Sequence

# n번째 피보나치 수를 리턴
def fib(n):
    # 코드를 입력하세요.
    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))



# Triangle Number

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # 코드를 입력하세요
    if n == 1:
        return 1
    return triangle_number(n-1) + n

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))


# Sum of digits

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))



# Flipping List

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # 코드를 입력하세요.
    if len(some_list) <= 1:
        return some_list
    new_list = []
    new_list.append(some_list[-1])
    return new_list + flip(some_list[0:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)



# Binary_Search by Recurssion

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    if start_index == end_index:
        if element == some_list[start_index]:
            return start_index
        return None
    elif start_index < end_index:
        midpoint = (start_index + end_index) // 2
        if element == some_list[midpoint]:
            return midpoint
        elif element < some_list[midpoint]:
            return binary_search(element, some_list, start_index, midpoint - 1)
        elif element > some_list[midpoint]:
            return binary_search(element, some_list, midpoint + 1, end_index)
    return None
        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))




# Tower of Hanoi

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    peg_list = [1, 2, 3]
    peg_list.remove(start_peg)
    peg_list.remove(end_peg)
    temp_peg = peg_list[0]
    if num_disks < 1:
        return None
    elif num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
    else:
        hanoi(num_disks - 1, start_peg, temp_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, temp_peg, end_peg)
    
    
# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)



# 22.07.07 00:43

# Max Product

def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    product_list = []
    for i in left_cards:
        for j in right_cards:
            product_list.append(i * j)
    return max(product_list)
    
# def max_product(left_cards, right_cards):
#     max_product = left_cards[0] * right_cards[0]
#     for left in left_cards:
#         for right in right_cards:
#             max_product = max(max_product, left * right)
    
#     return max_product 
    
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))



# Closest Pair

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    min_distance = distance(coordinates[0], coordinates[1])
    closest_stores = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i < j:
                if distance(coordinates[i], coordinates[j]) < min_distance:
                    min_distance = distance(coordinates[i], coordinates[j])
                    closest_stores[0] = coordinates[i]
                    closest_stores[1] = coordinates[j]
                
    return closest_stores

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


# Trapping Rain

def trapping_rain(buildings):
    # 코드를 작성하세요
    rain = 0
    for i in range(1, len(buildings) - 1):
        left_bound = max(buildings[:i])
        right_bound = max(buildings[i:])
        bound = min(left_bound, right_bound)
        rain += max(0, bound - buildings[i])
    
    return rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))



# 22.07.08 04:03

# Consecutive Sum

def consecutive_sum(start, end):
    # 코드를 작성하세요

    # base case: start와 end가 같으면 start값 반환하기
    if start == end:
        return start
    
    # recursive case: 절반씩 분할하여 정복하기.
    return consecutive_sum(start, (start + end) // 2) + consecutive_sum((start + end) // 2 + 1, end)

# def consecutive_sum(start, end):
#     # base case   
#     if start == end:
#         return start
    
#     # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
#     mid = (start + end) // 2
    
#     # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
#     return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))


 
# 22.07.09 22:45

# List Merge Function

def merge(list1, list2):
    # 코드를 작성하세요.
    if len(list1) == 0 or len(list2) == 0:
        return list1 + list2
    new_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    if i == len(list1):
        return new_list + list2[j:]
    else:
        return new_list + list1[i:]


# 모범답안    
# def merge(list1, list2):
#     i = 0
#     j = 0

#     # 정렬된 항목들을 담을 리스트
#     merged_list = []

#     # list1과 list2를 돌면서 merged_list에 항목 정렬
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merged_list.append(list2[j])
#             j += 1
#         else:
#             merged_list.append(list1[i])
#             i += 1

#     # list2에 남은 항목이 있으면 정렬 리스트에 추가
#     if i == len(list1):
#         merged_list += list2[j:]

#     # list1에 남은 항목이 있으면 정렬 리스트에 추가
#     elif j == len(list2):
#         merged_list += list1[i:]

#     return merged_list

    
    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))




# Merge Sort

def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    if len(list1) == 0 or len(list2) == 0:
        return list1 + list2
    new_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    if i == len(list1):
        return new_list + list2[j:]
    else:
        return new_list + list1[i:]

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    
    # base case: my_list has only one or no element
    if len(my_list) <= 1:
        return my_list
        
    # recursive case: when there are more than one elemet, divde the list into half    
    mid = len(my_list) // 2
    my_list_left = my_list[:mid]
    my_list_right = my_list[mid:]
    return merge(merge_sort(my_list_left), merge_sort(my_list_right))


# 모범답안
# def merge(list1, list2):
#     i = 0
#     j = 0

#     # 정렬된 항목들을 담을 리스트
#     merged_list = []

#     # list1과 list2를 돌면서 merged_list에 항목 정렬
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merged_list.append(list2[j])
#             j += 1
#         else:
#             merged_list.append(list1[i])
#             i += 1

#     # list2에 남은 항목이 있으면 정렬 리스트에 추가
#     if i == len(list1):
#         merged_list += list2[j:]

#     # list1에 남은 항목이 있으면 정렬 리스트에 추가
#     elif j == len(list2):
#         merged_list += list1[i:]

#     return merged_list


# def merge_sort(my_list):
#     # base case
#     if len(my_list) < 2:
#         return my_list

#     # my_list를 반씩 나눈다(divide)
#     left_half = my_list[:len(my_list)//2]    # 왼쪽 반
#     right_half = my_list[len(my_list)//2:]   # 오른쪽 반

#     # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
#     # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
#     return merge(merge_sort(left_half), merge_sort(right_half))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))




# Partition

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    b = start
    i = start
    p = end
    while i < len(my_list) - 1:
        if my_list[i] > my_list[p]:
            i += 1 
        else:
            swap_elements(my_list, b, i)
            b += 1
            i += 1
    swap_elements(my_list, b, p)
    return my_list.index(p) - 1
    
    
# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
#     i = start
#     b = start
#     p = end

#     # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
#     while i < p:
#         # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
#         if my_list[i] <= my_list[p]:
#             swap_elements(my_list, i, b)
#             b += 1
#         i += 1

#     # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
#     swap_elements(my_list, b, p)
#     p = b

#     # pivot의 최종 인덱스를 리턴해 준다
#     return p

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)



# QuickSort

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

    
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    b = start
    i = start
    p = end
    while i < p:
        if my_list[i] > my_list[p]:
            i += 1 
        else:
            swap_elements(my_list, b, i)
            b += 1
            i += 1
    swap_elements(my_list, b, p)
    p = b
    
    return p

    
# 퀵 정렬
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    if end - start < 1:
        return
    p = partition(my_list, start, end)
    quicksort(my_list, start, p - 1)
    quicksort(my_list, p + 1, end)
    
    
# 모범답안

# # 두 요소의 위치를 바꿔주는 helper function
# def swap_elements(my_list, index1, index2):
#     temp = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = temp

# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
#     i = start
#     b = start
#     p = end

#     # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
#     while i < p:
#         # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
#         if my_list[i] <= my_list[p]:
#             swap_elements(my_list, i, b)
#             b += 1
#         i += 1

#     # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
#     swap_elements(my_list, b, p)
#     p = b

#     # pivot의 최종 인덱스를 리턴해 준다
#     return p

# # 퀵 정렬
# def quicksort(my_list, start, end):
#     # base case
#     if end - start < 1:
#         return

#     # my_list를 두 부분으로 나누어주고,
#     # partition 이후 pivot의 인덱스를 리턴받는다
#     pivot = partition(my_list, start, end)

#     # pivot의 왼쪽 부분 정렬
#     quicksort(my_list, start, pivot - 1)

#     # pivot의 오른쪽 부분 정렬
#     quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)


# QuickSort without start, end Parameters

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    b = start
    i = start
    p = end
    while i < p:
        if my_list[i] > my_list[p]:
            i += 1 
        else:
            swap_elements(my_list, b, i)
            b += 1
            i += 1
    swap_elements(my_list, b, p)
    p = b
    
    return p

# 퀵 정렬 (start, end 파라미터 없이도 호출이 가능하도록 수정해보세요!)
def quicksort(my_list, start = 0, end = None):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    if end == None:
        end = len(my_list) - 1
    if end - start < 1:
        return
    p = partition(my_list, start, end)
    quicksort(my_list, start, p - 1)
    quicksort(my_list, p + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)



# Fibonacci by Memoization

def fib_memo(n, cache):
    # 코드를 작성하세요.
    if n < 3:
        return 1
    if n not in cache:
        cache[n] = fib_memo(n - 2, cache) + fib_memo(n - 1, cache)
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 모범답안

# def fib_memo(n, cache):
#     # base case
#     if n < 3:
#         return 1
        
#     # 이미 n번째 피보나치를 계산했으면:
#     # 저장된 값을 바로 리턴한다
#     if n in cache:
#         return cache[n]
    
#     # 아직 n번째 피보나치 수를 계산하지 않았으면:
#     # 계산을 한 후 cache에 저장
#     cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

#     # 계산한 값을 리턴한다
#     return cache[n]

# def fib(n):
#     # n번째 피보나치 수를 담는 사전
#     fib_cache = {}

#     return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))



# 22.07.10 23:36

# Fibonacci by Tabulation

def fib_tab(n):
    # 코드를 작성하세요.
    if n < 1:
        return None
    elif n < 3:
        return 1
    fib_list = [1, 1]
    i = 0
    while i < n - 2:
        fib_list.append(fib_list[i] + fib_list[i + 1])
        i += 1
    return fib_list[-1]

# 모범답안

# def fib_tab(n):
#     # 이미 계산된 피보나치 수를 담는 리스트
#     fib_table = [0, 1, 1]

#     # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
#     for i in range(3, n + 1):
#         fib_table.append(fib_table[i - 1] + fib_table[i - 2])

#     # 피보나치 n번째 수를 리턴한다
#     return fib_table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
