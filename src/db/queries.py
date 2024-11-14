def get_positions():
    return ["Quarterback", "Receiver", "Runningback", "Defense"]

def get_attributes(position)
    """Return attributes based on player position."""
    attributes = {
        "Quarterback": ["player_id", "name", "team", "passing_yards", "touchdowns"],
        "Receiver": ["player_id", "name", "team", "receiving_yards", "receptions", "touchdowns"],
        "Runningback": ["player_id", "name", "team", "rushing_yards", "touchdowns"],
        "Defense": ["player_id", "name", "team", "tackles", "sacks", "interceptions"],
    }
    return attributes.get(position, [])

def filter_query(conn, position, attributes, stat_filter):
    """Build and execute a query based on user input."""
    table_map = {
        "Quarterback": "career_stats_passing",
        "Receiver": "career_stats_receiving",
        "Runningback": "career_stats_rushing",
        "Defensive Player": "career_stats_defensive",
    }

    table_name = table_map.get(position)
    if not table_name:
        print("Invalid position.")
        return []

    query = f"SELECT {', '.join(attributes)} FROM {table_name} WHERE {stat_filter};"
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            return results
    except Exception as e:
        print(f"Query error: {e}")
        return []