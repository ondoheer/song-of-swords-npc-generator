# Song of Swords NPC Generator

This is a terminal based NPC generator for quickly developing characters for our campaigns.

_It is badly, tightly coupled written code._

## Characteristics

- It **only** creates new characters
- It **does not** imrpove characters with arc points
- It only generates **humans** and **dwarves** because that is all we use in out campaign
- It **does not** build characters that use firearms but can easily be configured to do so
- I have defined some basic **lifestyles** so the skill assignment makes sense. The skill packets weren't good enough to create full characters
- It won't buy extra boons if the Boons and Banes PCP value is negative or 0
- It **does not** select talents or superior maneuvers **YET**
- It chooses a campaign power randomly because **I want it this way** to simulate different character _levels_
- It **does not** choose equipment **YET**
- It allows you to add a background story to a generated character so you can use it as it is


### Example Character

```
 --------------------------------
        Character: dwarf - criminal
        Starting Power: awesome_fantasy
        Social Class: Minor Noble
        Background:
        Hirun was raised to become a dwarven military leader. His 
        father, a well positioned noble dwarf, invested a lot in his
        education. Hirun trained to use guerrilla tactics and learned
        everything about his people hsitory. Everything turned 180deg
        when he went into the world to face his first mission. His band
        performed badly, he was attacked, a hammer blow to his head
        deformed him and affected his eyesight. He was captured and
        became bitter and resented against his world. While being
        transported to be executed, he escaped (he was with a brigands
        band leader that was recued). He joined the brigands and
        decided to never tell his family that he is still alive. Now he
        is a key piece in this brigand band and leads the racketering
        efforts.

        --------------------------------
        ATTRIBUTES
        --------------------------------
        STR: 5 | AGI: 4 | END: 9 | HLT: 6
        WIL: 8 | WIT: 7 | PER: 4 | INT: 8
        ADR: 5 | MOB: 7 | CAR: 6 | CHA: 9
        TOU: 5 | SDB: 2 | GRIT: 4
        ---------------------------------
        COMBAT (Base CPs)
        ---------------------------------
        Melee CP: 14
        Misile CP: 9
        --------------------------------
        SCHOOLS
        ---------------------------------
        officer lvl:9 - talents:3 sup maneuvers:3
        - crossbow
        - 2-h-blunt
        - bow
        - dagger

        ---------------------------------
        BOONES
        ---------------------------------

        ---------------------------------
        BANES
        - facial-deformity-8
        - bad-eyes-6
        - barren-sterile-1

        ---------------------------------
        SKILLS
        ---------------------------------
        subterfuge: 2 (cha)
        intimidation: 6 (cha)
        gathering information: 4 (cha)
        observation: 3 (per)
        knowledge: 8 (int)
        climbing: 2 (end)
        navigation: 2 (per)
        stealth: 1 (agi)

        ---------------------------------
        MONEY
        ---------------------------------
        GP: 80
        SP: 0
        CP: 0
```


