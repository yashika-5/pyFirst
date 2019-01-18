import webbrowser,time
import commands





option = '''
Press 1 to check your OS version:
Press 2 to login fb account:
Press 3 to check RAM and cpu in your current machine:
Press 4 to search something in google search en2gine:
Press 5 to list out all IP and MAC address in your current zone:

'''
print(option)
choice = input()

print("u have entered :", choice)
if int(choice) == 1:
        print("My Os is RHEL")

elif int(choice) == 4:
            data = input("type something to search on google :")
            webbrowser.open_new_tab('https://www.google.com/search?q ='+data)

            
elif int(choice) == 3:
       execfile('cpu_ram_check.py')
                    

else:
        print("No input is given")
        print("closing program")
        exit()
