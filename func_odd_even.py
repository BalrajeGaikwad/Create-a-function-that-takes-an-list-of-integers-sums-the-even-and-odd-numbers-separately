def odd_even(numbers):
    even=0
    odd=0
    for num in numbers:
        if num%2==0:
            even+=num
        else:
            odd+=num

    return even-odd

print(odd_even([1, 2, 3, 4, 5, 6]))