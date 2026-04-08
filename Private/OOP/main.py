from tournament import Knight, Mage, Rogue, Tournament

if __name__ == "__main__":
    knight = Knight.create_random()
    mage = Mage.create_random()
    rogue = Rogue.create_random()
    tournament = Tournament([knight, mage, rogue])
    tournament.start_tournament()