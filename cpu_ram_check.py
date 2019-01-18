import commands,time

print("Plz wait we r working hard to get RAM and CPU info")
time.sleep(2)
ram = commands.getoutput('free -m')
final_memory = ram.split()[7]
print("My system RAM is "+final_memory+"MB")
execfile('menu.py')