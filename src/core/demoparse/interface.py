import core.demoparse.parser_impl

class DemoParser:
    """
    Parser for CSGO demo files.
    Provides methods to extract players, events, stats, and more.
    """

    def __init__(self, file_path):
        ...

    def load_demo(self, file_path):
        ...

    def get_players(self):
        ...

    def get_teams(self):
        ...

    def get_rounds(self):
        ...

    def get_game_state(self, timestamp):
        ...

    def get_timeline(self):
        ...

    def get_events(self, event_type=None):
        ...

    def get_key_events(self):
        ...

    def get_player_stats(self, player_id):
        ...

    def get_team_stats(self, team_id):
        ...

    def export_json(self):
        ...

    def close(self):
        ...
