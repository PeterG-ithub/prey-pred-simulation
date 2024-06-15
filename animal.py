import random


class Animal:
    def __init__(self) -> None:
        self.hunt_success_rate = 0.0
        self.flee_success_rate = 0.0
        self.birth_rate = 0.0
        self.starvation_time = 0

    def roll(self):
        return random.random()

    def did_hunt_succeed(self) -> bool:
        if self.roll() < self.hunt_success_rate:
            return True
        return False

    def did_flee_succeed(self) -> bool:
        if self.roll() < self.flee_success_rate:
            return True
        return False


def test_did_hunt_suceed(hunt_success_rate, test_num=1000):
    anim = Animal()
    anim.hunt_success_rate = hunt_success_rate
    test_case = test_num
    success = 0
    for i in range(test_case):

        hunt_sucess = anim.did_hunt_succeed()
        # print(hunt_sucess)
        if (hunt_sucess):
            success += 1

    print(f'Hunt success rate: {success / test_case}')


def test_did_flee_suceed(flee_success_rate, test_num=1000):
    anim = Animal()
    anim.flee_success_rate = flee_success_rate
    test_case = test_num
    success = 0
    for i in range(test_case):

        flee_success = anim.did_flee_succeed()
        # print(hunt_sucess)
        if (flee_success):
            success += 1

    print(f'Flee success rate: {success / test_case}')


test_did_hunt_suceed(0.8, 1000)
test_did_hunt_suceed(0.1, 1000)
test_did_flee_suceed(0.3, 1000)
test_did_flee_suceed(1, 1000)
