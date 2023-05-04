def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations), 0, -1):
        if i>citations[-1]:
            pass
        citations.append(i)
        citations.sort()
        idx = citations.index(i)
        if i<=len(citations[idx+1:]):
            answer = i
            break
        citations.remove(i)
    
    return answer