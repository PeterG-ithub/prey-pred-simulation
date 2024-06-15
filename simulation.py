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

    def create_simulatoin(self):
        for i in range(self.initial_prey_count):
            anim = Animal('prey')
            self.preys.append(anim)

        for i in range(self.initial_predator_count):
            anim = Animal('predator')
            self.predators.append(anim)