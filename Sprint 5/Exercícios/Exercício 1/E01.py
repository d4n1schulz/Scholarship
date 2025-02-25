
lines = sc.textFile("/app/README.md")

words = lines.flatMap(lambda line: line.split(" "))

word_counts = words.map(lambda word: (word, 1))

word_counts = word_counts.reduceByKey(lambda a, b: a + b)

results = word_counts.collect()

for (word, count) in results:
    print(f"{word}: {count}")
