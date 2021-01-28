# Enter number of lines
n = int(input())

lines = ""
for _ in range(n):
    # Enter text
    lines += " " + input()

word_and_freq = {}  # Keep track of the words and their frequencies
for word in lines.strip().split():
    freq = word_and_freq.get(word, 0)+1
    word_and_freq.update({word: freq})

new = {k: v for k, v in sorted(
    word_and_freq.items(), key=lambda item: (-item[1], item[0]))}

# Print output
for word, _ in new.items():
    print(word)
