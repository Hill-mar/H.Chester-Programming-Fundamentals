# Author: Hilmar Chester
# Date: November 6, 2026
# Description: Records workouts until the user types done and summarizes the session.
# Tier: Base and Intermediate Level
#
# BASE Level test outputs:
# --------------------------------------
# WORKOUT 1 SUMMARY
# --------------------------------------
# Workout name:  Walking (Low Intensity)
# Duration:      45 minutes
# Calories:      180 calories
# Calorie rate:  4.0 cal/min
# Intensity:     Low
# --------------------------------------
#
# --------------------------------------
# WORKOUT 2 SUMMARY
# --------------------------------------
# Workout name:  Running (Moderate Intensity)
# Duration:      40 minutes
# Calories:      300 calories
# Calorie rate:  7.5 cal/min
# Intensity:     Moderate
# --------------------------------------
#
# --------------------------------------
# WORKOUT 3 SUMMARY
# --------------------------------------
# Workout name:  Cycling (High Intensity)
# Duration:      30 minutes
# Calories:      320 calories
# Calorie rate:  10.7 cal/min
# Intensity:     High
# --------------------------------------


# INTERMEDIATE test outputs:
# --------------------------------------
# WORKOUT 1 SUMMARY
# --------------------------------------
# Workout name:  Yoga
# Duration:      45 minutes
# Calories:      180 calories
# Calorie rate:  4.0 cal/min
# Intensity:     Low
# --------------------------------------

# Please enter another workout name or type 'done': done

# ==========================================
# SESSION SUMMARY
# ==========================================
# Workouts logged:       1
# Total calories burned: 180 calories
# Average calories:      180.0 per workout
# Average duration:      45.0 minutes
# Best workout:          Yoga
# ==========================================
# Thanks for using the tracker. Great job staying active!

#3 WORKOUTS TEST OUTPUTS:
# --------------------------------------
# WORKOUT 1 SUMMARY
# --------------------------------------
# Workout name:  Walking
# Duration:      30 minutes
# Calories:      150 calories
# Calorie rate:  5.0 cal/min
# Intensity:     Moderate
# --------------------------------------

# --------------------------------------
# WORKOUT 2 SUMMARY
# --------------------------------------
# Workout name:  Running
# Duration:      40 minutes
# Calories:      350 calories
# Calorie rate:  8.8 cal/min
# Intensity:     Moderate
# --------------------------------------

# --------------------------------------
# WORKOUT 3 SUMMARY
# --------------------------------------
# Workout name:  Yoga
# Duration:      45 minutes
# Calories:      180 calories
# Calorie rate:  4.0 cal/min
# Intensity:     Low
# --------------------------------------

# Please enter another workout name or type 'done': done

# ==========================================
# SESSION SUMMARY
# ==========================================
# Workouts logged:       3
# Total calories burned: 680 calories
# Average calories:      226.7 per workout
# Average duration:      38.3 minutes
# Best workout:          Running
# ==========================================


# 2 WORKOUTS TEST(TIE) OUTPUTS:
# --------------------------------------
# WORKOUT 1 SUMMARY
# --------------------------------------
# Workout name:  Spinning
# Duration:      40 minutes
# Calories:      300 calories
# Calorie rate:  7.5 cal/min
# Intensity:     Moderate
# --------------------------------------

# --------------------------------------
# WORKOUT 2 SUMMARY
# --------------------------------------
# Workout name:  Dancing
# Duration:      30 minutes
# Calories:      300 calories
# Calorie rate:  10.0 cal/min
# Intensity:     High
# --------------------------------------

# Please enter another workout name or type 'done': done

# ==========================================
# SESSION SUMMARY
# ==========================================
# Workouts logged:       2
# Total calories burned: 600 calories
# Average calories:      300.0 per workout
# Average duration:      35.0 minutes
# Best workout:          Spinning
# ==========================================

#FUNCTIONS

# Calculate the calorie burn rate and return it rounded to one decimal place.
def calories_per_minute(calories, duration):
    rate = calories / duration
    return round(rate, 1)


# Return an intensity label based on the calorie burn rate.
def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate < 10.0:
        return "Moderate"
    else:
        return "High"


