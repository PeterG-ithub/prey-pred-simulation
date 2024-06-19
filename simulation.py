from animal import Animal
from producer import Producer
import math

class Simulation:
    def __init__(self) -> None:
        self.initial_prey_count = 0
        self.initial_predator_count = 0
        self.prey_birth_rate = 0.0
        self.prey_flee_success_rate = 0.0
        self.prey_starvation_time = 0
        self.prey_population = self.initial_prey_count
        self.prey_max_population = 1000
        self.predator_birth_rate = 0.0
        self.predator_hunt_success_rate = 0.0
        self.predator_starvation_time = 0
        self.predator_population = self.initial_predator_count
        self.preys = []
        self.predators = []
        self.resource: Producer

    def simulate_one_time_step(self, time_step_num=0):
        # print(f'{time_step_num}') debugging
        prey_index_list = []  # List of all the preys that died
        predator_index_list = []  # List of all the predator that died

        self.simulate_grass_growing()
        self.simulate_prey_eating()
        prey_index_list = self.check_prey_starvation()
        prey_index_list += self.simulate_predator_eating()
        predator_index_list = self.check_predator_starvation()

        prey_index_list = list(dict.fromkeys(prey_index_list))  # Remove duplicate

        # Simulate Death
        self.simulate_death(prey_index_list, predator_index_list)

        # Simulate Birth
        self.simulate_birth()

    def create_simulation(self):
        prey_num = self.initial_prey_count
        self.create_prey(prey_num)

        predator_num = self.initial_predator_count
        self.create_predator(predator_num)

        self.prey_population = self.initial_prey_count
        self.predator_population = self.initial_predator_count

    def create_prey(self, prey_num):
        for _ in range(prey_num):
            anim = Animal('prey')
            anim.flee_success_rate = self.prey_flee_success_rate
            anim.starvation_time = self.prey_starvation_time
            self.preys.append(anim)

        self.prey_population = len(self.preys)

    def create_predator(self, predator_num):
        for _ in range(predator_num):
            anim = Animal('predator')
            anim.hunt_success_rate = self.predator_hunt_success_rate
            anim.starvation_time = self.predator_starvation_time
            self.predators.append(anim)

        self.predator_population = len(self.predators)

    def create_resource(self, num, growth_rate, max):
        grass = Producer()
        grass.grass_amount = num
        grass.grass_growth_rate = growth_rate
        grass.max_grass_amount = max
        self.resource = grass

    def simulate_birth(self):
        new_prey_num = math.ceil(self.prey_population * self.prey_birth_rate)
        self.create_prey(new_prey_num)

        new_predator_num = math.ceil(self.predator_population * self.predator_birth_rate)
        print(f'New predator num: {new_predator_num}')
        self.create_predator(new_predator_num)

        self.update_population()

    def simulate_death(self, prey_list=[], predator_list=[]):
        if prey_list:
            self.simulate_prey_death(prey_list)
        if predator_list:
            self.simulate_predator_death(predator_list)
        self.update_population()

    def simulate_prey_death(self, prey_list):
        prey_list.reverse()
        for index in prey_list:
            self.preys.pop(index)

    def simulate_predator_death(self, predator_list):
        predator_list.reverse()
        print(f"Predator that died: {len(predator_list)}")
        for index in predator_list:
            self.predators.pop(index)

    def simulate_prey_eating(self):
        total_grass_needed = len(self.preys)
        for preys in self.preys:
            if total_grass_needed > 0 and self.resource.grass_amount > 0:
                preys.starvation_time = 3
                self.resource.grass_amount -= 1
                total_grass_needed -= 1
            else:
                preys.starvation_time -= 1

    def simulate_predator_eating(self):
        total_prey = 10
        prey_list = []
        for index, pred in enumerate(self.predators):
            if pred.is_hunt_successful() and index < total_prey:
                prey_list.append(index)
                pred.starvation_time = 2
            else:
                pred.starvation_time -= 1
        return prey_list

    def simulate_grass_growing(self):
        new_grass_amount = self.resource.grass_amount
        if new_grass_amount < 1:
            new_grass_amount = 1
        new_grass_amount += new_grass_amount * self.resource.grass_growth_rate
        if new_grass_amount > self.resource.max_grass_amount:
            new_grass_amount = self.resource.max_grass_amount
        self.resource.grass_amount = new_grass_amount

    def check_prey_starvation(self):
        prey_list = []
        for index, prey in enumerate(self.preys):
            if prey.has_starved():
                prey_list.append(index)
        return prey_list

    def check_predator_starvation(self):
        predator_list = []
        for index, pred in enumerate(self.predators):
            if pred.has_starved():
                predator_list.append(index)
        return predator_list

    def update_population(self):
        self.prey_population = len(self.preys)
        self.predator_population = len(self.predators)


