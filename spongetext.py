print(" ".join(["".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(tok)]) for tok in input("> ").split(" ")]))
