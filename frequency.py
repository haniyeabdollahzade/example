string = "Python Programming"
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sort_freq = sorted(freq.items(), key=lambda x : x[1], reverse=True)
for k,v in sort_freq:
    print(k, v)            
