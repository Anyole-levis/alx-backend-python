def paginate_users(page_size, offset):
    """
    Fetches a page of users using SELECT * with LIMIT and OFFSET.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()

    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Lazily yields pages of users from the database using one loop.
    Each page is fetched only when needed.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            return  # No more records
        yield page
        offset += page_size

        
