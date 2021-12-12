def solution(begin, target, words):
    answer = 0
    
    if target in words:
        idx_info = []
        for i in range(len(begin)):
            if begin[i] != target[i]:
                idx_info.append(i)
        
        print(idx_info)
        
        words.remove(target)
        
        for i in idx_info:
            for word in words:
                tmp = begin
                
                if tmp[i] != word[i] and target[i] == word[i]:
                    tmp = tmp[:i] + word[i] + tmp[i + 1:]
                    print("tmp: ", tmp)
                
                    if tmp == word:
                        words.remove(word)
                        answer += 1
                        begin = tmp
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))