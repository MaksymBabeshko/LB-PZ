import re
import hashlib

def count_tool_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip(",.!?:;")  # очистка від розділових знаків
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "дриль молоток викрутка дриль викрутка молоток ключ пилка дриль викрутка молоток пилка викрутка"

result = count_tool_words(text)
print("Частота інструментів у тексті:")
print(result)

frequent_words = [word for word, count in result.items() if count > 3]
print("Інструменти, що зустрічаються більше 3 разів:")
print(frequent_words)
