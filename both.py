def doall():
  def kofvalue(dic, value):
    for k in dic:
      if dic[k] == value:
        return k
  ipts = input("String to encode: ")
  cr = {}
  bufferchars = 'ÓÔÒÅ'
  chars = 'qwertyuioplkjhgfdsazxcvbnm`1234567890-=[]\;\',./~!@#$%^&*()_+{}|:"<>?QWERTYUIOPLKJHGFDSAZXCVBNMOPQRSTUVWXYZ ' + bufferchars
  for char in ipts:
    if char not in chars or char in bufferchars:
      print('Character not supported: ' + char)
      while 1:
        pass
  for char in chars:
    cr[char] = chars[(chars.index(char) + 5) % (len(chars) - 1)]
  out = ""
  for char in ipts:
    out += cr[char]
  print(out)
  ipts = input("String to decode: ")
  out = ""
  for char in ipts:
    out += kofvalue(cr, char)
  print(out)
