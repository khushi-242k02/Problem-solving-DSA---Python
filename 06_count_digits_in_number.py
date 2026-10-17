number = 87692543
n = number
i = 0

while n > 0:
  # last_digit = n % 10
  # print(last_digit)
  n = n// 10
  i+= 1

print('total digits in given number', i)
