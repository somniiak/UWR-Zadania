package cards:
    enum Color:
        case Clubs, Diamonds, Hearts, Spades

    enum Value:
        case Ace
        case Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten
        case Jack, Queen, King

        def isNumerical: Boolean = this match
            case Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten => true
            case _ => false

        def isFace: Boolean = this match
            case Jack | Queen | King => true
            case _ => false

        def points: Int = this match
            case Ace   => 1; case Two   => 2
            case Three => 3; case Four  => 4
            case Five  => 5; case Six   => 6
            case Seven => 7; case Eight => 8
            case Nine  => 9; case Ten   => 10
            case Jack | Queen | King => 10

    case class Card(color: Color, value: Value)

package deck:
    import scala.math.Ordered.orderingToOrdered
    import scala.util.Random
    import cards._

    class Deck(val cards: List[Card]):
        def pull(): Deck = cards match
            case _ :: tl => Deck(tl)
            case Nil => this

        def push(card: Card): Deck =
            Deck(card :: cards)

        def push(color: Color, value: Value): Deck =
            push(Card(color, value))

        val isStandard: Boolean =
            val ord: Card => (Int, Int) = c => (c.color.ordinal, c.value.ordinal)
            cards.sortBy(ord) == Deck.standardDeckCards.sortBy(ord)

        def duplicatesOfCard(card: Card): Int =
            math.max(cards.count(_ == card) - 1, 0)

        def amountOfColor(color: Color): Int =
            cards.count(_.color == color)

        def amountOfNumerical(value: Value): Int =
            require(value.isNumerical)
            cards.count(_.value == value)

        val amountWithNumerical: Int =
            cards.count(_.value.isNumerical)

        def amountOfFace(value: Value): Int =
            require(value.isFace)
            cards.count(_.value == value)

        val amountWithFace: Int =
            cards.count(_.value.isFace)

    object Deck:
        val standardDeckCards: List[Card] = for {
            color <- Color.values.toList
            value <- Value.values.toList
        } yield Card(color, value)

        val standardDeckSize: Int = standardDeckCards.size

        def apply(cards: List[Card]): Deck =
            new Deck(cards)

        def apply(): Deck =
            new Deck(Random.shuffle(standardDeckCards))

package games:
    import scala.util.Random
    import cards._
    import deck._

    class Blackjack(deck: Deck):
        private def totalPoints(cards: List[Card]): Int =
            val base = cards.map(_.value.points).sum
            val aces = cards.count(_.value == Value.Ace)
            (0 until aces).foldLeft(base): (acc, _) =>
                if acc + 10 <= 21 then acc + 10 else acc

        private def prettyCard(card: Card): String =
            val symbol = card.color match
                case Color.Clubs    => "♣"
                case Color.Diamonds => "♦"
                case Color.Hearts   => "♥"
                case Color.Spades   => "♠"
            s"[$symbol ${card.value}]"

        def play(n: Int): Unit =
            val drawn = deck.cards.take(n)
            drawn.foreach: card =>
                println(s"${prettyCard(card)} - ${card.value.points} pts")
            println(s"Total: ${totalPoints(drawn)} pts")

        lazy val all21: List[List[Card]] =
            val cards = deck.cards
            (1 to cards.length)
                .flatMap(len => cards.combinations(len))
                .filter(combo => totalPoints(combo) == 21)
                .toList

        def first21(): Unit =
            val cards = deck.cards
            val result =(1 to cards.length).iterator
                .flatMap(len => cards.combinations(len))
                .find(combo => totalPoints(combo) == 21)

            result match
                case Some(combo) =>
                    combo.foreach(c => println(s"${prettyCard(c)}"))
                    println(s"Total: ${totalPoints(combo)} pts")
                case None =>
                    println("No combination giving 21 found.")

    object Blackjack:
        def apply(numOfDecks: Int): Blackjack =
            new Blackjack(Deck(Random.shuffle(
                (1 to numOfDecks).flatMap(_ => Deck.standardDeckCards).toList
            )))

@main def main(): Unit =

    import cards._
    import deck._
    import games._

    val exampleCard = Card(Color.Hearts, Value.Queen)
    println(s"Card: $exampleCard")
    println(s"Is face: ${exampleCard.value.isFace}")
    println(s"Is numerical: ${exampleCard.value.isNumerical}")
    println(s"Points: ${exampleCard.value.points}")
    println()

    val standardDeck = Deck()
    println(s"Deck size: ${standardDeck.cards.size}")
    println(s"Is standard: ${standardDeck.isStandard}")
    println(s"Amount of Hearts: ${standardDeck.amountOfColor(Color.Hearts)}")
    println(s"Amount of Queens: ${standardDeck.amountOfFace(Value.Queen)}")
    println(s"Amount of Fives: ${standardDeck.amountOfNumerical(Value.Five)}")
    println(s"Amount with face: ${standardDeck.amountWithFace}")
    println(s"Amount with numerical: ${standardDeck.amountWithNumerical}")
    println()

    val modifiedDeck = standardDeck.pull().pull().push(Card(Color.Hearts, Value.Ace))
    println(s"Size: ${modifiedDeck.cards.size}")
    println(s"Is standard: ${modifiedDeck.isStandard}")
    println()

    val game = Blackjack(3)
    println("Playing 5 cards...")
    game.play(5)
    println()

    println("First combination giving 21:")
    game.first21()
