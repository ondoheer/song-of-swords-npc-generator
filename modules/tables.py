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
            "amount": {
                "cp": 0,
                "sp": 10,
                "gp": 0
            }
        },
        2: {
            "name": "Peasant",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 5
            }
        },
        3: {
            "name": "Poor freeman",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 15
            }
        },
        4: {
            "name": "freeman",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 25
            }
        },
        5: {
            "name": "High freeman",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 40
            }
        },
        6: {
            "name": "Minor Noble",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 80
            }
        },
        7: {
            "name": "Landed Noble",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 150
            }
        },
        8: {
            "name": "High Noble",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 300
            }
        },
        9: {
            "name": "Royalty",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 800
            }
        },
        10: {
            "name": "High Royalty",
            "amount": {
                "cp": 0,
                "sp": 0,
                "gp": 1500
            }
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


# boones
boones_cost_full = {
    "allies-1": 1,
    "allies-5": 5,
    "allies-10": 10,
    "beautiful-3": 3,
    "beautiful-6": 6,
    "bloodthirsty": 3,
    "brave": 3,
    "berserker-8": 8,
    "berserker-12": 12,
    "contacts-1": 1,
    "contacts-4": 4,
    "contacts-6": 6,
    "contacts-8": 8,
    "direction-sense": 3,
    "estate": 10,
    "favor-1": 1,
    "favor-2": 2,
    "favor-3": 3,
    "famous-2": 2,
    "famous-3": 3,
    "famous-4": 4,
    "folks-back-home-3": 3,
    "folks-back-home-6": 6,
    "folks-back-home-8": 8,
    "follower": 5,
    "good-ears": 3,
    "good-eyes": 3,
    "good-nose": 3,
    "hale-hearty-2": 2,
    "hale-hearty-4": 4,
    "impressive-voice": 2,
    "known-for-virtue": 5,
    "languages-1": 1,
    "languages-2": 2,
    "languages-3": 3,
    "literate": 1,
    "natural-born-killer-6": 6,
    "natural-born-killer-12": 12,
    "natural-born-killer-18": 18,
    "natural-leader": 3,
    "rich-1": 1,
    "rich-3": 3,
    "rich-5": 5,
    "robust": 8,
    "tall-8": 8,
    "tall-12": 12,
    "true-grit-2": 2,
    "true-grit-4": 4,
    "true-grit-6": 6,
}

banes_cost_full = {
    "arrow-magnet": 3,
    "bad-ears-2": 2,
    "bad-ears-4": 4,
    "bad-eyes-4": 4,
    "bad-eyes-6": 6,
    "bad-reputation-3": 3,
    "bad-reputation-6": 6,
    "bad-reputation-9": 9,
    "barren-sterile-1": 1,
    "barren-sterile-3": 3,
    "bigoted": 5,
    "blind": 20,
    "braggart": 3,
    "brain-dmg-4": 4,
    "brain-dmg-8": 8,
    # "broken-limb": 0,
    "complete-monster": 10,
    "craven-4": 4,
    "craven-8": 8,
    "crippled-limb": 8,
    "debt-2": 2,
    "debt-4": 4,
    "debt-8": 8,
    # "dire-past": 0,
    "enemies-3": 3,
    "enemies-10": 10,
    "enemies-15": 15,
    "facial-deformity-2": 2,
    "facial-deformity-4": 4,
    "facial-deformity-8": 8,
    "fat": 5,
    "frail": 8,
    "hemophilia": 8,
    "hothead": 3,
    "honorable": 5,
    "lasting-pain-4": 4,
    "lasting-pain-8": 8,
    "mute-5": 5,
    "mute-8": 8,
    "oath-2": 2,
    "oath-3": 3,
    "oath-4": 4,
    "oath-5": 5,
    "oath-6": 6,
    "oath-7": 7,
    "oath-8": 8,
    "oath-9": 9,
    "oath-10": 10,
    "old-wound": 1,
    "one-eyed": 10,
    "poor-4": 4,
    "poor-6": 6,
    "poor-8": 8,
    "severed-limb-10": 10,
    "severed-limb-15": 15,
    "severed-limb-18": 18,
    "sheltered-2": 2,
    "sheltered-4": 4,
    "sheltered-6": 6,
    "short-8": 8,
    "short-15": 15,
    "skinny": 3,
    "tech-impaired": 5,
    "unhappily-married-1": 1,
    "unhappily-married-2": 2,
    "unhappily-married-3": 3,
    "virtuous": 5,
    "wanted-5": 5,
    "wanted-10": 10,
    "wanted-15": 15,
}

skill_pts_balancing_table = {
    # determines how mani extra skill points to
    # assing since they won't be buying packets
    # skill_pcp: extra points
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 4
}
skills = {
    1: "athletics",
    2: "chemistry",
    3: "climbing",
    4: "cooking",
    5: "crafting",
    6: "drill",
    7: "engineering",
    8: "gathering information",
    9: "history",
    10: "hunting",
    11: "intimidation",
    12: "knowledge",
    13: "navigation",
    14: "observation",
    15: "oration",
    16: "performance",
    17: "persuasion",
    18: "profession",
    19: "research",
    20: "riding",
    21: "sailing",
    22: "stealth",
    23: "strategy",
    24: "subterfuge",
    25: "surgery",
    26: "swimming",
    27: "tactics",
    28: "thievery"
}
lifestyles = {
    "academic": {
        "skills": {

            "basic": [2, 7, 12, 19, 9],
            "other": [3, 4, 5, 7, 8, 11, 13, 14, 15, 16, 17, 20, 25, 26]
        },
        "schools": []
    },
    "criminal": {
        "skills": {

            "basic": [8, 11, 12, 14, 24],
            "other": [1, 3, 10, 13, 20, 22, 28]
        },
        "schools": []
    },
    "civilian": {
        "skills": {

            "basic": [4, 5, 18, 20, 14],
            "other": [1, 3, 10, 12, 13, 26]
        },
        "schools": []
    },
    "military": {
        "skills": {

            "basic": [1, 6, 11, 13, 14, 20, 23, 27],
            "other": [3, 4, 5, 7, 8, 12, 16, 17, 21, 22, 24, 25, 26]
        },
        "schools": []
    },
    "outdoorsman": {
        "skills": {

            "basic": [1, 3, 4, 10, 13, 14, 20, 22],
            "other": [5, 21, 24, 26]
        },
        "schools": []
    },
    "noble": {
        "skills": {

            "basic": [9, 12, 15, 17, 20],
            "other": [1, 2, 3, 10, 11, 21, 26, 27]
        },
        "schools": []
    },
    "merchant": {
        "skills": {

            "basic": [8, 12, 17, 18, 20],
            "other": [1, 4, 5, 9]
        },
        "schools": []
    },
    "medic": {
        "skills": {

            "basic": [2, 12, 18, 19, 25, ],
            "other": [1, 4, 5, 8, 9, 14, 20]
        },
        "schools": []
    }
}

spp_schools = [
    {
        "name": "scraper",
        "cost": 0,
        "num_proficencies": 4
    },
    {
        "name": "soldier",
        "cost": 1,
        "num_proficencies": 10
    },
    {
        "name": "officer",
        "cost": 3,
        "num_proficencies": 4
    },
    {
        "name": "noble",
        "cost": 5,
        "num_proficencies": 3
    },
    {
        "name": "traditional-fencer",
        "cost": 5,
        "num_proficencies": 4
    },
    {
        "name": "unorthodox",
        "cost": 5,
        "num_proficencies": 6
    }
]

school_advancement = {
    1: 0,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 2,
    8: 2,
    9: 3,
    10: 3,
    11: 3,
    12: 3,
    13: 3,
    14: 6,
    15: 6,
    16: 6,
    17: 6,
    18: 8,
    19: 10,
    20: 10,
    21: 20
}
proficencies_all = [
    "dagger",
    "1-h-blades",
    "1-h-blunt",
    "2-h-blades",
    "2-h-blunt",
    "pugilism",
    "wrestling",
    "bow",
    "pistol",
    "crossbow",
    "polearms",
    "spear",
    "throwing"
]

proficencies_no_gun = [
    "dagger",
    "1-h-blades",
    "1-h-blunt",
    "2-h-blades",
    "2-h-blunt",
    "pugilism",
    "wrestling",
    "bow",
    "crossbow",
    "polearms",
    "spear",
    "throwing"
]
