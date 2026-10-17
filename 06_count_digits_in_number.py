number = 87692543
i = 0

while number > 0:
  # last_digit = number % 10
  # print(last_digit)
  number = number// 10
  i+= 1

print('total digits in given number', i)
