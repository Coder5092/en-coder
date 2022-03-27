def kofvalue(dic, value):
  for k in dic:
    if dic[k] == value:
      return k
def decode(ipts):
  out = ""
  for char in ipts:
    out += kofvalue(cr, char)
  print(out)
