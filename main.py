import time
from datetime import datetime

reminders = {}

def add_reminder():
    task = input("Enter the task you want to be reminded of: ").strip()
    date_time = input("Enter the date and timefor the reminder (YYYY-MM-DD HH:MM): ").strip()
    try:
        reminder_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        reminders[reminder_time] = task
        print(f"Reminder added: {task} at {reminder_time}. \n")
    except ValueError:
        print("Invalid date/time format. Please use YYYY-MM-DD HH:MM) \n")

def view_reminders():
    if reminders:
        print("\nScheduled Reminders:")
        for time, task in sorted(reminders.items()):
            print(f"- {task} at {time}")
    else:
        print("\nNo reminders set.")

def check_reminders():
    while True:
        now = datetime.now()
        to_remove = []
        for reminder_time, task in reminders.items():
            if reminder_time <= now:
                print(f'\n Reminder: {task} is due now!')
                to_remove.append(reminder_time)
        for time_to_remove in to_remove:
            del reminders[time_to_remove]
        time.sleep(60)

def main():
    print(" Welcome to your Reminder Assistant!")
    while True:
        print("\nChoose aan option:")
        print("1: Add a new Reminder")
        print("2: View all Reminders")
        print("3: Start checking for Reminders")
        print("4: Exit")

        choice = input("Enter your choice (1/2/3/4)")

        if choice == '1':
            add_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            print("Checking for reminders...")
            check_reminders()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Enter 1/2/3/4")

if __name__ == "__main__":
    main()