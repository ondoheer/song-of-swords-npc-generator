# Determines the basic pcp points to use in the pcp_investment
campaign_power = {
    "low": {
        "pcp": 14,
        "max": 5
    },
    "medium": {
        "pcp": 18,
        "max": 6
    },
    "high_fantasy": {
        "pcp": 22,
        "max": 7
    },
    "epic_fantasy": {
        "pcp": 26,
        "max": 8
    },
    "awesome_fantasy": {
        "pcp": 30,
        "max": 10
    }
}

races_table = {
    "human": 1,
    "dwarf": 2
}
# determines the costs to use on each development area at caracter creation
pcp_investment = {
    "race_tier": {
        1: 1,
        2: 2,
        4: 3,
        6: 4,
        8: 5
    },
    "attribute": {
        1: 22,
        2: 23,
        3: 24,
        4: 27,
        5: 31,
        6: 35,
        7: 40,
        8: 45,
        9: 50,
        10: 56
    },
    "skill": {
        1: 6,
        2: 9,
        3: 12,
        4: 15,
        5: 18,
        6: 21,
        7: 24,
        8: 27,
        9: 30,
        10: 33
    },
    "spp": {  # schools and proficency points
        1: 0,
        2: 3,
        3: 6,
        4: 9,
        5: 12,
        6: 15,
        7: 18,
        8: 21,
        9: 24,
        10: 27
    },
    "wealth": {  # social class and wealth
        1: {
            "name": "Slave/Exile",
            "amount": "10sp"
        },
        2: {
            "name": "Peasant",
            "amount": "5gp"
        },
        3: {
            "name": "Poor freeman",
            "amount": "15gp"
        },
        4: {
            "name": "freeman",
            "amount": "25gp"
        },
        5: {
            "name": "High freeman",
            "amount": "40gp"
        },
        6: {
            "name": "Minor Noble",
            "amount": "80gp"
        },
        7: {
            "name": "Landed Noble",
            "amount": "150gp"
        },
        8: {
            "name": "High Noble",
            "amount": "300gp"
        },
        9: {
            "name": "Royalty",
            "amount": "800gp"
        },
        10: {
            "name": "High Royalty",
            "amount": "1500gp"
        },
    },
    "boones_banes": {
        1: -15,
        2: -10,
        3: -5,
        4: 0,
        5: 5,
        6: 10,
        7: 15,
        8: 20,
        9: 25,
        10: 30
    }
}

# Cost of attribute advancing
attribute_costs = {
    #  cost: value
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    10: 10,
    12: 11,
    14: 12,
    16: 13
}
