require_relative 'karta'

class GraczCzlowiek
    attr_reader :name, :cards

    def initialize(name)
        @name = name.dup
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
        puts "\n#{name}, wybierz kartę (1-#{@cards.size}):"
        @cards.each_with_index do |card, idx|
            number = Rainbow(idx + 1).gray
            label  = card.to_colored_s
            spacing = " " * (6 - card.to_s.length)
            print " " unless idx > 8
            print "#{number}. #{label} #{spacing}"
            puts if (idx + 1) % 7 == 0
        end
        print "\n\n(Input)> "
        choice = gets.to_i - 1
        while choice < 0 or choice > @cards.size - 1
            puts "Wartość poza zakresem! Spróbuj ponownie."
            print "(Input)> "
            choice = gets.to_i - 1
        end
        @cards.delete_at(choice)
    end
end
