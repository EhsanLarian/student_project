# main.py

from Student.grades import calculate_avg, calculate_max, calculate_min
from Student.status import get_status

def main():
    # 1. Get student name
    name = input("Enter student name: ")

    # 2. Get the number of grades and the grades themselves
    grades_list = []
    try:
        count = int(input("How many grades do you want to enter? "))
        for i in range(count):
            score = float(input(f"Enter grade {i+1}: "))
            grades_list.append(score)
    except ValueError:
        print("Please enter valid numbers!")
        return

    # 3. Call calculation functions
    avg = calculate_avg(grades_list)
    max_grade = calculate_max(grades_list)
    min_grade = calculate_min(grades_list)
    
    # Call status function
    status = get_status(avg)

    # 4. Print the output matching the whiteboard image
    print(f"\nstudent: {name}")
    print(f"Avg = {avg}")
    print(f"max = {max_grade}")
    print(f"min = {min_grade}")  
    print(f"status = {status}")

if __name__ == "__main__":
    main()