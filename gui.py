import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Prey and Predator Simulation")
        self.geometry("1280x720")

        # Create frames
        self.grid_frame = ttk.Frame(self, width=640, height=420)
        self.grid_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.params_frame = ttk.Frame(self, width=640, height=420)
        self.params_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.graph_frame = ttk.Frame(self, width=1280, height=300)
        self.graph_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_grid()
        self.create_params()
        self.create_graph()

    def create_grid(self):
        # Create a label for the grid
        label = ttk.Label(self.grid_frame, text="Simulation Grid")
        label.pack()

        # Create a canvas to draw the grid with padding for the border
        canvas_width = 500
        canvas_height = 400
        border_width = 2  # Adjust border width as needed
        self.canvas = tk.Canvas(self.grid_frame, width=canvas_width + 2 * border_width,
                                height=canvas_height + 2 * border_width, highlightthickness=0)
        self.canvas.pack(padx=border_width, pady=border_width)

        # Define the dimensions of the grid
        grid_width = canvas_width // 20
        grid_height = canvas_height // 20

        # Draw grid lines
        for i in range(21):
            x = i * grid_width
            self.canvas.create_line(x, 0, x, canvas_height, fill="gray")
            y = i * grid_height
            self.canvas.create_line(0, y, canvas_width, y, fill="gray")

        # Create rectangles for each grid cell (optional)
        # This is just a visual representation and can be adapted for your simulation
        self.rectangles = []
        for i in range(20):
            row = []
            for j in range(20):
                x1, y1 = j * grid_width, i * grid_height
                x2, y2 = x1 + grid_width, y1 + grid_height
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
                row.append(rect)
            self.rectangles.append(row)
        
        # Example: Modify a rectangle (fill with a different color)
        # self.canvas.itemconfig(self.rectangles[0][0], fill="blue")

    def create_params(self):
        # Prey Parameters
        prey_frame = ttk.LabelFrame(self.params_frame, text="Prey Parameters")
        prey_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(prey_frame, text="Initial Population:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.prey_initial_population = tk.IntVar(value=50)
        prey_pop_slider = ttk.Scale(prey_frame, variable=self.prey_initial_population, from_=10, to=100, orient=tk.HORIZONTAL)
        prey_pop_slider.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.prey_initial_population_label = ttk.Label(prey_frame, text=self.prey_initial_population.get())
        self.prey_initial_population_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        prey_pop_slider.bind("<Motion>", lambda e: self.prey_initial_population_label.config(text=f'{self.prey_initial_population.get()}'))

        ttk.Label(prey_frame, text="Flee Success Rate:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.flee_success = tk.DoubleVar(value=0.5)
        flee_success_slider = ttk.Scale(prey_frame, variable=self.flee_success, from_=0, to=1, orient=tk.HORIZONTAL)
        flee_success_slider.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.flee_success_label = ttk.Label(prey_frame, text=f'{self.flee_success.get():.2f}')
        self.flee_success_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        flee_success_slider.bind("<Motion>", lambda e: self.flee_success_label.config(text=f'{self.flee_success.get():.2f}'))

        ttk.Label(prey_frame, text="Birth Rate:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.prey_birth_rate = tk.DoubleVar(value=0.1)
        prey_birth_rate_slider = ttk.Scale(prey_frame, variable=self.prey_birth_rate, from_=0, to=1, orient=tk.HORIZONTAL)
        prey_birth_rate_slider.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.prey_birth_rate_label = ttk.Label(prey_frame, text=f'{self.prey_birth_rate.get():.2f}')
        self.prey_birth_rate_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        prey_birth_rate_slider.bind("<Motion>", lambda e: self.prey_birth_rate_label.config(text=f'{self.prey_birth_rate.get():.2f}'))

        # Predator Parameters
        predator_frame = ttk.LabelFrame(self.params_frame, text="Predator Parameters")
        predator_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(predator_frame, text="Initial Population:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.predator_initial_population = tk.IntVar(value=20)
        predator_pop_slider = ttk.Scale(predator_frame, variable=self.predator_initial_population, from_=10, to=100, orient=tk.HORIZONTAL)
        predator_pop_slider.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.predator_initial_population_label = ttk.Label(predator_frame, text=self.predator_initial_population.get())
        self.predator_initial_population_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        predator_pop_slider.bind("<Motion>", lambda e: self.predator_initial_population_label.config(text=f'{self.predator_initial_population.get()}'))

        ttk.Label(predator_frame, text="Hunt Success Rate:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.hunt_success = tk.DoubleVar(value=0.5)
        hunt_success_slider = ttk.Scale(predator_frame, variable=self.hunt_success, from_=0, to=1, orient=tk.HORIZONTAL)
        hunt_success_slider.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.hunt_success_label = ttk.Label(predator_frame, text=f'{self.hunt_success.get():.2f}')
        self.hunt_success_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        hunt_success_slider.bind("<Motion>", lambda e: self.hunt_success_label.config(text=f'{self.hunt_success.get():.2f}'))

        ttk.Label(predator_frame, text="Birth Rate:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.predator_birth_rate = tk.DoubleVar(value=0.1)
        predator_birth_rate_slider = ttk.Scale(predator_frame, variable=self.predator_birth_rate, from_=0, to=1, orient=tk.HORIZONTAL)
        predator_birth_rate_slider.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.predator_birth_rate_label = ttk.Label(predator_frame, text=f'{self.predator_birth_rate.get():.2f}')
        self.predator_birth_rate_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        predator_birth_rate_slider.bind("<Motion>", lambda e: self.predator_birth_rate_label.config(text=f'{self.predator_birth_rate.get():.2f}'))

        ttk.Label(predator_frame, text="Starvation Time:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.starvation_time = tk.IntVar(value=5)
        starvation_time_slider = ttk.Scale(predator_frame, variable=self.starvation_time, from_=1, to=10, orient=tk.HORIZONTAL)
        starvation_time_slider.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
        self.starvation_time_label = ttk.Label(predator_frame, text=self.starvation_time.get())
        self.starvation_time_label.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        starvation_time_slider.bind("<Motion>", lambda e: self.starvation_time_label.config(text=f'{self.starvation_time.get()}'))

        self.run_button = ttk.Button(self.params_frame, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Ensure the sections resize correctly
        self.params_frame.grid_rowconfigure(0, weight=1)
        self.params_frame.grid_rowconfigure(1, weight=1)
        self.params_frame.grid_rowconfigure(2, weight=1)
        self.params_frame.grid_columnconfigure(0, weight=1)

    def create_graph(self):
        self.figure = Figure(figsize=(10, 4), dpi=100)
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
