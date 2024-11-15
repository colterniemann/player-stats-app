from db.connection import DatabaseConnection
from db.queries import PlayerQuery
from utils.menu import Menu


class PlayerStatsApp:
    def __init__(self):
        self.db = DatabaseConnection()
        self.menu = Menu()
        self.query = None
    
    def run(self):
        self.db.connect()
        conn = self.db.get_connection()
        if conn is None or conn.closed:
            print("Failed to connect to the database. Exiting")
            return
        
        self.query = PlayerQuery(conn)
        try:
            while True:
                choice = self.menu.display_main_menu()

                if choice == 1:
                    self.handle_stat_filter_search()
                elif choice == 2:
                    self.handle_player_search_by_name_and_year()
                elif choice == 3:
                    self.handle_top_players_search()
                elif choice == 4:
                    print("Exiting the application.")
                    break
                else:
                    print ("Invalid choice. Please try again.")
        finally:
            self.db.close()

    def handle_stat_filter_search(self):
        position = self.menu.select_position()
        self.query.set_position(position)

        attributes = self.query.get_attributes()
        selected_attributes = self.menu.select_attributes(attributes)
        self.query.set_attributes(selected_attributes)

        stat_filter = self.menu.get_stat_filter()
        self.query.set_stat_filter(stat_filter)

        results = self.query.search_by_stat_filter()
        self.display_results(selected_attributes, results)
    
    def handle_player_search_by_name_and_year(self):
        position = self.menu.select_position()
        self.query.set_position(position)
        name, start_year, end_year = self.menu.get_player_name_and_year()
        self.query.set_player_name(name)
        self.query.set_year_range(start_year, end_year)
        
        attributes = self.query.get_attributes()
        '''
        selected_attributes = self.menu.select_attributes(attributes)
        self.query.set_attributes(selected_attributes)
        '''

        results = self.query.search_player_by_name_and_year()
        self.display_results(attributes, results)

    def handle_top_players_search(self):
        position, stat, top_n = self.menu.get_top_players_query()
        self.query.set_position(position)
        self.query.set_stat(stat)

        self.query.set_attributes(['name', 'year', 'team', self.query.stat])

        results = self.query.get_top_players(top_n)
        self.display_results(['name', 'year', 'team', stat], results)

    def display_results(self, headers, results):
        if results:
            print("\n Query Results:")
            print(tuple(headers))
            for row in results:
                print(row)
        else:
            print ("No results found.")




if __name__ == "__main__":
    app = PlayerStatsApp()
    app.run()