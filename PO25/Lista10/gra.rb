require_relative 'szablon_wojna'

class Game
    include Zapis

    def initialize(strategy)
      @strategy = strategy
      @round = 1
    end
  
    def play_game
      @strategy.deal_cards
  
      loop do
        puts "<--- Runda ##{@round} ---->"
        @strategy.play_round
        break if @strategy.game_over?
        @round += 1
      end
  
      end_game
    end
  
    def end_game
      puts "Koniec gry!\n\n"
      tp @strategy.current_score
      puts "\nWygrywa #{Rainbow(@strategy.winner.name).magenta}, gratulacje!"
    end
  end