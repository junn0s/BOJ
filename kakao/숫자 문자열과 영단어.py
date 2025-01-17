def solution(s):
    number_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for word, digit in number_words.items():
        while word in s:  
            s = s.replace(word, digit, 1)
            
    answer = int(s)
    return answer


s = input()
print(solution(s))
    
