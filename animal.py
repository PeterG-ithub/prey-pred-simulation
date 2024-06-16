import random


class Animal:
    def __init__(self, role='prey') -> None:
        assert role in ['predator', 'prey'], "Role must be 'predator' or 'prey'"
        self.hunt_success_rate = 0.0
        self.flee_success_rate = 0.0
        self.birth_rate = 0.0
        self.starvation_time = 0
        self.role = role

    def roll(self):
        return random.random()

    def is_hunt_successful(self) -> bool:
        if self.roll() < self.hunt_success_rate:
            return True
        return False

    def is_flee_successful(self) -> bool:
        if self.roll() < self.flee_success_rate:
            return True
        return False

    def has_starved(self) -> bool:
        if self.starvation_time < 0:
            return True
        return False


def test_is_hunt_successful(hunt_success_rate, test_num=1000):
    anim = Animal()
    anim.hunt_success_rate = hunt_success_rate
    test_case = test_num
    success = 0
    for i in range(test_case):

        hunt_sucess = anim.is_hunt_successful()
        # print(hunt_sucess)
        if (hunt_sucess):
            success += 1

    print(f'Hunt success rate: {success / test_case}')


def test_is_flee_successful(flee_success_rate, test_num=1000):
    anim = Animal()
    anim.flee_success_rate = flee_success_rate
    test_case = test_num
    success = 0
    for i in range(test_case):

        flee_success = anim.is_flee_successful()
        # print(hunt_sucess)
        if (flee_success):
            success += 1

    print(f'Flee success rate: {success / test_case}')


def test_has_starved(starvation_time):
    anim = Animal()
    anim.starvation_time = starvation_time
    if anim.has_starved():
        print('Animal starved to death')
    else:
        print('Animal is not starving')


# test_is_hunt_successful(0.8, 1000)
# test_is_hunt_successful(0.1, 1000)
# test_is_flee_successful(0.3, 1000)
# test_is_flee_successful(1, 1000)
# test_has_starved(0)
# test_has_starved(1)
# test_has_starved(-1)