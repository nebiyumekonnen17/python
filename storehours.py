
open_hour = 9    # 9 AM
close_hour = 18  # 6 PM

current_hour = 14  # Example: 2 PM

if current_hour < open_hour:
    print("The store is CLOSED (too early)")
elif open_hour <= current_hour < close_hour:
    print("The store is OPEN")
elif current_hour >= close_hour:
    print("The store is CLOSED (too late)")
