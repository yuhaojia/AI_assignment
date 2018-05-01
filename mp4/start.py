import sys
from pong import *
from  qlearning import *
from sarsa import *

if __name__ == '__main__':
	print('pong ganme start!!!')
	agent = qlearning()
	# agent = sarsa()
	game = pong(agent)
	game.train()
	game.play()