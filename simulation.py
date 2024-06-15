from animal import Animal


class Simulation:
    def __init__(self) -> None:
        self.initial_prey_count = 0
        self.initial_predator_count = 0
        self.prey_birth_rate = 0.0
        self.predator_birth_rate = 0.0
        self.create_simulation()
        self.preys = []
        self.predators = []

    def create_simulation(self):
        for _ in range(self.initial_prey_count):
            anim = Animal('prey')
            self.preys.append(anim)

        for _ in range(self.initial_predator_count):
            anim = Animal('predator')
            self.predators.append(anim)


def test_create_simulation(prey_count, predator_count):
    sim = Simulation()
    sim.initial_predator_count = prey_count
    sim.initial_prey_count = predator_count
    sim.create_simulation()
    print(f'Prey count: {len(sim.preys)}')
    print(f'Predator count: {len(sim.predators)}')


test_create_simulation(100, 10)