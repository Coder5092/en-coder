from both import doall
while 1:
  try:
    doall()
  except KeyboardInterrupt:
    exit('\nKeyboardInterrupt quit')
