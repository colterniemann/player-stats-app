class Menu:
    def __init__(self):
        self.positions = "Quarterback", "Receiver", "Runningback", "Defensive Player"  
        self.main_options = [
            "Search attributes by a stat filter",
            "Search for a player's stats by name and year",
            "Find top players in a specific stat",
            "Exit"
        ]  
    def select_position(self):
        print("Select a position:")
        for i, position in enumerate(self.positions, 1):
            print(f"{i}. {position}")
        
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(self.positions):
            return self.positions[int(choice) - 1]
        else:
            print("Invalid choice. Please try again.")
            return self.select_position()

    def select_attributes(self, attributes):
        print("Select attributes to view (comma-separated list):")
        for i, attr in enumerate(attributes, 1):
            print(f"{i}. {attr}")
        
        choices = input("Enter the numbers of the attributes: ").strip().split(',')
        selected_attrs = [attributes[int(choice) - 1] for choice in choices if choice.isdigit() and 1 <= int(choice) <= len(attributes)]
        return selected_attrs

    def get_stat_filter(self):
        return input("Enter a filter condition (e.g., 'receiving_yards > 600'): ").strip()
    
    def get_player_name_and_year(self):
        name = input("Enter the player's name (e.g., 'Peyton Manning'): ").strip()
        start_year = input("Enter the first year you would like to see stats for (e.g., '2010'): ").strip()
        end_year = input("Enter the last year you would like to see stats for (or leave blank for a single year): ").strip()
        return name, start_year, end_year
    
    def get_top_players_query(self):
        position = self.select_position()
        stat = input("Enter the stat to rank by (e.g., 'passing_yards'): ").strip()
        top_n = input("Enter the number of top players to retrieve (e.g., 3): ").strip()

        if top_n.isdigit():
            return position, stat, int(top_n)
        else:
            print("Invalid input for number of players. Please try again.")
            return self.get_top_players_query()
    
    def display_main_menu(self):
        print("\nMain Menu:")
        for i, option in enumerate(self.main_options, 1):
            print(f"{i}. {option}")

        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(self.main_options):
            return int(choice)
        else:
            print("Invalid choice. Please try again.")
            return self.display_main_menu()