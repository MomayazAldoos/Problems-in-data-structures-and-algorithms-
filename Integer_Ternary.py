def convert_into_ternary(A):
    if A == 0:
        ordered_ternary = [0]
        return ordered_ternary
    
    # Initialize temp as the input number, and reminders as an empty array
    temp = A
    reminders = []

    while temp > 0:
        reminder_of_number_divided = temp % 3
        reminders.append(reminder_of_number_divided)
        temp = temp // 3 

    temp_size = len(reminders)
    # initialize the non-dynamic array 
    ordered_ternary = [0]* temp_size

    # reserve the reminders into the final array 
    for i in range(temp_size):
        ordered_ternary[i] = reminders[temp_size-1-i]
    return ordered_ternary

A = 34 
print(convert_into_ternary(A))
