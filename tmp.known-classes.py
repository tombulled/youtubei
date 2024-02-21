with open("resources/known-classes.txt") as file:
    known_classes = file.readlines()

for cls in known_classes:
    cls = cls.strip()

    # if not cls.endswith("Action"):
    # if not cls.endswith("Endpoint"):
    if not cls.endswith("Command"):
        continue

    print(cls)
