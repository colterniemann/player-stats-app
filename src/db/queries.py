class PlayerQuery:
    def __init__(self, conn):
        self.conn = conn
        self.position = None
        self.attributes = []
        self.stat_filter = ""
        self.player_name = ""
        self.start_year = None
        self.end_year = None
        self.stat = ""

    def get_positions(self):
        return ["Quarterback", "Receiver", "Runningback", "Defensive Player"]
    
    def set_position(self, position):
        self.position = position
   
    def get_attributes(self):
        attributes = {
            "Quarterback": ["player_id","name","year","team","games_played","passes_attempted","passes_completed","completion_percentage","PA_per_game","passing_yards","yards_per_attempt","yards_per_game","touchdown_passes","interceptions","interception_rate","longest_pass","sacks","sacked_yards_lost","passer_rating"],
            "Receiver": ["player_id","name","year","team","games_played","receptions","receiving_yards","yards_per_reception","yards_per_game","longest_reception","touchdowns","receptions_over_20","receptions_over_40","first_downs","fumbles"],
            "Runningback": ["player_id","name","year","team","games_played","rush_attempts","attempts_per_game","rush_yards","yards_per_carry","yards_per_game","touchdowns","longest_run","first_downs","percentage_first_downs","runs_over_20","runs_over_40","fumbles"],
            "Defensive Player": ["player_id","name","year","team","games_played","total_tackles","solo_tackles","assisted_tackles","sacks","safeties","passes_defended","interceptions","pick_six","int_yards"],
        }
        return attributes.get(self.position, [])
    
    def set_attributes(self, selected_attributes):
        self.attributes = [
            attribute.replace("name", "first_name || ' ' || last_name AS name")
            for attribute in selected_attributes
        ]

    def set_stat_filter(self, stat_filter):
        self.stat_filter = stat_filter
    
    def set_player_name(self, plyr_name):
        self.player_name = plyr_name

    def set_year_range(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
    
    def set_stat(self, stat):
        self.stat = stat
    
    def get_table_name(self):
        table_map = {
            "Quarterback": "Career_Stats_Passing",
            "Receiver": "Career_Stats_Receiving",
            "Runningback": "Career_Stats_Rushing",
            "Defensive Player": "Career_Stats_Defensive",
        }
        return table_map.get(self.position)
    
    def execute_query(self, query, params):
        try:
            with self.conn.cursor() as cur:
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)
                results = cur.fetchall()
                return results
        except Exception as e:
            print(f"Query error: {e}")
            return []
    
    def search_by_stat_filter(self):
        table_name = self.get_table_name()
        print(table_name)
        query = f"""
        SELECT {','.join(self.attributes)} FROM {table_name} WHERE {self.stat_filter}
        ORDER BY name, year;
        """
        params = []
        return self.execute_query(query, params)
        

        
    def search_player_by_name_and_year(self):
        table_name = self.get_table_name()
        print(table_name)
        if self.end_year:
            query = f"""
            SELECT * FROM {table_name} 
            WHERE (TRIM(first_name) || ' ' || last_name) ILIKE %s
            AND year BETWEEN %s AND %s
            ORDER BY year;
            """
            params = (f"%{self.player_name}%", self.start_year, self.end_year)
        else:
            query = f"""
            SELECT * FROM {table_name}
            WHERE (first_name || ' ' || last_name) ILIKE %s
            AND year = %s
            """
            params = (f"%{self.player_name}%", self.start_year)
        return self.execute_query(query, params)
        
    def get_top_players(self, top_n):
        table_name = self.get_table_name()

        query = f"""
        SELECT {','.join(self.attributes)}
        FROM {table_name}
        ORDER BY {self.stat} DESC NULLS LAST
        LIMIT %s;
        """
        params = (top_n,)
        return self.execute_query(query, params)
            