def add_length(str_):
    lst = str_.split()
    return [f"{word} {len(word)}" for word in lst]

str_ = "apple ban"
print(add_length(str_))

