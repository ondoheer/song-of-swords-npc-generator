import random

from modules.randomizers import power_randomizer
from modules.tables import campaign_power, races_table, pcp_investment, attribute_costs


class Character():

    _str = 1
    agi = 1
    end = 1
    hlt = 1
    wil = 1
    wit = 1
    per = 1
    _int = 1

    def __init__(self, race="human"):
        self.race = race

        # character creation PCP
        self.power = None
        self.pcp = None
        self.max = None
        self.race_pcp = 0
        self.attributes_pcp = 0
        self.attributes_points = 0
        self.skill_pcp = 0
        self.spp_pcp = 0
        self.wealth_pcp = 0
        self.boones_banes_pcp = 0

        # attribute points to spend

    def __str__(self):

        return f"""
        -- ATRIBUTES
        STR: {self._str}
        AGI: {self.agi}
        END: {self.end}
        HLT: {self.hlt}
        WIL: {self.wil}
        WIT: {self.wit}
        PER: {self.per}
        INT: {self._int}
        AVALIABLE ATTR PCP: {self.avaliable_attr_pts}
        -- COMPOUND
        ADR: {self.adr}
        MOB: {self.mob}
        CAR: {self.car}
        CHA: {self.cha}
        TOU: {self.tou}
        SDB: {self.sdb}
        GRIT: {self.grit}
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



        """

    @property
    def adr(self):
        return (self.agi + self.wit) // 2

    @property
    def mob(self):
        return (self._str + self.agi + self.end) // 2

    @property
    def car(self):
        return (self._str + self.end) // 2

    @property
    def cha(self):
        return (self.wil + self.wit + self.per) // 2

    @property
    def tou(self):
        # TODO
        return 4

    @property
    def sdb(self):
        return self._str//2

    @property
    def grit(self):
        # TODO
        return self.wil // 2

    def set_campaign_power(self, power=None):
        """
        Set the initial campaign power
        if none chosen it will randomize it
        """
        if not self.power:
            if power:
                self.power = campaign_power[power]
            else:
                self.power = power_randomizer()
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
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.attributes_pcp = random.randint(1, max_value)

    def set_spp_pcp(self):
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.spp_pcp = random.randint(1, max_value)

    def set_skill_pcp(self):
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.skill_pcp = random.randint(1, max_value)

    def set_boones_banes_pcp(self):
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.boones_banes_pcp = random.randint(1, max_value)

    def set_wealth_pcp(self):
        if self.avaliable_pcp > 1:
            if self.max < self.avaliable_pcp:
                max_value = self.max
            else:
                max_value = self.avaliable_pcp
            self.wealth_pcp = random.randint(1, max_value)

    def spend_remaining_pcp(self):
        # hand picked order
        if self.spp_pcp < self.max:
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

    def spend_attr(self):
        return sum([
            self._str,
            self.agi,
            self.end,
            self.hlt,
            self.wil,
            self.wit,
            self.per,
            self._int
        ]) - 8  # basic 1

    @property
    def avaliable_attr_pts(self):
        return self.attributes_points - self.spend_attr()

    def process_attr_cost(self, value):
        """
        checks if the random generated value exists in the table, otherwise generates another
        """
        try:
            attr = attribute_costs[value]
            return attr
        except KeyError:
            self.process_attr_cost(value - 1)

    def allocate_attributes(self):

        self.attributes_points = pcp_investment["attribute"][self.attributes_pcp]

        # first random values 2 to 4
        # then spend the rest randomly

        # give all stats a basic random stat up to avg
        if self.avaliable_attr_pts:
            self._str = self.process_attr_cost(random.randint(1, 5))

        if self.avaliable_attr_pts:
            self.agi = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self.end = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self.hlt = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self.wil = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self.wit = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self.per = self.process_attr_cost(random.randint(1, 5))
        if self.avaliable_attr_pts:
            self._int = self.process_attr_cost(random.randint(1, 5))
        print(self.spend_attr())

    def build_npc(self):
        self.allocate_pcp()
        self.allocate_attributes()
