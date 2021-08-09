import re

def simple_name(name, chapter):
    name_treat = re.sub(" ", "_", name)
    if len(name_treat) > 10:
        name_final = f"{name_treat[:9]}_{chapter}"
    else:
        name_final = complete_name(name, chapter)
    return name_final

def complete_name(name, chapter):
    name_treat = re.sub(" ", "_", name)
    name_treat = re.sub(r":|!|@|#|\$|&|\|", "_", name_treat)
    name_final = f"{name_treat}_{chapter}"
    return name_final