import random

#H - represents Heads
#T - represents Tails
class Game:

    def Simulate(self, probHeads):

        reward = -250
        twoBack = ""
        oneBack = ""
        for i in range(1,21):

            score = random.random()

            if score <= probHeads:
                outcome = 'H'
            else:
                outcome = 'T'

            if twoBack == 'T' and oneBack == 'T' and outcome == 'H':
                reward = reward + 100

            twoBack = oneBack
            oneBack = outcome

        return reward

g = Game()

sumOfRewards = 0
for i in range(0, 1000):
    rew = g.Simulate(0.4)

    sumOfRewards = sumOfRewards + rew

print("Average of 1000 realizations is {}".format( sumOfRewards/1000))
