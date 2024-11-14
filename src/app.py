from db.connection import connect
from db.queries import get_attributes, filter_query
from utils.menu import select_position, select_attributes, get_stat_filter


def main():
    conn = connect()
    if not conn:
        print("Failed to connect to the database. Exiting.")
        return

    position = select_position()
    attributes = get_attributes(position)
    selected_attributes = select_attributes(attributes)
    stat_filter = get_stat_filter()
    results = filter_query(conn, position, selected_attributes, stat_filter)


    if results:
        print("\nQuery Results:")
        for row in results:
            print(row)
    else:
        print("No results found.")

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
