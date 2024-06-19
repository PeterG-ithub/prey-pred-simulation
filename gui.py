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

    def create_param_section(self, parent, title, params):
        frame = ttk.LabelFrame(parent, text=title)
        frame.grid(padx=10, pady=10, sticky="nsew")

        for i, (label_text, settings) in enumerate(params.items()):
            var, from_, to, var_type = settings
            row, col = divmod(i, 4)  # Arrange in two columns
            ttk.Label(frame, text=label_text).grid(row=row*2, column=col*2, padx=5, pady=5, sticky="w")

            if var_type == 'int':
                var_instance = tk.IntVar(value=var)
            elif var_type == 'double':
                var_instance = tk.DoubleVar(value=var)
            else:
                raise ValueError(f"Unsupported var_type: {var_type}")

            scale = ttk.Scale(frame, variable=var_instance, from_=from_, to=to, orient=tk.HORIZONTAL)
            scale.grid(row=row*2+1, column=col*2, padx=5, pady=5, sticky="ew")
            label = ttk.Label(frame, text=f'{var_instance.get():.2f}' if var_type == 'double' else f'{var_instance.get()}')
            label.grid(row=row*2+1, column=col*2+1, padx=5, pady=5, sticky="w")

            def update_label(event, var_instance=var_instance, label=label, var_type=var_type):
                value = var_instance.get()
                formatted_value = f'{value:.2f}' if var_type == 'double' else f'{value}'
                label.config(text=formatted_value)

            scale.bind("<Motion>", update_label)

        return frame
    def create_params(self):
        # Simulation Parameters
        simulation_params = {
            "Simulation Time (days):": [100, 10, 365, 'int'],
        }
        simulation_frame = self.create_param_section(self.params_frame, "Simulation Parameters", simulation_params)
        simulation_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Resource Parameters
        resource_params = {
            "Resource Growth Rate:": [0.1, 0, 1, 'double'],
            "Resource Carrying Capacity:": [500, 100, 999, 'int'],
        }
        resource_frame = self.create_param_section(self.params_frame, "Resource Parameters", resource_params)
        resource_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Prey Parameters
        prey_params = {
            "Initial Population:": [50, 10, 100, 'int'],
            "Flee Success Rate:": [0.5, 0, 1, 'double'],
            "Birth Rate:": [0.1, 0, 1, 'double'],
        }
        prey_frame = self.create_param_section(self.params_frame, "Prey Parameters", prey_params)
        prey_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Predator Parameters
        predator_params = {
            "Initial Population:": [20, 10, 100, 'int'],
            "Hunt Success Rate:": [0.5, 0, 1, 'double'],
            "Birth Rate:": [0.1, 0, 1, 'double'],
            "Starvation Time:": [5, 1, 10, 'int'],
        }
        predator_frame = self.create_param_section(self.params_frame, "Predator Parameters", predator_params)
        predator_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.run_button = ttk.Button(self.params_frame, text="Run Simulation", command=self.run_simulation)
        self.run_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # Ensure the sections resize correctly
        for i in range(5):
            self.params_frame.grid_rowconfigure(i, weight=1)
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
