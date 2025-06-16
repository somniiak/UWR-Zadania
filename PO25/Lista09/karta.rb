require 'rainbow'

class Karta
    # @@Cards - zmienna klasowa, wspólna dla całej klasy, a
    # nie dla pojedyńczych obiektów.
    @@cards = {}

    attr_reader :rank, :suit, :symbol, :color

    def initialize(suit, rank)
        # Głowne atrybuty
        # suit - kolor/rodzaj: ':kier', ':karo', ':trefl', ':pik'
        # rank - wartość/figura: '2', .., '10', ':walet', ':dama', ':krol', ':as'
        @suit = suit
        @rank = rank

        # Dodatkowe atrybuty
        @symbol = get_symbol(suit)
        @color = get_color(suit)
    end

    def get_symbol(suit)
        case suit
        when :kier
            "♥"
          when :karo
            "♦"
          when :pik
            "♠"
          when :trefl
            "♣"
          else
            "?"
        end
    end

    def get_color(suit)
        case suit
        when :kier, :karo
            :red
        when :pik, :trefl
            :black
        end
    end

    def compare_value
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', :walet, :dama, :krol, :as]
        ranks.index(@rank) + 2
    end

    def to_s
        "#{@rank.capitalize}#{@symbol}"
    end

    def to_colored_s
        colored_symbol = Rainbow(symbol).color(color == :red ? :red : :darkslategray)
        "#{rank.capitalize}#{colored_symbol}"
    end

    # self - medota statyczna, nie wymaga utworzenia obiektu
    def self.get_card(suit, rank)
        key = "#{suit}-#{rank}"
        unless @@cards[key]
            @@cards[key] = Karta.new(suit, rank)
        end
        @@cards[key]
    end
end
