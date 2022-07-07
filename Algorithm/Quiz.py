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


 
