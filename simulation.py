from animal import Animal
import math

class Simulation:
    def __init__(self) -> None:
        self.initial_prey_count = 0
        self.initial_predator_count = 0
        self.prey_birth_rate = 0.0
        self.prey_flee_success_rate = 0.0
        self.prey_population = self.initial_prey_count
        self.predator_birth_rate = 0.0
        self.predator_hunt_success_rate = 0.0
        self.predator_starvation_time = 0
        self.predator_population = self.initial_predator_count
        self.preys = []
        self.predators = []
        self.create_simulation()

    def create_simulation(self):
        prey_num = self.initial_prey_count
        self.create_prey(prey_num)

        predator_num = self.initial_predator_count
        self.create_predator(predator_num)

        self.prey_population = self.initial_prey_count
        self.predator_population = self.initial_predator_count

    def simulate_one_time_step(self):
        predator_index = 0
        prey_index_list = []  # List of all the hunted preys
        for prey_index in range(len(self.preys)):
            if predator_index > len(self.predators) - 1:
                predator_index = 0
            if self.predators[predator_index].is_hunt_successful():
                prey_index_list.append(prey_index)
                self.predators[predator_index].starvation_time = 5
            else:
                self.predators[predator_index].starvation_time -= 1

        # Remove the hunted preys
        prey_index_list.reverse()
        for index in prey_index_list:
            self.preys.pop(index)

        # Update Population
        self.prey_population = len(self.preys)
        self.predator_population = len(self.predators)

    def create_prey(self, prey_num):
        for _ in range(prey_num):
            anim = Animal('prey')
            anim.flee_success_rate = self.prey_flee_success_rate
            self.preys.append(anim)

    def create_predator(self, predator_num):
        for _ in range(predator_num):
            anim = Animal('predator')
            anim.hunt_success_rate = self.predator_hunt_success_rate
            anim.starvation_time = self.predator_starvation_time
            self.predators.append(anim)

def test_create_simulation(prey_count, predator_count):
    sim = Simulation()
    sim.initial_predator_count = predator_count
    sim.initial_prey_count = prey_count
    sim.create_simulation()
    print(f'Prey count: {len(sim.preys)}')
    print(f'Predator count: {len(sim.predators)}')


def test_simulate_one_time_step(prey_count, predator_count):
    sim = Simulation()
    sim.initial_predator_count = predator_count
    sim.initial_prey_count = prey_count
    sim.predator_hunt_success_rate = 0.5
    sim.predator_starvation_time = 5
    sim.create_simulation()

    print(f'Prey count before hunt: {len(sim.preys)}')
    print(f'Starvation time before hunt of one of the predator: {sim.predators[0].starvation_time}')
    sim.simulate_one_time_step()
    print(f'Prey count after hunt: {len(sim.preys)}')
    print(f'Starvation time after hunt of the same predator: {sim.predators[0].starvation_time}')

test_create_simulation(100, 10)
# test_simulate_one_time_step(100, 10)