"""All app configurations."""

# Web settings.
WEB_NAME = "Names Creator"
ICON = "🎰"
LAYOUT = "wide"

LIGHT_THEME_CSS = """<style>
                    :root {color - scheme: light;}
                    </style>
                    """

NO_BORDERS_CSS = """<style>
                        [data-testid="stForm"] {border: 0px}
                    </style>
                    """

HIDE_MENU_CSS = """<style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                     </style>
                     """
