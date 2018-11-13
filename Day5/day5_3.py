import webbrowser
import time

user = False
alarm_number = int(input("How many alarms would you like to set?: "))
alarm_freq = int(input("How frequently would you like the alarm to sound?: "))
link = input("Please insert your preferred YouTube video: ")
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
#https://www.youtube.com/watch?v=sFYo2-KUeTA

totalplays = 0

while totalplays < alarm_number:
    totalplays += 1
    webbrowser.open_new_tab(link)
    print("Playing alarm " + str(totalplays) + " of " + str(alarm_number))
    time.sleep(alarm_freq)
    user = False
print("Thank you for using the program!")