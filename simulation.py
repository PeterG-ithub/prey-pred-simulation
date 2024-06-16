from animal import Animal


class Simulation:
    def __init__(self) -> None:
        self.initial_prey_count = 0
        self.initial_predator_count = 0
        self.prey_birth_rate = 0.0
        self.prey_flee_success_rate = 0.0
        self.predator_birth_rate = 0.0
        self.predator_hunt_success_rate = 0.0
        self.predator_starvation_time = 0
        self.create_simulation()
        self.preys = []
        self.predators = []

    def create_simulation(self):
        for _ in range(self.initial_prey_count):
            anim = Animal('prey')
            anim.flee_success_rate = self.prey_flee_success_rate
            self.preys.append(anim)

        for _ in range(self.initial_predator_count):
            anim = Animal('predator')
            anim.hunt_success_rate = self.predator_hunt_success_rate
            anim.starvation_time = self.predator_starvation_time
            self.predators.append(anim)

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

# test_create_simulation(100, 10)
test_simulate_one_time_step(100, 10)