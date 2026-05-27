
bananas = 0 #Initial value


while bananas <= 6:
    
    if bananas >= 5:
        print(f"{bananas}: I have a bunch of bananas.")
    elif 1 <= bananas <= 4:
        print(f"{bananas}: I have a small bunch of bananas.")
    else:
        print(f"{bananas}: I have no bananas.")

    # Increase bananas each loop
    bananas += 1
