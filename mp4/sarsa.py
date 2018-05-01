import numpy as np
import random

N_STATES = 10369
N_ACTIONS = 3
EPSILON = 0.05
GAMMA = 0.5
ALPHA = 50


class sarsa(object):

    def __init__(self):
        self.id = 'sarsa'
        self.qtable = self.buildQTable(N_STATES, N_ACTIONS)
        self.nsatable = self.buildNSATable(N_STATES, N_ACTIONS)
        self.epsilon = EPSILON
        self.actions = [-1, 0, 1]

    def buildQTable(self, n_states, n_actions):
        table = np.zeros((n_states, n_actions))
        return table

    def buildNSATable(self, n_states, n_actions):
        table = np.zeros((n_states, n_actions))
        return table

    def selectAction(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            state_index = self.getStateIndex(state)
            # action = np.argmax(self.qtable[state_index])
            qvalues = self.qtable[state_index]
            qvalues = qvalues.tolist()
            maxQ = max(qvalues)
            if qvalues.count(maxQ) > 1:
                best = [i for i in range(3) if qvalues[i] == maxQ]
                action = self.actions[random.choice(best)]
                return action
            else:
                return self.actions[qvalues.index(maxQ)]

    def testSelectAction(self, state):
        if random.random() < 0:
            return random.choice(self.actions)
        else:
            state_index = self.getStateIndex(state)
            # action = np.argmax(self.qtable[state_index])
            qvalues = self.qtable[state_index]
            qvalues = qvalues.tolist()
            maxQ = max(qvalues)
            if qvalues.count(maxQ) > 1:
                best = [i for i in range(3) if qvalues[i] == maxQ]
                action = self.actions[random.choice(best)]
                return action
            else:
                return self.actions[qvalues.index(maxQ)]

    def updateQTable(self, state, action, nextaction, reward, nextstate, terminal):
        state_index = self.getStateIndex(state)
        nextstate_index = self.getStateIndex(nextstate)
        self.nsatable[nextstate_index][nextaction+1] += 1
        if not terminal:
            q_target = reward + GAMMA * self.qtable[nextstate_index][nextaction+1]
        else:
            q_target = reward
        self.qtable[state_index][action+1] += float(ALPHA) / float(ALPHA + self.nsatable[
            nextstate_index][nextaction+1]) * (q_target - self.qtable[state_index][action+1])
        # self.qtable[state_index][action+1] += 0.25 * (q_target - self.qtable[state_index][action+1])

    def getStateIndex(self, state):
        index = 72 * 12 * state[0] + 72 * state[1] + \
            36 * state[2] + 12 * state[3] + state[4]
        return index

    def writeFile(self):
        np.savetxt('qtable2.txt', self.qtable, delimiter=',')
