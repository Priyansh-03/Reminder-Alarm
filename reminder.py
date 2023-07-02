import winsound
from win10toast import ToastNotifier

def timer(reminder,second):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"Alarm will Buzz in {second} Seconds,",duration=0)
    notificator.show_toast(f"Reminder",reminder,duration=0)

    try:
        # Alarm
        frequency = 2500
        duration = 3000
        winsound.Beep(frequency, duration)
    except Exception as e:
        print("An error occurred while playing the sound:", str(e))

if __name__=="__main__":
    words=input("PC: What is your reminder?\nYOU: ")
    sec=int(input("PC: Enter seconds:\nYOU: "))
    timer(words,sec)
