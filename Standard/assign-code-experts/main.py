# main python file

import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def random_number():
    return random.randint(1, 100)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def random_list(length):
    return [random_number() for _ in range(length)]

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def shuffle_string(word):
    chars = list(word)
    random.shuffle(chars)
    return ''.join(chars)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def reverse_list(lst):
    return lst[::-1]

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def random_color():
    return '#' + ''.join(random.choice(string.hexdigits) for _ in range(6))

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def find_max(lst):
    if len(lst) == 0:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def find_min(lst):
    if len(lst) == 0:
        return None
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

def random_matrix(rows, cols):
    return [[random_number() for _ in range(cols)] for _ in range(rows)]

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def convert_to_binary(num):
    return bin(num)[2:]

def convert_to_decimal(binary):
    return int(binary, 2)

def calculate_area_of_circle(radius):
    return 3.14159 * radius ** 2

def calculate_circumference_of_circle(radius):
    return 2 * 3.14159 * radius

def generate_fibonacci_sequence(length):
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def remove_duplicates(lst):
    return list(set(lst))

def generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def linear_search(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_interpolation(x, x1, y1, x2, y2):
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

def random_choice(lst):
    return random.choice(lst)

def generate_random_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

def random_boolean():
    return random.choice([True, False])

def main():
    # Generate a random string of length 10
    random_string = generate_random_string(10)
    print("Random String:", random_string)

    # Generate a random number between 1 and 100
    number = random_number()
    print("Random Number:", number)

    # Check if a number is prime
    prime = is_prime(number)
    print("Is Prime:", prime)

    # Generate a random list of length 5
    lst = random_list(5)
    print("Random List:", lst)

    # Count the number of vowels in a word
    word = "Hello, World!"
    vowel_count = count_vowels(word)
    print("Vowel Count
