import random
from modules.tables import campaign_power, races_table, pcp_investment, attribute_costs, boones_cost_full, banes_cost_full, lifestyles, skills, skill_pts_balancing_table, spp_schools, proficencies_no_gun, school_advancement, school_talents, school_sup_maneuvers
from modules.config import MILITARY_LIFESTYLES, NON_MILITARY_LIFESTYLES

class Character():

    _str = 1
    _agi = 1
    _end = 1
    _hlt = 1
    _wil = 1
    _wit = 1
    _per = 1
    _int = 1
    _str_mod = 0
    _agi_mod = 0
    _end_mod = 0
    _hlt_mod = 0
    _wil_mod = 0
    _wit_mod = 0
    _per_mod = 0
    _int_mod = 0
    _tou_mod = 0
    _grit_mod = 0
    _adr_mod = 0
    _cha_mod = 0
    _mob_mod = 0
    _sdb_mod = 0
    _car_mod = 0

    def __init__(self, race="human", lifestyle=None):
        self.race = race

        # character creation PCP
        self.power = None
        self.pcp = None
        self.max = None
        self.race_pcp = 0
        self.attributes_pcp = 0
        # attribute points to spend
        self.attributes_points = 0
        self.skill_pcp = 0
        self.spp_pcp = 0
        self.wealth_pcp = 0
        self.boones_banes_pcp = 0
        # boones n banes points to spend
        self.boones_banes_points = 0
        self.basic_boones_banes_pts = 0
        self.boones = []
        self.banes = []
        # skills
        self.skill_points = 0
        self.skills = {}
        # wealth
        self.social_status = None
        self.money = {}
        # SPP
        self.spp_points = 0
        self.school = None # now it only supports 1 school
        self.proficencies = []

        # set lifestyle
        if not lifestyle:
            self.lifestyle = random.choice(list(lifestyles.keys()))
        else:
            self.lifestyle = lifestyle

        

    def __str__(self):

        return f"""
        -- RACIAL
        Race: {self.race}
        -- LIFESTYLE
        Lifestyle: {self.lifestyle}
        -- ATRIBUTES
        STR: {self.str} = {self._str} + {self._str_mod}
        AGI: {self.agi} = {self._agi} + {self._agi_mod}
        END: {self.end} = {self._end} + {self._end_mod}
        HLT: {self.hlt} = {self._hlt} + {self._hlt_mod}
        WIL: {self.wil} = {self._wil} + {self._wil_mod}
        WIT: {self.wit} = {self._wit} + {self._wit_mod}
        PER: {self.per} = {self._per} + {self._per_mod}
        INT: {self.int} = {self._int} + {self._int_mod}
        AVALIABLE ATTR PCP: {self.avaliable_attr_pts}
        -- COMPOUND
        ADR: {self.adr} mod =  {self._adr_mod}
        MOB: {self.mob} mod =   {self._mob_mod}
        CAR: {self.car} mod =   {self._car_mod}
        CHA: {self.cha} mod =   {self._cha_mod}
        TOU: {self.tou} mod =   {self._tou_mod}
        SDB: {self.sdb} mod =   {self._sdb_mod}
        GRIT: {self.grit} mod =  {self._grit_mod}
        -- CAMPAIGN POWER
        Power: {self.power}
        PCP: {self.pcp}
        UNSPEND PCP: {self.avaliable_pcp}
        Max values: {self.max}
        spend race: {self.race_pcp}
        spend attributes: {self.attributes_pcp}
        spend boones banes: {self.boones_banes_pcp}
        spend skills: {self.skill_pcp}
        spend spp: {self.spp_pcp}
        spend wealth: {self.wealth_pcp}
        -- BOONES AND BANES
        PCP: {self.boones_banes_pcp}
        BASIC PTS: {self.basic_boones_banes_pts}
        REMAINING POINTS: {self.boones_banes_points}
        BOONES: {self.boones}
        BANES: {self.banes}
        -- SKILLS
        Skill points: {self.skill_points}
        Skills List: {self.skills}
        -- WEALTH
        Social Status: {self.social_status}
        Money: {self.money}
        -- SCHOOLS
        School: {self.school["name"]}
        School Level: {self.school["level"]}
        # talents: {self.school["talents"]}
        # superior maneuvers: {self.school["maneuvers"]}
        Cost: {self.school["cost"]}
        Proficencies: {self.proficencies}
        """

    @property
    def str(self):
        return self._str + self._str_mod

    @property
    def agi(self):
        return self._agi + self._agi_mod

    @property
    def end(self):
        return self._end + self._end_mod

    @property
    def hlt(self):
        return self._hlt + self._hlt_mod

    @property
    def wil(self):
        return self._wil + self._wil_mod

    @property
    def wit(self):
        return self._wit + self._wit_mod

    @property
    def per(self):
        return self._per + self._per_mod

    @property
    def int(self):
        return self._int + self._int_mod

    @property
    def adr(self):
        return (self._agi + self._wit) // 2 + self._adr_mod

    @property
    def mob(self):
        return (self._str + self._agi + self._end) // 2 + self._mob_mod

    @property
    def car(self):
        return (self._str + self._end) // 2 + self._car_mod

    @property
    def cha(self):
        return (self._wil + self._wit + self._per) // 2 + self._cha_mod

    @property
    def tou(self):
        # TODO
        return 4 + self._tou_mod

    @property
    def sdb(self):
        return self._str//2 + self._sdb_mod

    @property
    def grit(self):
        # TODO
        return self._wil // 2 + self._grit_mod

    def set_campaign_power(self, power=None):
        """
        Set the initial campaign power
        if none chosen it will randomize it
        """
        if not self.power:
            if power:
                self.power = campaign_power[power]
            else:
                self.power = random.choice(list(campaign_power.keys()))
                self.pcp = campaign_power[self.power]["pcp"]
                self.max = campaign_power[self.power]["max"]

    @property
    def avaliable_pcp(self):
        return self.pcp - (self.race_pcp + self.attributes_pcp + self.skill_pcp
                           + self.spp_pcp + self.wealth_pcp + self.boones_banes_pcp)

    def set_race(self):
        """
        Sets the races cost
        """
        self.race_pcp = pcp_investment["race_tier"][races_table[self.race]]

    def set_basic_pcps(self):
        """
        Spends 1 pcp on each required aspect
        """
        self.attributes_pcp = 1
        self.spp_pcp = 1
        self.boones_banes_pcp = 1
        self.spp_pcp = 1
        self.wealth_pcp = 1
        self.race_pcp = 1

    def set_attribute_pcp(self):
        """
        defines how many pcp to allocate to attributes
        has no relationship with the lifestyle
        """
        
        if self.avaliable_pcp > 1 :
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.attributes_pcp = random.randint(1, max_value)

    def set_spp_pcp(self):
        """
        shouldn't give many to non military lifestyles
        still the randomizer will allow for it to happen
        this way but it will break.
        """
        if self.lifestyle in NON_MILITARY_LIFESTYLES:
            knows_melee = random.choice([True, False, False, False, False, False])
        else:
            knows_melee = True 
        if self.avaliable_pcp > 1 and knows_melee:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.spp_pcp = random.randint(1, max_value)

    def set_skill_pcp(self):
        """
        defines how many pcp to spend in skills
        """
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.skill_pcp = random.randint(1, max_value)

    def set_boones_banes_pcp(self):
        """
        defines how many pcp to spend in boones and banes
        """
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.boones_banes_pcp = random.randint(1, max_value)
        self.basic_boones_banes_pts = pcp_investment["boones_banes"][self.boones_banes_pcp]

    def set_wealth_pcp(self):
        """
        sets the wealth pcp, it's not based on lifestyles but it limits itself to minor noble
        """
        # TODO move this to a kwargs config initializer
        max_wealth = 6
        if self.avaliable_pcp > 1:
            if max_wealth < self.avaliable_pcp:
                max_value = max_wealth
            else:
                max_value = self.avaliable_pcp
            self.wealth_pcp = random.randint(1, max_value)

    def spend_remaining_pcp(self):
        """
        spend first the spp_pcp only if in the military classes
        """
        # hand picked order
        if self.spp_pcp < self.max and self.lifestyle in MILITARY_LIFESTYLES:
            if self.avaliable_pcp + self.spp_pcp > self.max:
                self.spp_pcp = self.max
            else:
                self.spp_pcp = self.avaliable_pcp + self.spp_pcp
        if self.skill_pcp < self.max:
            if self.avaliable_pcp + self.skill_pcp > self.max:
                self.skill_pcp = self.max
            else:
                self.skill_pcp = self.avaliable_pcp + self.skill_pcp
        if self.attributes_pcp < self.max:
            if self.avaliable_pcp + self.attributes_pcp > self.max:
                self.attributes_pcp = self.max
            else:
                self.attributes_pcp = self.avaliable_pcp + self.attributes_pcp
        if self.boones_banes_pcp < self.max:
            if self.avaliable_pcp + self.boones_banes_pcp > self.max:
                self.boones_banes_pcp = self.max
            else:
                self.boones_banes_pcp = self.avaliable_pcp + self.boones_banes_pcp
        if self.wealth_pcp < self.max:
            if self.avaliable_pcp + self.wealth_pcp > self.max:
                self.wealth_pcp = self.max
            else:
                self.wealth_pcp = self.avaliable_pcp + self.wealth_pcp

    def allocate_pcp(self, power=None):
        """
        allocates PCP
        """
        self.set_campaign_power(power=None)
        self.set_basic_pcps()
        self.set_race()
        self.set_attribute_pcp()
        self.set_spp_pcp()
        self.set_skill_pcp()
        self.set_boones_banes_pcp()
        self.set_wealth_pcp()

        while self.avaliable_pcp > 0:

            self.spend_remaining_pcp()

    def spent_attr(self):
        """
        adds up how many pcp were spent on attrs
        substracts 8 because everyone starts with 1
        """
        return sum([
            self._str,
            self._agi,
            self._end,
            self._hlt,
            self._wil,
            self._wit,
            self._per,
            self._int
        ]) - 8  # basic 1

    @property
    def avaliable_attr_pts(self):
        """
        calculates how many attr pts haven't been spent yet
        """
        return self.attributes_points - self.spent_attr()

    def set_random_attr(self):
        """
        adds +1 to a random attr
        """
        attrs = [
            "_str",
            "_agi",
            "_end",
            "_hlt",
            "_wil",
            "_wit",
            "_per",
            "_int"
        ]
        rand_attr = random.choice(attrs)
        curr_val = self.__getattribute__(rand_attr)
        if curr_val > 7:  # max starting lvl is 8, so search for another attr
            self.set_random_attr()
        else:
            self.__setattr__(rand_attr, curr_val + 1)

    def process_attr_cost(self, value):
        """
        checks if the random generated value exists in the table, otherwise generates another. from 0 to 10 all values exist
        """
        try:
            attr = attribute_costs[value]
            return attr
        except KeyError:
            self.process_attr_cost(value - 1)

    def allocate_attributes(self):
        """
        # first give 2 to each,
        # since the lowest attr_pcp is 22
        # this will leave at least 8 to
        # spend the rest randomly

        """

        self.attributes_points = pcp_investment["attribute"][self.attributes_pcp]

        
        # give all stats a basic random stat up to 2
        self._str = 2
        self._agi = 2
        self._end = 2
        self._hlt = 2
        self._wit = 2
        self._wil = 2
        self._per = 2
        self._int = 2

        while self.avaliable_attr_pts > 0:
            self.set_random_attr()

    def process_race_attrs(self):
        """
        Adds the racial modifiers,
        so far it only takes into account the
        dwarves
        """
        if self.race == "dwarf":
            self._mob_mod = -1
            self._tou_mod = 1
            self._end_mod = 2
            self._hlt_mod = 1

    def filter_boones_or_banes_by_value(self, value, _type):
        """
        value: max cost of the boon or banes
        type: "boon" or "bane" to choose the right table to filter
        """

        if _type == "boon":
            table = boones_cost_full

        elif _type == "bane":
            table = banes_cost_full

        # we convert the boones_banes_points to abs value so we can filter them when they have a negative value
        return {k: v for k, v in table.items() if v <= abs(self.boones_banes_points)}

    def assign_banes(self, banes_list):
        """
        if boones and banes points have a negative value
        select banes to compensate it to 0
        """
        if self.boones_banes_points < 0:
            bane_name = random.choice(list(banes_list.keys()))
            # this should get the bane explanation as well
            self.banes.append(bane_name)
            self.boones_banes_points += banes_list[bane_name]

    def assign_boones(self, boones_list):
        """
        if boones and banes points have a positive value, select boones to compensate it to 0
        """
        if self.boones_banes_points > 0:
            boon_name = random.choice(list(boones_list.keys()))
            # this should append a dict with explanation not only a name of the boon
            self.boones.append(boon_name)
            self.boones_banes_points -= boones_list[boon_name]

    def choose_boon_or_bane(self, _type):
        """
        chooses a boon or bane that hasn't been selected yet
        """
        if _type == "boon":
            table = {k: v for k, v in boones_cost_full.items()
                     if k not in self.boones}
            boon_name = random.choice(list(table.keys()))
            self.boones.append(boon_name)
            self.boones_banes_points -= table[boon_name]

        elif _type == "bane":
            table = {k: v for k, v in banes_cost_full.items()
                     if k not in self.banes}
            bane_name = random.choice(list(table.keys()))
            self.banes.append(bane_name)
            self.boones_banes_points += table[bane_name]

    def allocate_boones_banes(self):
        """
        buy boones and banes
        1. check if points have a negative value
        1.1 if negative, buy banes until it reaches positive value (select only banes that sum up to that value)
        2. 50% chance to want a boon
        2.1 select boon, repeat 2
        3. repeat 1
        """
        self.boones_banes_points = pcp_investment["boones_banes"][self.boones_banes_pcp]

        # if the selected tier implies negative values
        while self.boones_banes_points < 0:

            # filter banes to choose from
            can_buy_banes = self.filter_boones_or_banes_by_value(
                self.boones_banes_points, "bane")
            self.assign_banes(can_buy_banes)
            if self.boones_banes_points == 0:
                break
        # if the selected tier implies points to buy boones without banes

        while self.boones_banes_pcp > 0:
            can_buy_boones = self.filter_boones_or_banes_by_value(
                self.boones_banes_points, "boon")
            self.assign_boones(can_buy_boones)
            if self.boones_banes_points == 0:
                break
        # randomly flavour more boones and banes
        # TODO this isn't working and if it adds boones then it ends up adding much more banes
        # I'm to lazy to check why
        """if self.boones_banes_points == 0:
            choose_new_boon = random.choice([True, False])
            if choose_new_boon:
                self.choose_boon_or_bane("boon")
                self.allocate_boones_banes()
        """

    def incease_skill(self, skill):
        """
        increases paying with pcp,
        has to be modified to be paid with arc
        """
        try:
            self.skills[skill] += 1
        except KeyError:
            self.skills[skill] = 1
        self.skill_points -= 1

    def allocate_skills(self):
        """
        this will process based on pre made profiles
        like "bandit", "knight", etc
        They will be like the packets but more complex
        and will add extra points for not choosing the packets
        adequately
        """

        # set the skill points amount + the modifier
        self.skill_points = pcp_investment["skill"][self.skill_pcp] + \
            skill_pts_balancing_table[self.skill_pcp]

        # This might end up with weird characters
        # have to assess it

        # All lifestyles have AT LEAST 5 basic skills
        basic = random.sample(
            lifestyles[self.lifestyle]["skills"]["basic"], k=5)
        # All lifestyles have AT LEAST 4 other skills
        other_4 = random.sample(
            lifestyles[self.lifestyle]["skills"]["other"], k=4)

        # 1. give 1 point to each basic skill
        for skill in basic:
            self.incease_skill(skill)
        # 2. give 1 point to up to 5 basic skills
        if self.skill_points > 4:  # it can be 1, 4 or more at this stage
            random.shuffle(basic)
            for skill in basic:
                if self.skill_points > 0:
                    self.incease_skill(skill)
        # 3. give points between basic and other skills
        merged = basic + other_4
        while self.skill_points > 0:
            self.incease_skill(random.choice(merged))
            if self.skill_points == 0:
                break

    def allocate_wealth(self):
        """
        allocates money and social status
        """
        self.money = pcp_investment["wealth"][self.wealth_pcp]["amount"]
        self.social_status = pcp_investment["wealth"][self.wealth_pcp]["name"]
    
    def assign_proficencies(self):
        """
        1. if human assign all
        2. other races - asses remaining pts, if more than % 3 num profs or 4
        """

        if self.race == "human":
            proficencies_to_get = self.school["num_proficencies"]
        else:
            proficencies_to_get = min(self.spp_points // 3, 4)
            # pay for them
            self.spp_points -= proficencies_to_get

        self.proficencies = random.sample(proficencies_no_gun, proficencies_to_get)

    def advance_school(self):
        """
        spend the remaning points
        """
        while self.spp_points > 0:
            print(self.spp_points)
            print(self.school["level"])
            next_lvl = self.school["level"] + 1
            if self.spp_points >= school_advancement[next_lvl]:
                self.school["level"] += 1
                self.spp_points -= school_advancement[next_lvl]

            if self.spp_points < school_advancement[next_lvl +1] or self.spp_points == 0:
                break
    
    def assign_school_maneuvers(self):
        """
        assing number of maneuvers avaliable to the character
        """
        self.school["maneuvers"] = school_sup_maneuvers[self.school["level"]]

    def assign_school_talents(self):
        """
        assing number of talents avaliable to the character
        """
        self.school["talents"] = school_talents[self.school["level"]]
    
    def allocate_spp(self):
        """
        choose school and assign points 
        1. determine schools that can be bought (most non military will be scrapers)
        2. choose proficencies
        3. spend the remaining spp_points
        """

        self.spp_points = pcp_investment["spp"][self.spp_pcp]
        # if not many spp don't buy an expensive school
        max_spp_pts_for_school = 5
        if self.spp_points < 4:
            max_spp_pts_for_school = 1
        if self.spp_points < 10:
            max_spp_pts_for_school = 3 
        avaliable_schools = [s for s in spp_schools if s["cost"] <= max_spp_pts_for_school]
        # choose school
        self.school = random.choice(avaliable_schools)
        self.school["level"] = 1
        # choose proficencies
        self.assign_proficencies()
        # spend remaning spp_points
        self.advance_school()
        # assign talents and maneuvers
        self.assign_school_talents()
        self.assign_school_maneuvers()
        




    def build_npc(self):
        """
        Create a new NPC following the CC process
        """
        self.allocate_pcp()
        self.allocate_attributes()
        self.process_race_attrs()
        self.allocate_boones_banes()
        self.allocate_skills()
        self.allocate_wealth()
        self.allocate_spp()
    
    def print_boones(self):
        s = ""
        for boon in self.boones:
            s+= f"- {boon} \n"
        
        return s

    def print_pc(self):
        """
        Prints the character sheet
        """

        print(f"""
        --------------------------------
        Character: {self.race} - {self.lifestyle}
        Starting Power: {self.power}
        --------------------------------
        ATTRIBUTES
        --------------------------------
        STR: {self.str} | AGI: {self.agi} 
        END: {self.end} | HLT: {self.hlt} 
        WIL: {self.wil} | WIT: {self.wit} 
        PER: {self.per} | INT: {self.int} 
        ---------------------------------
        ADR: {self.adr} | MOB: {self.mob}
        CAR: {self.car} | CHA: {self.cha} 
        TOU: {self.tou} | SDB: {self.sdb}
        GRIT: {self.grit}
        ---------------------------------
        BOONES
        ---------------------------------
        {self.print_boones()}
        
        BANES: {self.banes}
        -- SKILLS
        Skill points: {self.skill_points}
        Skills List: {self.skills}
        -- WEALTH
        Social Status: {self.social_status}
        Money: {self.money}
        -- SCHOOLS
        School: {self.school["name"]}
        School Level: {self.school["level"]}
        # talents: {self.school["talents"]}
        # superior maneuvers: {self.school["maneuvers"]}
        Cost: {self.school["cost"]}
        Proficencies: {self.proficencies}
        """)