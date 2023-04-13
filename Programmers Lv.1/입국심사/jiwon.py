def solution(n, times):
    answer = 0
    start=1
    end=max(times)*n
    
    while start<=end:
        mid=(start+end)//2
        possible_n = sum([mid//t for t in times])
        if possible_n<n:
            start=mid+1
        elif possible_n>=n:
            end=mid-1
            answer=mid
    
    return answer