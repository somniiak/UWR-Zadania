# Artur Dzido
# Lista 8
# Ruby 3.3.8

require_relative 'gra'
require_relative 'gracz_bot'
require_relative 'gracz_czlowiek'

player = GraczCzlowiek.new("Gregg")
bot = GraczBot.new("Tux")

gra = Gra.new([player, bot])
gra.play_game
