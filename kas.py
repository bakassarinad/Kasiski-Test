from collections import Counter

def text_mod():
    text = ''
    with open('text.txt') as f:
        text += f.read()
    text = text.replace(" ", "")
    return text.lower()

def get_repeats(text, k):
    ctr = Counter(text[i:i+k] for i in range(len(text) - k + 1))
    return {sub: c for sub, c in ctr.items() if c>1}

def get_last_nonempty_dict(text):
    last_repeat = None
    for i in range(2, 10): # for supposed key length from 2 to 10
        repeats = get_repeats(text, i)
        if repeats:
            last_repeat = repeats
    return last_repeat

def substring_positions(text):
    dictionary = get_last_nonempty_dict(text)
    substring = list(dictionary.keys())[0]
    first_index = text.find(substring)
    second_index = text.find(substring , text.find(substring) + 1)
    return second_index - first_index

def divisors():
    distance = substring_positions(text_mod())
    divisors = []
    for i in range(2, distance + 1):
        if distance % i == 0:
            divisors.append(i)
    return divisors
divisors = divisors()    
print('Here are the possible lengths of the key: ' + ' '.join(str(x) for x in divisors))




#print(substring_positions(text_mod()))