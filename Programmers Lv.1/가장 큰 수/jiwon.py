def solution(numbers):
    numbers = list(map(lambda x:str(x), numbers))
    numbers = sorted(numbers, key=lambda x: (x*4)[:4])[::-1]
    
    if numbers[0]=='0':
        numbers='0'
        
    return ''.join(numbers)