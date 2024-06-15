from animal import Animal


class Simulation:
    def __init__(self) -> None:
        self.create_simulation()
        self.initial_prey_count = 0
        self.initial_predator_count = 0
        self.prey_birth_rate = 0.0
        self.predator_birth_rate = 0.0