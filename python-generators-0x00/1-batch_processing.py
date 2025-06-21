def stream_users_in_batches(batch_size):
    """Yields batches of user records from the 'user_data' table."""
    connection = connect_to_prodev()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT user_id, name, email, age FROM user_data")

        batch = []
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch

    finally:
        cursor.close()
        connection.close()
        return  # graceful exit


def batch_processing(batch_size):
    """Processes batches to yield users older than 25."""
    try:
        for batch in stream_users_in_batches(batch_size):
            filtered_users = [user for user in batch if float(user[3]) > 25]
            yield filtered_users
    finally:
        return  # graceful exit

