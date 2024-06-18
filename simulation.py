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

    def simulate_one_time_step(self, time_step_num):
        print(f'{time_step_num}')
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

        # Simulate Birth
        self.simulate_birth()

    def create_prey(self, prey_num):
        for _ in range(prey_num):
            anim = Animal('prey')
            anim.flee_success_rate = self.prey_flee_success_rate
            self.preys.append(anim)

        self.prey_population = len(self.preys)

    def create_predator(self, predator_num):
        for _ in range(predator_num):
            anim = Animal('predator')
            anim.hunt_success_rate = self.predator_hunt_success_rate
            anim.starvation_time = self.predator_starvation_time
            self.predators.append(anim)

        self.predator_population = len(self.predators)

    def simulate_birth(self):
        new_prey_num = math.ceil(self.prey_population * self.prey_birth_rate)
        self.create_prey(new_prey_num)

        new_predator_num = math.ceil(self.predator_population * self.predator_birth_rate)
        self.create_predator(new_predator_num)


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
    sim.prey_birth_rate = 0.3
    sim.predator_birth_rate = 0.1
    sim.create_simulation()

    print('Before:')
    print(f'Prey population before birth: {sim.prey_population}')
    print(f'Predator population before birth: {sim.predator_population}')
    print(f'Prey count before hunt: {len(sim.preys)}')
    print(f'Starvation time before hunt of one of the predator: {sim.predators[0].starvation_time}')
    sim.simulate_one_time_step()
    print('After:')
    print(f'Prey population after birth: {sim.prey_population}')
    print(f'Predator population after birth: {sim.predator_population}')
    print(f'Prey count after hunt: {len(sim.preys)}')
    print(f'Starvation time after hunt of the same predator: {sim.predators[0].starvation_time}')


def test_simulate_birth(prey_count, predator_count):
    sim = Simulation()
    sim.initial_predator_count = predator_count
    sim.initial_prey_count = prey_count
    sim.prey_birth_rate = 0.3
    sim.predator_birth_rate = 0.1
    sim.create_simulation()

    print(f'Prey population before birth: {sim.prey_population}')
    print(f'Predator population before birth: {sim.predator_population}')
    sim.simulate_birth()
    print(f'Prey population after birth: {sim.prey_population}')
    print(f'Predator population after birth: {sim.predator_population}')


def run_simulation(sim_data):
    sim = Simulation()
    sim.initial_prey_count = sim_data['prey_initial_population']
    sim.initial_predator_count = sim_data['predator_initial_population']
    sim.predator_hunt_success_rate = sim_data['hunt_success']
    sim.predator_starvation_time = sim_data['starvation_time']
    sim.prey_birth_rate = sim_data['prey_birth_rate']
    sim.predator_birth_rate = sim_data['predator_birth_rate']
    sim.create_simulation()

    prey_population = []
    predator_population = []
    time_step = 50

    prey_population.append(sim.prey_population)
    predator_population.append(sim.predator_population)

    for i in range(time_step):
        sim.simulate_one_time_step(i)
        prey_population.append(sim.prey_population)
        predator_population.append(sim.predator_population)

    return time_step, prey_population, predator_population


def test_run_simulation():
    sim_data = {
        'prey_initial_population': 100,
        'prey_birth_rate': .3,
        'flee_success': 0.0,
        'predator_initial_population': 10,
        'predator_birth_rate': .3,
        'hunt_success': .5,
        'starvation_time': 5
    }
    timestep, prey_pop, predator_pop = run_simulation(sim_data)

    print(f'Timestep: {timestep}')
    print(f'Population Length - Prey: {len(prey_pop)} - Predator: {len(predator_pop)}')
    print(f'Prey Population: {prey_pop}')
    print(f'Predator Population: {predator_pop}')


# test_create_simulation(100, 10)
# test_simulate_one_time_step(100, 10)
# test_simulate_birth(100, 10)
test_run_simulation()