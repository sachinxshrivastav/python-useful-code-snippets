import time

a = 0
for i in range(101):
  text = "progress: " + str(i) + "%"
  print ("\r" + text + "        ", end='')
  time.sleep (0.1)
  i = i + 1