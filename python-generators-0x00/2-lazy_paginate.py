def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database based on the given page_size and offset.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    
    query = """
    SELECT user_id, name, email, age
    FROM user_data
    LIMIT %s OFFSET %s
    """
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator that lazily paginates users from the database using the given page_size.
    It fetches a new page only when needed and yields each page.
    """
    offset = 0

    while True:
        page = paginate_users(page_size, offset)
        if not page:
            return  # No more data to yield, stop iteration
        yield page
        offset += page_size
