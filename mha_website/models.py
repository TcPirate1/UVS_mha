from django.db import models

# Create your models here.

class Card(models.Model):
    def __init__(self, name, rarity, set, cardType, difficulty, control, blockZone, blockModifier, speed, attackZone, damage, symbols, cardText, keywords):
        self.image = models.URLField()
        self.name = name
        self.rarity = rarity
        self.set = set
        self.cardType = cardType
        self.difficulty = difficulty
        self.control = control
        self.blockZone = blockZone
        self.blockModifier = blockModifier
        self.speed = speed
        self.attackZone = attackZone
        self.damage = damage
        self.symbols = symbols
        self.cardText = cardText
        self.keywords = keywords

        def __str__(self):
            return self.name

class Deck(models.Model):
    def __init__(self, name, by, main, main_card_copies, side_card_copies, total_cards, symbol, visibility, description):
        user = models.ForeignKey("User", related_name=("decks"), on_delete=models.CASCADE)
        self.name = name
        self.by = by
        self.main = main
        self.main_card_copies = main_card_copies
        self.side_card_copies = side_card_copies
        self.total_cards = total_cards
        self.symbol = symbol
        self.visibility = visibility
        self.description = description

        def __str__(self):
            return self.name