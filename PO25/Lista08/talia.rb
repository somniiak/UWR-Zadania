require 'rainbow'
require_relative 'karta'

class Talia
    def initialize
        @cards = []
        suits = [:kier, :karo, :pik, :trefl]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', :walet, :dama, :krol, :as]

        suits.each do |suit|
            ranks.each do |rank|
                @cards << Karta.get_card(suit, rank)
            end
        end
    end

    def is_empty
        @cards.empty?
    end

    def shuffle
        @cards.shuffle!
    end

    def get_card
        unless @cards.empty?
            @cards.shift
        end 
    end

    def show
        print "Dostępne karty:\n"
        @cards.each_with_index do |card, idx|
            number = Rainbow(idx + 1).gray
            label  = card.to_colored_s
            spacing = " " * (6 - card.to_s.length)
            print " " unless idx > 8
            print "#{number}. #{label} #{spacing}"
            puts if (idx + 1) % 7 == 0
        end
        puts
    end
end
