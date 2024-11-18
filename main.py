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
        print("Invlid date/time format. Please use YYYY-MM-DD HH:MM) \n")


add_reminder()