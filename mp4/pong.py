from ball import *
from paddle import *
import math
import numpy as np
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
from functools import reduce
import sys
import time
from sys import exit

N_STATES = 10369
N_ACTIONS = 3
TRAINING_TIMES = 100000
PLAY_TIMES = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 200
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
LINETHICKNESS = 5
PADDLESIZE = 100


class pong(object):

    def __init__(self, agent):
        print('this is pong class')
        self.ball = None
        self.paddle = None
        self.qtable = None
        self.terminal = False
        self.scores = []
        self.agent = agent
        self.score = 0
        self.scores_cumsum = None
        self.playscore = 0
        self.playscores = []
        self.playscores_cumsum = None
        self.state = None
        self.action = None

    def buildQTable(self, n_states, n_actions):
        table = np.zeros((n_states, n_actions))
        return table

    def getReward(self):
        reward = 0
        if self.checkBounceFromPaddle():
            self.score += 1
            self.ball.bounceFromPaddle()
            reward = 1
        if self.checkTerminal():
            reward = -1
        return reward

    def getReward_human(self, human_paddle_y):
        reward = 0
        if self.checkBounceFromPaddle_human(human_paddle_y):
            self.score += 1
            reward = 1
        if self.checkTerminal_human(human_paddle_y):
            reward = -1
        return reward

    def checkBounceFromPaddle(self):
        if self.ball.x > self.paddle.x:
            if self.ball.y > self.paddle.y and self.ball.y < self.paddle.y + self.paddle.height:
                return True
            else:
                return False
        return False

    def checkBounceFromPaddle_human(self, human_paddle_y):
        if self.ball.x < 0:
            if self.ball.y > human_paddle_y and self.ball.y < human_paddle_y + self.paddle.height:
                return True
            else:
                return False
        return False

    def checkTerminal(self):
        self.terminal = False
        if self.ball.x > self.paddle.x:
            if self.ball.y <= self.paddle.y or self.ball.y >= self.paddle.y + self.paddle.height:
                self.terminal = True
        return self.terminal

    def checkTerminal_human(self, human_paddle_y):
        self.terminal = False
        if self.ball.x < 0:
            if self.ball.y <= human_paddle_y or self.ball.y >= human_paddle_y + self.paddle.height:
                self.terminal = True
        return self.terminal

    def updateState(self):
        if self.terminal:
            return (12, 12, 12, 12, 12)
        else:
            if self.ball.v_x > 0:
                vel_x = 1
            else:
                vel_x = -1
            if self.ball.v_y >= 0.015:
                vel_y = 1
            elif self.ball.v_x <= -0.0015:
                vel_y = -1
            else:
                vel_y = 0

            ball_x = min(11, math.floor(12 * self.ball.x))
            ball_y = min(11, math.floor(12 * self.ball.y))
            paddle_y = min(11, math.floor(
                12 * self.paddle.y / (1 - self.paddle.height)))
            return (ball_x, ball_y, vel_x, vel_y, paddle_y)

    def Qtrain(self):
        self.ball = ball()
        self.paddle = paddle(self.agent)
        for i in range(TRAINING_TIMES):
            print(i + 1, ' time/times Q training')
            self.terminal = False
            self.ball.initBall()
            self.paddle.initPaddle()
            self.score = 0
            state = self.updateState()
            self.state = state
            self.checkTerminal()
            while not self.terminal:
                action = self.agent.selectAction(state)
                self.paddle.update(action)
                self.ball.update()
                nextstate = self.updateState()
                reward = self.getReward()
                # print(reward)
                self.agent.updateQTable(
                    state, action, reward, nextstate, self.terminal)
                state = nextstate
                self.state = state
                # print(state)
                self.checkTerminal()
            self.scores.append(self.score)
            # self.score = 0
        self.scores_cumsum = np.cumsum(self.scores)
        result = []
        for i in range(len(self.scores_cumsum)):
            # print(self.scores_cumsum[i]/(i+1))
            result.append(self.scores_cumsum[i] / i + 1)
        print(result)
        # self.plot()
        self.agent.writeFile()

    def sarsa_train(self):
        self.ball = ball()
        self.paddle = paddle(self.agent)
        for i in range(TRAINING_TIMES):
            print(i + 1, ' time/times SARSA training')
            self.terminal = False
            self.ball.initBall()
            self.paddle.initPaddle()
            self.score = 0
            self.checkTerminal()
            state = self.updateState()
            self.state = state
            action = self.agent.selectAction(state)
            self.action = action
            while not self.terminal:
                reward = self.getReward()
                self.paddle.update(action)
                self.ball.update()
                nextstate = self.updateState()
                nextaction = self.agent.selectAction(nextstate)
                self.agent.updateQTable(
                    state, self.action, nextaction, reward, nextstate, self.terminal)
                state = nextstate
                self.state = state
                action = nextaction
                self.action = action
                self.checkTerminal()
            self.scores.append(self.score)
        self.scores_cumsum = np.cumsum(self.scores)
        result = []
        for i in range(len(self.scores_cumsum)):
            result.append(self.scores_cumsum[i] / (i + 1))
        print(result)
        # self.plot()
        self.agent.writeFile()

    def train(self):
        if self.agent.id == 'qlearning':
            self.Qtrain()
        if self.agent.id == 'sarsa':
            self.sarsa_train()

    def plot(self):
        x_label = 'Episodes'
        y_label = 'Mean Episode Rewards'
        title = 'Mean Episode Rewards vs. Episodes'
        y = []
        for i in range(1, 101):
            # if i = 0:
            #     y.append(self.scores_cumsum[i]/)
            y.append(self.scores_cumsum[i * 1000 - 1] / (i * 1000))
        x = [(i + 1) * 1000 for i in range(100)]
        plt.plot(x, y, 'r-x')
        plt.legend()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def play(self):
        if self.agent.id == 'qlearning':
            self.ball = ball()
            self.paddle = paddle(self.agent)
            self.scores = []
            self.scores_cumsum = None
            self.score = 0
            self.qtable = np.loadtxt('qtable.txt', delimiter=',')
            # self.Qplay()
            # self.QGUI()
            self.human_GUI()
        if self.agent.id == 'sarsa':
            self.ball = ball()
            self.paddle = paddle(self.agent)
            self.scores = []
            self.scores_cumsum = None
            self.score = 0
            self.qtable = np.loadtxt('qtable2.txt', delimiter=',')
            self.sarsa_play()
            # self.sarsa_GUI()

    def Qplay(self):
        for i in range(PLAY_TIMES):
            print(i + 1, ' time/times playing')
            self.terminal = False
            self.ball.initBall()
            self.paddle.initPaddle()
            self.score = 0
            state = self.updateState()
            self.checkTerminal()
            while not self.terminal:
                # self.draw(state)
                action = self.agent.testSelectAction(state)
                self.paddle.update(action)
                self.ball.update()
                nextstate = self.updateState()
                nextaction = self.agent.selectAction(nextstate)
                # self.getReward()
                state = nextstate
                action = nextaction
                self.state = state
                self.checkTerminal()
            self.scores.append(self.score)
            print(self.score)
        # print('mean score of 200 QLearning Games', reduce(lambda x, y: x + y, self.playscores) / len(self.playscores))
        self.scores_cumsum = np.cumsum(self.scores)
        result = []
        for i in range(len(self.scores_cumsum)):
            result.append(self.scores_cumsum[i] / (i + 1))
        print('play mean', result)

    def sarsa_play(self):
        for i in range(PLAY_TIMES):
            print(i + 1, ' time/times SARA playing')
            self.terminal = False
            self.ball.initBall()
            self.paddle.initPaddle()
            self.score = 0
            state = self.updateState()
            self.checkTerminal()
            action = self.agent.selectAction(state)
            while not self.terminal:
                self.getReward()
                self.paddle.update(action)
                self.ball.update()
                nextstate = self.updateState()
                nextaction = self.agent.selectAction(nextstate)
                state = nextstate
                action = nextaction
                self.checkTerminal()
            self.scores.append(self.score)
            print(self.score)
        # print('mean score of 200 SARSA Games', reduce(lambda x, y: x + y, self.playscores) / len(self.playscores))
        self.scores_cumsum = np.cumsum(self.scores)
        result = []
        for i in range(len(self.scores_cumsum)):
            result.append(self.scores_cumsum[i] / (i + 1))
        print('SARSA play mean', result)

    def scaleBall(self, unit):
        return 500 * unit - LINETHICKNESS / 2

    def scalePaddle(self, unit):
        return 500 * unit - LINETHICKNESS

    def scaleWall(self, unit):
        return 500 * unit

    def drawBall(self, ball):
        ball.x = self.scaleBall(self.ball.x)
        ball.y = self.scaleBall(self.ball.y)
        pygame.draw.rect(SURFACE, RED, ball)
        # print('this is a drawball')

    def drawWall(self, wall):
        pygame.draw.rect(SURFACE, BLACK, wall)

    def drawPaddle(self, paddle):
        paddle.y = self.scalePaddle(self.paddle.y)
        pygame.draw.rect(SURFACE, BLACK, paddle)

    def drawHumanPaddle(self, paddle, human_paddle_y):
        paddle.y = self.scalePaddle(human_paddle_y)
        pygame.draw.rect(SURFACE, BLACK, paddle)

    def Qupdate(self):
        if not self.terminal:
            action = self.agent.testSelectAction(self.state)
            self.paddle.update(action)
            self.ball.update()
            nextstate = self.updateState()
            reward = self.getReward()
            self.state = nextstate
        else:
            self.terminal = False
            self.state = None
            self.ball.initBall()
            self.paddle.initPaddle()
            self.state = self.updateState()
            self.checkTerminal()
            print(self.score)
            self.score = 0

    def QGUI(self):
        self.terminal = False
        self.ball.initBall()
        self.paddle.initPaddle()
        self.score = 0
        self.state = self.updateState()
        self.checkTerminal()
        pygame.init()
        global SURFACE
        FPSCLOCK = pygame.time.Clock()
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('AWESOME PONG GAME')
        ball_x = self.scaleBall(self.state[0])
        ball_y = self.scaleBall(self.state[1])
        ball = pygame.Rect(ball_x, ball_y, LINETHICKNESS, LINETHICKNESS)
        paddle_x = self.scalePaddle(self.paddle.x)
        paddle_y = self.scalePaddle(self.state[4])
        paddle_height = self.scaleWall(self.paddle.height)
        paddle = pygame.Rect(paddle_x, paddle_y, LINETHICKNESS, paddle_height)
        wall_x = self.scaleWall(0.0)
        wall_y = self.scaleWall(0.0)
        wall = pygame.Rect(wall_x, wall_y, LINETHICKNESS, WINDOWHEIGHT)
        wall_x2 = self.scaleWall(0.0)
        wall_y2 = self.scaleWall(0.0)
        wall2 = pygame.Rect(wall_x2, wall_y2, WINDOWHEIGHT, LINETHICKNESS)
        wall_x3 = self.scaleWall(0.0)
        wall_y3 = self.scaleWall(0.99)
        wall3 = pygame.Rect(wall_x3, wall_y3, WINDOWHEIGHT, LINETHICKNESS)
        SURFACE.fill(WHITE)
        self.drawBall(ball)
        self.drawWall(wall)
        self.drawWall(wall2)
        self.drawWall(wall3)
        self.drawPaddle(paddle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.agent.id == 'qlearning':
                self.Qupdate()

            SURFACE.fill(WHITE)
            self.drawBall(ball)
            self.drawPaddle(paddle)
            self.drawWall(wall)
            self.drawWall(wall2)
            self.drawWall(wall3)

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def human_GUI(self):
        self.terminal = False
        self.ball.initBall()
        self.paddle.initPaddle()
        self.score = 0
        self.state = self.updateState()
        self.checkTerminal()
        pygame.init()
        global SURFACE
        FPSCLOCK = pygame.time.Clock()
        FPSCLOCK.tick(60)
        SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('AWESOME PONG GAME - HUMAN')

        ball_x = self.scaleBall(self.state[0])
        ball_y = self.scaleBall(self.state[1])
        ball = pygame.Rect(ball_x, ball_y, LINETHICKNESS, LINETHICKNESS)

        paddle_x = self.scalePaddle(self.paddle.x)
        paddle_y = self.scalePaddle(self.state[4])
        paddle_height = self.scaleWall(self.paddle.height)
        paddle = pygame.Rect(paddle_x, paddle_y, LINETHICKNESS, paddle_height)

        human_paddle_x = self.scalePaddle(0.01)
        human_paddle_y = self.scalePaddle(0.5)
        humanpaddle_height = self.scaleWall(self.paddle.height)
        human_paddle = pygame.Rect(
            human_paddle_x, human_paddle_y, LINETHICKNESS, paddle_height)

        wall_x2 = self.scaleWall(0.0)
        wall_y2 = self.scaleWall(0.0)
        wall2 = pygame.Rect(wall_x2, wall_y2, WINDOWHEIGHT, LINETHICKNESS)
        wall_x3 = self.scaleWall(0.0)
        wall_y3 = self.scaleWall(0.99)
        wall3 = pygame.Rect(wall_x3, wall_y3, WINDOWHEIGHT, LINETHICKNESS)

        SURFACE.fill(WHITE)
        self.drawBall(ball)
        self.drawWall(wall2)
        self.drawWall(wall3)
        self.drawPaddle(paddle)
        human_paddle_y = 0.5
        self.drawHumanPaddle(human_paddle, human_paddle_y)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                human_paddle_y = human_paddle_y - 0.04
                if human_paddle_y < 0:
                    human_paddle_y = 0
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                human_paddle_y = human_paddle_y + 0.04
                if human_paddle_y > 0.8:
                    human_paddle_y = 0.8

            if self.agent.id == 'qlearning':
                self.Qupdate_human(human_paddle_y)

            SURFACE.fill(WHITE)
            self.drawBall(ball)
            self.drawPaddle(paddle)
            self.drawHumanPaddle(human_paddle, human_paddle_y)
            self.drawWall(wall2)
            self.drawWall(wall3)
            pygame.time.wait(100)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def Qupdate_human(self, human_paddle_y):
        if not self.terminal:
            action = self.agent.testSelectAction(self.state)
            self.paddle.update(action)
            self.ball.update_human()
            nextstate = self.updateState()
            reward = self.getReward()
            reward = self.getReward_human(human_paddle_y)
            self.state = nextstate
        else:
            self.terminal = False
            self.state = None
            self.ball.initBall()
            self.paddle.initPaddle()
            self.state = self.updateState()
            self.checkTerminal()
            self.checkTerminal_human(human_paddle_y)
            print(self.score)
            self.score = 0