def run_simulation(sim_data):
    sim = Simulation()
    sim.initial_prey_count = sim_data['prey_initial_population']
    sim.initial_predator_count = sim_data['predator_initial_population']
    sim.predator_hunt_success_rate = sim_data['hunt_success']
    sim.predator_starvation_time = sim_data['starvation_time']
    sim.prey_birth_rate = sim_data['prey_birth_rate']
    sim.predator_birth_rate = sim_data['predator_birth_rate']
    sim.prey_starvation_time = sim_data['prey_starvation_time']
    sim.create_simulation()
    grass_amount = sim_data['resource_num']
    grass_growth_rate = sim_data['resource_growth_rate']
    grass_max = sim_data['resource_max']
    sim.create_resource(grass_amount, grass_growth_rate, grass_max)
    prey_population = []
    predator_population = []
    time_step = sim_data['time_step']

    prey_population.append(sim.prey_population)
    predator_population.append(sim.predator_population)

    for i in range(time_step):
        sim.simulate_one_time_step(i)
        prey_population.append(sim.prey_population)
        predator_population.append(sim.predator_population)
        print(f'Prey pop: {prey_population}')
        print(f'Predator pop: {predator_population}')

    return time_step, prey_population, predator_population


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
    sim.predator_hunt_success_rate = 0.9
    sim.predator_starvation_time = 5
    sim.prey_birth_rate = 0.3
    sim.predator_birth_rate = 0.1
    sim.prey_starvation_time = 3
    sim.create_simulation()

    print('Before:')
    print(f'Prey population before birth: {sim.prey_population}')
    print(f'Predator population before birth: {sim.predator_population}')
    print(f'Prey count before hunt: {len(sim.preys)}')
    if sim.predators:
        print(f'Starvation time before hunt of one of the predator: {sim.predators[0].starvation_time}')
    sim.simulate_one_time_step()
    print('1 After:')
    print(f'Prey population after birth: {sim.prey_population}')
    print(f'Predator population after birth: {sim.predator_population}')
    print(f'Prey count after hunt: {len(sim.preys)}')
    if sim.predators:
        print(f'Starvation time after hunt of the same predator: {sim.predators[0].starvation_time}')
    sim.simulate_one_time_step()
    print('2 After:')
    print(f'Prey population after birth: {sim.prey_population}')
    print(f'Predator population after birth: {sim.predator_population}')
    print(f'Prey count after hunt: {len(sim.preys)}')
    if sim.predators:
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


def test_run_simulation():
    sim_data = {
        'prey_initial_population': 50,
        'prey_birth_rate': .3,
        'flee_success': 0.0,
        'predator_initial_population': 1,
        'predator_birth_rate': .1,
        'hunt_success': .5,
        'starvation_time': 5,
        'prey_starvation_time': 3,
        'time_step': 200,
        'resource_num': 1000,
        'resource_growth_rate': 100,
        'resource_max': 2000,
    }
    timestep, prey_pop, predator_pop = run_simulation(sim_data)

    print(f'Timestep: {timestep}')
    print(f'Population Length - Prey: {len(prey_pop)} - Predator: {len(predator_pop)}')
    print(f'Prey Population: {prey_pop}')
    print(f'Predator Population: {predator_pop}')


def test_resource_creation():
    sim = Simulation()
    sim.create_resource(1000, 10, 1000)
    print(f'Resource amount: {sim.resource.grass_amount}')

# test_create_simulation(100, 10)
# test_simulate_one_time_step(50, 0)
# test_simulate_birth(100, 10)
test_run_simulation()
# test_resource_creation()