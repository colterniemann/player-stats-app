def select_position():
    """Prompt user to select a position."""
    positions = ["Quarterback", "Receiver", "Runningback", "Defensive Player"]
    print("Select a position:")
    for i, position in enumerate(positions, 1):
        print(f"{i}. {position}")
    
    choice = input("Enter the number of your choice: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(positions):
        return positions[int(choice) - 1]
    else:
        print("Invalid choice. Please try again.")
        return select_position()

def select_attributes(attributes):
    """Prompt user to select attributes to view."""
    print("Select attributes to view (comma-separated list):")
    for i, attr in enumerate(attributes, 1):
        print(f"{i}. {attr}")
    
    choices = input("Enter the numbers of the attributes: ").strip().split(',')
    selected_attrs = [attributes[int(choice) - 1] for choice in choices if choice.isdigit() and 1 <= int(choice) <= len(attributes)]
    return selected_attrs

def get_stat_filter():
    """Prompt user for a filter condition."""
    return input("Enter a filter condition (e.g., 'receiving_yards > 600'): ").strip()
