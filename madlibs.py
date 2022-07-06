# String concatenation putting strings together

madlibs = ""

adjective = input("Enter an adjective: ")
nouns = []
for x in range(3):
    a = ""
    if x > 0:
        a = "another"
    else:
        a = "a"
    noun = input(f"Enter {a} noun: ")
    nouns.append(noun)

nounPlural = input("Enter a noun plural: ")
bodyPart1 = input("Enter a body part: ")
bodyPart2 = input("Enter another body part: ")
verb = input("Enter a verb: ")
# verbPastTense1 = input("Enter a verb(Past tense): ")
# verbPastTense2 = input("Enter another verb(Past tense): ")
spell1 = input("Enter a magic spell: ")
spell2 = input("Enter another magic spell: ")
madlibs = f"A pretty glow burst suddenly across the enchanted sky above them as an edge of dazzling sun appeared over the sill of \
    the nearest {nouns[0]}. The light hit both their {bodyPart1} at the same time, so that Voldemort's was suddenly a flaming {nouns[1]}.\
    Harry heard the high voice shriek as he too {verb} his best hope to the heavens, pointing Draco's {nouns[2]}:\n\"{spell1}!!!!\"\n{spell2}!\n\
    The bang was like a cannon blast, and the soft flames that erupted between them, at the dead center of the circle they had been treading,\
    marked the point where the {bodyPart2} collided."
print(madlibs)