# Add the numbers in a list using an accumulator and a for loop.
def calculate_total(values):
    total = 0
    for value in values:
        total = total + value
    return total


# Calculate an average by calling calculate_total().
def calculate_average(values):
    total = calculate_total(values)
    average = total / len(values)
    return round(average, 1)


# Return the name of the workout with the most calories burned.
# When workouts tie, the first one logged remains the best workout.
def find_best_workout(names, calories_list):
    best_workout = names[0]
    highest_calories = calories_list[0]

    for index in range(1, len(calories_list)):
        if calories_list[index] > highest_calories:
            highest_calories = calories_list[index]
            best_workout = names[index]

    return best_workout


# Print a clear report for one workout.
def display_workout_summary(workout_number, name, duration, calories, rate, intensity):
    print("\n" + "-" * 38)
    print(f"WORKOUT {workout_number} SUMMARY")
    print("-" * 38)
    print(f"Workout name:  {name}")
    print(f"Duration:      {duration} minutes")
    print(f"Calories:      {calories} calories")
    print(f"Calorie rate:  {rate:.1f} cal/min")
    print(f"Intensity:     {intensity}")
    print("-" * 38)


# Calculate and print the summary for the whole session.
def display_session_summary(names, durations, calories_list):
    total_calories = calculate_total(calories_list)
    average_calories = calculate_average(calories_list)
    average_duration = calculate_average(durations)
    best_workout = find_best_workout(names, calories_list)

    print("\n" + "=" * 42)
    print("SESSION SUMMARY")
    print("=" * 42)
    print(f"Workouts logged:       {len(names)}")
    print(f"Total calories burned: {total_calories} calories")
    print(f"Average calories:      {average_calories} per workout")
    print(f"Average duration:      {average_duration} minutes")
    print(f"Best workout:          {best_workout}")
    print("=" * 42)


# Welcome the user and explain how to finish entering workouts.
print("Hey there! Welcome to the Personal Fitness Tracker.")
print("Enter your workouts one at a time. Type 'done' when you are finished.")

# Keep each type of workout information in its own parallel list.
workout_names = []
durations = []
calories_list = []

# Ask for workout names until the user enters done.
workout_name = input("\nPlease enter a workout name or type 'done': ").strip()
while workout_name == "":
    print("The workout name cannot be blank. Please enter a name or type 'done'.")
    workout_name = input("Please enter a workout name or type 'done': ").strip()

workout_number = 1

while workout_name.lower() != "done":
    print(f"Please enter the details for Workout {workout_number}.")

    # Keep asking until the duration is a whole number from 1 to 60.
    while True:
        try:
            duration = int(input("Please enter the duration in minutes: "))
        except ValueError:
            print("Please enter a whole number from 1 to 60.")
        else:
            if duration >= 1 and duration <= 60:
                break
            else:
                print("Duration must be from 1 to 60 minutes.")

    # Keep asking until calories are a whole number that is zero or greater.
    while True:
        try:
            calories_burned = int(input("Please enter the total calories burned: "))
        except ValueError:
            print("Please enter calories as a whole number.")
        else:
            if calories_burned >= 0:
                break
            else:
                print("Calories burned cannot be negative.")

    # Add the workout details to their matching lists.
    workout_name = workout_name.title()
    workout_names.append(workout_name)
    durations.append(duration)
    calories_list.append(calories_burned)

    # Calculate and display this workout's rate and intensity.
    rate = calories_per_minute(calories_burned, duration)
    intensity = get_intensity(rate)

    display_workout_summary(
        workout_number,
        workout_name,
        duration,
        calories_burned,
        rate,
        intensity
    )

    workout_number = workout_number + 1
    workout_name = input("\nPlease enter another workout name or type 'done': ").strip()
    while workout_name == "":
        print("The workout name cannot be blank. Please enter a name or type 'done'.")
        workout_name = input("Please enter another workout name or type 'done': ").strip()

# Show a message for an empty session, or display the workout summary.
if len(workout_names) == 0:
    print("\nNo workouts were logged.")
else:
    display_session_summary(workout_names, durations, calories_list)

# Display a closing message after the workout session ends.
print("Thanks for using the tracker. Great job staying active!")
