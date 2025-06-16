require_relative 'karta'

class GraczBot
    attr_reader :name, :cards

    def initialize(name = "Player")
        @name = name + " (Bot)"
        @cards = []
    end

    def add_card(card)
        @cards << card
    end

    def discard_card
        card = @cards.sample
        @cards.delete(card)
    end

    def draw_card
        card = @cards.sample
        @cards.delete(card)
    end
end
