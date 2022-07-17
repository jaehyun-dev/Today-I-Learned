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


# 22.07.11 22:08

# Fibonacci Sequence with Optimized Space Complexity

def fib_optimized(n):
    # 코드를 작성하세요. 
    previous = 0
    current = 1
    i = 0
    while i < n - 1:
        current, previous = previous + current, current
        i += 1
    return current

# 모범답안
# def fib_optimized(n):
#     current = 1
#     previous = 0

#     # 반복적으로 위 변수들을 업데이트한다. 
#     for i in range(1, n):
#         current, previous = current + previous, current

#     # n번재 피보나치 수를 리턴한다. 
#     return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))



# Max Profit
### Memoization 익숙지 않은 듯
### 고민 깊게 하지 못하고 해설 봄

def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    # base case
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]
    
    # 이미 count개의 최대 수익이 계산됐으면:
    # 저장된 값을 바로 리턴한다
    if count in cache:
        return cache[count]
        
    # 아직 count개의 최대 수익이 계산되지 않았으면:
    # 계산을 한 후 cache에 저장 
    max_profit_count = 0
    for i in range(1, count // 2 + 1):
        max_profit_count = max(max_profit_count, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))
        
    cache[count] = max_profit_count
    
    if count < len(price_list):
        cache[count] = max(cache[count], price_list[count])
    
    return cache[count]
    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 모범답안
# def max_profit_memo(price_list, count, cache):
#     # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
#     if count < 2:
#         cache[count] = price_list[count]
#         return cache[count]

#     # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
#     if count in cache:
#         return cache[count]

#     # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#     if count < len(price_list):
#         profit = price_list[count]
#     else:
#         profit = 0

#     # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
#     for i in range(1, count // 2 + 1):
#         profit = max(profit, max_profit_memo(price_list, i, cache) 
#                  + max_profit_memo(price_list, count - i, cache))

#     # 계산된 최대 수익을 cache에 저장
#     cache[count] = profit

#     return profit


# def max_profit(price_list, count):
#     max_profit_cache = {}

#     return max_profit_memo(price_list, count, max_profit_cache)



# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))





# 22.07.15 01:07

# Max Profit by Tabulation
def max_profit(price_list, count):
    # 코드를 작성하세요.
    max_profit_list = []
    for i in range(len(price_list)):
        max_profit_list.append(price_list[i])
    
    for i in range(count - len(price_list) + 1):
        max_profit_list.append(0)
    
    for i in range(2, count + 1):
        max_profit_count = 0
        for j in range(1, i // 2 + 1):
            max_profit_count = max(max_profit_count, max_profit_list[j] + max_profit_list[i - j])
        if max_profit_count > max_profit_list[i]:
            max_profit_list[i] = max_profit_count    
    return max_profit_list[count]

# 모범답안
# def max_profit(price_list, count):
#     # 개수별로 가능한 최대 수익을 저장하는 리스트
#     # 새꼼달꼼 0개면 0원
#     profit_table = [0]

#     # 개수 1부터 count까지 계산하기 위해 반복문
#     for i in range(1, count + 1):
#         # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정   
#         if i < len(price_list):
#             profit = price_list[i]
#         else:
#             profit = 0

#         # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
#         for j in range(1, i // 2 + 1):
#             profit = max(profit, profit_table[j] + profit_table[i - j])

#         profit_table.append(profit)

#     return profit_table[count]

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))



# 22.07.15 22:31
# Minimum Coin Count

def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    coin_list.sort(reverse = True)
    num_coins = 0
    value_remain = value
    for i in coin_list:
        num_i = value_remain // i
        value_remain -= i * num_i
        num_coins += num_i    
    return num_coins    

# 모범답안
# def min_coin_count(value, coin_list):
#     # 누적 동전 개수
#     count = 0

#     # coin_list의 값들을 큰 순서대로 본다
#     for coin in sorted(coin_list, reverse=True):
#         # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
#         count += (value // coin)

#         # 잔액을 계산한다
#         value %= coin

#     return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))


# Max Card Product

def max_product(card_lists):
    # 코드를 작성하세요.
    product = 1
    for i in card_lists:
        max_card = 1
        for j in i:
            max_card = max(max_card, j)
        product *= max_card
    return product

# 모범답안
# def max_product(card_lists):
#     # 누적된 곱을 저장하는 변수
#     product = 1

#     # 반복문을 돌면서 카드 뭉치를 하나씩 본다
#     for card_list in card_lists:
#         # product에 각 뭉치의 최댓값을 곱해 준다
#         product *= max(card_list)

#     return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))


# Minimum Fee

def min_fee(pages_to_print):
    # 코드를 작성하세요.
    time_sum = 0
    i = 0
    j = 0
    while i < len(pages_to_print):
        while j < len(pages_to_print):
            time_sum += sorted(pages_to_print)[i] * (len(pages_to_print)-j)    
            i += 1
            j += 1
    return time_sum

# 모범답안
# def min_fee(pages_to_print):
#     # 인풋으로 받은 리스트를 정렬시켜 준다
#     sorted_list = sorted(pages_to_print)

#     # 총 벌금을 담을 변수
#     total_fee = 0

#     # 정렬된 리스트에서 총 벌금 계산
#     for i in range(len(sorted_list)):
#         total_fee += sorted_list[i] * (len(sorted_list) - i)

#     return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))


# Course Selection

def course_selection(course_list):
    # 코드를 작성하세요.
    temp_list = []

    for course in course_list:
        temp_list.append(tuple(reversed(course)))
    
    temp_list.sort()
    
    course_pick = []
    course_pick.append(temp_list[0])
    
    for i in range(1, len(temp_list)):
        if temp_list[i][1] > course_pick[-1][0]:
            course_pick.append(temp_list[i])
    
    final_list = []
    for course in course_pick:
        final_list.append(tuple(reversed(course)))
    
    return final_list
  
# 모범답안
# def course_selection(course_list):
#     # 수업을 끝나는 순서로 정렬한다
#     sorted_list = sorted(course_list, key=lambda x: x[1])

#     # 가장 먼저 끝나는 수업은 무조건 듣는다
#     my_selection = [sorted_list[0]]

#     # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
#     for course in sorted_list:
#         # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
#         if course[0] > my_selection[-1][1]:
#             my_selection.append(course)

#     return my_selection    

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))


# 22.07.17 22:58

# 투자 귀재 규식이 I

def sublist_max(profits):
    # 코드를 작성하세요.
    profit_list = []
    for i in range(len(profits)):
        profit = 0
        for j in range(i, len(profits)):
            profit += profits[j]
            profit_list.append(profit)
    
    return max(profit_list)

# 모범답안
# def sublist_max(profits):
#     max_profit = profits[0] # 최대 수익
    
#     for i in range(len(profits)):
#         # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
#         total = 0
        
#         for j in range(i, len(profits)):
#             # i부터 j까지 수익의 합을 계산
#             total += profits[j]
            
#             # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
#             max_profit = max(max_profit, total)

#     return max_profit
    
# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
