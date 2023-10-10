# https://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz

import time

freqs = {}

with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    lines = f.readlines()

    start_time = time.time()

    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] = freqs[word] + count
        else:
            freqs[word] = count
    end_time = time.time()
    print(f"{end_time - start_time:.4f}")