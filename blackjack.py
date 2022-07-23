import random
from turtle import clear


def dealCard():
    """Returns a random card from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(cards):
    """Take a list of cards and  return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Lose, opponent has BlackJack"
    elif userScore == 0:
        return "Win with a BlackJack"
    elif userScore > 21:
        return "You Lose"
    elif computerScore > 21:
        return "You Win"
    elif computerScore < userScore:
        return "You Win"
    else:
        return "You Lose"


def playGame():
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)

        print(f"your Cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            nextInput = input("Type 'y' to get another card, type 'n' to pass")
            if nextInput == 'y':
                userCards.append(dealCard())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)

    print(f"Your final hand: {userCards} , final score: {userScore}")
    print(
        f"Computer's final hand: {computerCards} , final score: {computerScore}")
    print(compare(userScore, computerScore))


while input("Do you want to play Blackjack? Type 'y' or 'n'") == 'y':
    clear()
    playGame()
