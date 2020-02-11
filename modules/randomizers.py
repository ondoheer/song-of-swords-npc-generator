from random import choice
from modules.tables import campaign_power 

def power_randomizer():
    """
    Returns a random campaign power"
    """
    c = choice(list(campaign_power.keys()))
    return c

