import datetime

def display_current_datetime():

     date = datetime.datetime.now()
     return date

current_date = display_current_datetime()
print("Current date and time:",current_date)

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
      date = current_date + datetime.timedelta(days=number_of_days)
      return date
    
future_date = calculate_future_date()
print("\n Future date:", future_date)