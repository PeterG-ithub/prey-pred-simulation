import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SimulationGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Prey and Predator Simulation")
        self.geometry("1280x720")

        # Create frames
        self.grid_frame = ttk.Frame(self, width=640, height=520)
        self.grid_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.params_frame = ttk.Frame(self, width=640, height=520)
        self.params_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.graph_frame = ttk.Frame(self, width=1280, height=200)
        self.graph_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_grid()
        self.create_params()
        self.create_graph()

    def create_grid(self):
        # Placeholder for the grid
        label = ttk.Label(self.grid_frame, text="Simulation Grid")
        label.pack()

    def create_params(self):
        # Prey Parameters
        prey_frame = ttk.LabelFrame(self.params_frame, text="Prey Parameters")
        prey_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(prey_frame, text="Flee Success Rate").grid(row=0, column=0, padx=5, pady=5)
        self.flee_success = tk.DoubleVar(value=0.5)
        ttk.Entry(prey_frame, textvariable=self.flee_success).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(prey_frame, text="Birth Rate").grid(row=1, column=0, padx=5, pady=5)
        self.birth_rate = tk.DoubleVar(value=0.1)
        ttk.Entry(prey_frame, textvariable=self.birth_rate).grid(row=1, column=1, padx=5, pady=5)

        # Predator Parameters
        predator_frame = ttk.LabelFrame(self.params_frame, text="Predator Parameters")
        predator_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(predator_frame, text="Hunt Success Rate").grid(row=0, column=0, padx=5, pady=5)
        self.hunt_success = tk.DoubleVar(value=0.5)
        ttk.Entry(predator_frame, textvariable=self.hunt_success).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(predator_frame, text="Starvation Time").grid(row=1, column=0, padx=5, pady=5)
        self.starvation_time = tk.IntVar(value=5)
        ttk.Entry(predator_frame, textvariable=self.starvation_time).grid(row=1, column=1, padx=5, pady=5)

        self.run_button = ttk.Button(self.params_frame, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Ensure the sections resize correctly
        self.params_frame.grid_rowconfigure(0, weight=1)
        self.params_frame.grid_rowconfigure(1, weight=1)
        self.params_frame.grid_columnconfigure(0, weight=1)

    def create_graph(self):
        self.figure = Figure(figsize=(10, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Population Over Time")
        self.ax.set_xlabel("Time Steps")
        self.ax.set_ylabel("Population")
        self.figure.tight_layout(pad=3.0)

        self.canvas = FigureCanvasTkAgg(self.figure, self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def run_simulation(self):
        pass


if __name__ == "__main__":
    app = SimulationGUI()
    app.mainloop()
