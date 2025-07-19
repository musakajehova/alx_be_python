# 4. Personal Daily Reminder

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("'",task, "'" , "is a high priority task that requires immediate attention today!")
        else:
            print("'",task, "'" , "is a high priority task that requires your attention as soon as you are avaliable")
    case "meduim":
        if time_bound == "yes":
            print("'",task, "'" , "is a medium priority task that requires your attention today!")
        else:
            print("'",task, "'" , "is a medium priority task that is required to be completed sometime during the day")
    case "low":
        if time_bound == "yes":
            print("'",task, "'" , "is a low priority task that requires your timely attention after tending to pressing matters!")
        else:
            print("'",task, "'" , "is a low priority task. Consider completing it when you have free time.")
