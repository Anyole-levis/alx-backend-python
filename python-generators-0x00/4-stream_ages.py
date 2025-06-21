def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    
    cursor.execute("SELECT age FROM user_data")
    
    for (age,) in cursor:
        yield float(age)  # ensure it's numeric

    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Calculates and prints the average age using the age generator.
    Does not load the entire dataset into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():  # First and only loop
        total_age += age
        count += 1

    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found in the database.")


# Run the function
if __name__ == "__main__":
    calculate_average_age()

