import subprocess
proc = subprocess.Popen(['python3','productList.py'],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if line != b'':
    #the real code does filtering here
    print("test:",line.rstrip())
  else:
    break
