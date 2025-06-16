require 'table_print'
require_relative 'talia'
require_relative 'gracz_bot'
require_relative 'gracz_czlowiek'


class Gra
    def initialize(players)
        @players = players
        @score = {}
        @deck = Talia.new
        @deck.shuffle

        @players.each do |player|
            @score[player] = 0
        end
    end

    def deal_cards
        until @deck.is_empty
            @players.each do |player|
                player.add_card(@deck.get_card)
            end
        end
    end

    def play_round
        @table = []

        played = @players.map do |player|
            card = player.draw_card
            puts "#{player.name} wykłada kartę: #{card.to_colored_s}"
            [player, card]
        end

        resolve_battle(played)
    end

    def resolve_battle(cards_on_table)
        # Dodanie zagranych kart do stołu
        @table += cards_on_table

        max_value = cards_on_table.map { |p, c| c.compare_value }.max
        contenders = cards_on_table.select { |p, c| c.compare_value == max_value }

        if contenders.size == 1
            winner = contenders.first[0]
            puts Rainbow("> Wygrywa #{winner.name}, zabiera #{@table.size} kart(y).\n").green
            @score[winner] += 1
            @table.each do |_, card|
                winner.add_card(card)
              end              
        else
            puts Rainbow("\n> Wojna między: #{contenders.map { |p, _| p.name }.join(', ')}!\n").red

            # Dodatkowe karty na wojnę
            war_cards = []

            contenders.each do |player, _|
                if player.cards.size < 4
                  puts "> #{player.name} nie ma wystarczająco kart na wojnę! Przegrywa tę rundę."
                  next
                end

                # Wybieramy trzy zakryte karty i jedną odkrytą
                hidden = 3.times.map { player.discard_card }
                shown  = player.draw_card

                puts "> #{player.name} dokłada 3 zakryte karty i odsłania: #{shown.to_colored_s}"
                war_cards << [player, shown]

                # Dodajemy zakryte
                @table.concat(hidden.map { |c| [player, c] })
            end

            # Jeśli przynajmniej dwóch graczy może kontynuować wojnę
            if war_cards.size > 1
                # Rekurencyjne rozstrzyganie wojny
                resolve_battle(war_cards)
            else
                # Jeśli tylko jeden gracz mógł wziąć udział to wygrywa
                winner = war_cards.first&.first
                if winner
                    puts Rainbow("> #{winner.name} wygrywa przez brak przeciwników!\n").yellow
                    @score[winner] += 1
                    @table.each do |_, card|
                        winner.add_card(card)
                      end
                else
                    puts Rainbow("> Nikt nie wygrał tej wojny – karty przepadają!\n").blue
                end
            end
        end
    end

    def play_game
        deal_cards
        round = 1
        # Gra toczy się dopóki więcej niż
        # jeden gracz ma jeszcze jakieś karty
        while @players.count { |p| p.cards.size > 0 } > 1
            puts "<--- Runda ##{round} ---->"
            play_round
            round += 1
        end
        puts "Koniec gry!\n\n"
        tp @score.map { |player, score| { GRACZ: player.name, WYGRANE_RUNDY: score } }
        puts "\nWygrywa #{Rainbow(@score.max_by { |player, score| score }&.first.name).magenta}, gratulacje!"
    end

end
