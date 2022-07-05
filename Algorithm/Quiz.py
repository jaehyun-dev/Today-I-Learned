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
