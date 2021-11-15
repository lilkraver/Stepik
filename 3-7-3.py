count_dict = int(input())
dict = []
check_words = []
result = []
for i in range(count_dict):       #заполняем словарь
  dict.append(input().lower())
count_lines = int(input())
for i in range(count_lines):        #заполняем список проверяемых слов
  check_words += input().lower().strip().split(' ')
