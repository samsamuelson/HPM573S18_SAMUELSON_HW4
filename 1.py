import random

#1 - represents Heads
#2 - represents Tails
class Game:

    def Simulate(self):

        reward = -250
        twoBack = 0
        oneBack = 0
        for i in range(1,21):

            outcome = random.randint(1,2)

            if twoBack == 2 and oneBack == 2 and outcome == 1:
                reward = reward + 100

            twoBack = oneBack
            oneBack = outcome

        return reward

g = Game()

sumOfRewards = 0
for i in range(0, 1000):
    rew = g.Simulate()

    sumOfRewards = sumOfRewards + rew

print("Average of 1000 realizations is {}".format( sumOfRewards/1000))
