
ipts = input("String to encode: ")
cr = {}
chars = 'qwertyuioplkjhgfdsazxcvbnm`1234567890-=[]\;\',./~!@#$%^&*()_+{}|:"<>?QWERTYUIOPLKJHGFDSAZXCVBNM'
for char in ipts:
  if char not in chars:
    print('Character not supported: ' + char)
    while 1:
      pass
for char in chars:
  cr[char] = chars[(chars.index(char) + 5) % (len(chars) - 1)]
out = ""
for char in ipts:
  out += cr[char]
print(out)
