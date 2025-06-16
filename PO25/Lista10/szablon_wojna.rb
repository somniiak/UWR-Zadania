require 'table_print'
require_relative 'zapis'
require_relative 'talia'
require_relative 'gracz_bot'
require_relative 'gracz_czlowiek'

class WarStrategy
  include Zapis

  def initialize(players)
    @players = players
    @score = {}
    @deck = Talia.new
    @deck.shuffle
    @round = 1
    @table = []

    @players.each { |player| @score[player] = 0 }
  end

  def deal_cards
    until @deck.is_empty
      @players.each { |player| player.add_card(@deck.get_card) }
    end
  end

  def play_round
    @table = []
    played = @players.map do |player|
      card = player.draw_card
      exit if save_and_exit?(card)
      
      puts "#{player.name} wykłada kartę: #{card.to_colored_s}"
      [player, card]
    end

    resolve_battle(played)
  end

  def game_over?
    @players.count { |p| p.cards.size > 0 } <= 1
  end

  def winner
    @score.max_by { |_, score| score }&.first
  end

  def current_score
    @score.map { |player, score| { GRACZ: player.name, WYGRANE_RUNDY: score } }
  end

  private

  def save_and_exit?(card)
    if card == -1
      puts "\nZapisuję stan gry..."
      self.zapisz_stan(SAVE_FILE)
      puts "Stan gry zapisany."
      true
    end
  end

  def resolve_battle(cards_on_table)
    @table += cards_on_table
    max_value = cards_on_table.map { |_, c| c.compare_value }.max
    contenders = cards_on_table.select { |_, c| c.compare_value == max_value }

    if contenders.size == 1
      declare_round_winner(contenders.first[0])
    else
      handle_war(contenders)
    end
  end

  def declare_round_winner(winner)
    puts Rainbow("> Wygrywa #{winner.name}, zabiera #{@table.size} kart(y).\n").green
    @score[winner] += 1
    @table.each { |_, card| winner.add_card(card) }
  end

  def handle_war(contenders)
    puts Rainbow("\n> Wojna między: #{contenders.map { |p, _| p.name }.join(', ')}!\n").red
    war_cards = []

    contenders.each do |player, _|
      if player.cards.size < 4
        puts "> #{player.name} nie ma wystarczająco kart na wojnę! Przegrywa tę rundę."
        next
      end

      hidden = 3.times.map { player.discard_card }
      shown = player.draw_card

      puts "> #{player.name} dokłada 3 zakryte karty i odsłania: #{shown.to_colored_s}"
      war_cards << [player, shown]
      @table.concat(hidden.map { |c| [player, c] })
    end

    if war_cards.size > 1
      resolve_battle(war_cards)
    else
      handle_war_winner(war_cards.first&.first)
    end
  end

  def handle_war_winner(winner)
    if winner
      puts Rainbow("> #{winner.name} wygrywa przez brak przeciwników!\n").yellow
      @score[winner] += 1
      @table.each { |_, card| winner.add_card(card) }
    else
      puts Rainbow("> Nikt nie wygrał tej wojny - karty przepadają!\n").blue
    end
  end
end