############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
  

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless


        self.is_bestseller = is_bestseller

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairings):
        """Add a food pairing to the instance's pairings list."""
        self.pairings = pairings
        pairings.append()
        return pairings


        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types(Melontype):
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('Casaba', 'cas', 2003, 'orange', True, False)
    cas.add_pairing('strawberries and mint')
    all_melon_types.append(cas)

    cren = MelonType('Crenshaw','cren',1996,'green',True,False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('Yellow Watermelon','yw',2013,'yellow',True,True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    melon_name = make_melon_types(MelonType(name))
    
    print("{} pairs with {}".fomat(name,))
    # Fill in the rest
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



