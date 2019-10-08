"""Print out all the melons in our inventory."""


from melons import melon_info


def print_melons(melon_info):
    #price, seedless, flesh_color, rind_color, avg_weight
    """Print each melon with corresponding attribute information."""

    for melon_name, items in melon_info.items():

        print(melon_name.upper())

        for items, element in items.items():
            print(f'{items} : {element}')

print_melons(melon_info)

