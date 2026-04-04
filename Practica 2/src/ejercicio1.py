# Práctica 2, ejercicio 1

def text_statistics (text):
    print(f"{"-"*10} Text Statistics {"-"*10}")
    # amount of lines
    lines = text.split(".")
    amount_of_lines = len(lines)
    print(f"Total lines: {amount_of_lines}")

    # total words
    words = text.split()
    amount_of_words = len(words)
    print(f"Total words: {amount_of_words}")

    # average words per line
    words_per_line = amount_of_words / amount_of_lines
    print (f"Average words per line: {words_per_line:.2f}")

    # lines above average
    print (f"Lines above average:")
    for line in lines:
        list_of_words = line.split()
        amount = len(list_of_words)

        if amount > words_per_line:
            print(f"-'{line.strip()}'")

    print("-"*37)

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""