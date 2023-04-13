# python3 hash_substring.py

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    command = input()

    if "I" in command:
        pattern = input()
        text = input()

    elif "F" in command:
        fileName = input()

        
        filePath = "./tests/" + fileName
        with open(filePath, mode="r") as fail:
            pattern = fail.readline()
            text = fail.readline()

    else:
        print("error")
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

B = 13
Q = 256

def get_hash(str):
    global B, Q
    m = len(str)
    result = 0

    for i in range(m):
        result = (B * result + ord(str[i])) % Q

    return result

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    pattern_length = len(pattern)
    text_length = len(text)

    multiplier = 1
    for i in range(1, pattern_length):
        multiplier = (multiplier * B) % Q
    
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])

    answer = []

    for i in range(text_length - pattern_length + 1):
        # print("text_hash = ", text_hash, print("text = ", text[i : i+pattern_length]))
        if pattern_hash == text_hash and text[i : i+pattern_length] == pattern:
            answer.append(i)
        
        if i < text_length - pattern_length:
            text_hash = ((text_hash - ord(text[i]) * multiplier) * B + ord(text[i + pattern_length])) % Q

            if text_hash < 0:
                text_hash = text_hash + Q

    # and return an iterable variable
    return answer


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

