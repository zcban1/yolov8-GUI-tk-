import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO

class YOLOTrainingGUI:
    def __init__(self, master):
        self.master = master
        master.title("YOLO Training GUI")

        self.model_options = ['yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x']
        self.selected_model = tk.StringVar(value=self.model_options[0])

        self.create_model_dropdown("Select YOLO Model:", "model_selection", self.model_options)

        self.create_entry("Select YAML File:", "yaml_path", 50)
        self.create_button("Browse", self.browse_yaml)

        self.create_entry("Image Size (imgsz):", "imgsz", 10, default_value="320")
        self.create_entry("Batch Size (batch):", "batch", 10, default_value="-1")
        self.create_entry("Epochs:", "epochs", 10, default_value="300")
        self.create_entry("Cache:", "cache", 10, default_value="False")
        self.create_entry("AMP:", "amp", 10, default_value="False")
        self.create_entry("Validation:", "val", 10, default_value="False")
        self.create_entry("Save Period:", "save_period", 10, default_value="-1")

        self.create_button("Train Model", self.train_model)

        self.create_entry("Resume last.pt:", "resume_lastpt_path", 50)
        self.create_button("Browse for last.pt", self.browse_resume_lastpt)
        self.create_button("Resume Training", self.resume_training)

    def create_model_dropdown(self, label_text, var_name, options):
        label = tk.Label(self.master, text=label_text)
        label.pack()

        dropdown = tk.OptionMenu(self.master, self.selected_model, *options)
        dropdown.pack()

    def create_entry(self, label_text, var_name, width, default_value=""):
        label = tk.Label(self.master, text=label_text)
        label.pack()

        variable = tk.StringVar()
        variable.set(default_value)
        entry = tk.Entry(self.master, textvariable=variable, width=width)
        entry.pack()

        setattr(self, var_name.replace(" ", "_"), variable)  # Replace space with underscore

    def create_button(self, button_text, command):
        button = tk.Button(self.master, text=button_text, command=command)
        button.pack()

    def browse_yaml(self):
        file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml")])
        if file_path:
            self.yaml_path.set(file_path)

    def train_model(self):
        yaml_path = self.yaml_path.get()
        if yaml_path:
            selected_model = self.selected_model.get()
            imgsz = int(self.imgsz.get())
            batch = int(self.batch.get())
            epochs = int(self.epochs.get())
            cache = self.cache.get().capitalize() == 'True'
            amp = self.amp.get().capitalize() == 'False'
            val = self.val.get().capitalize() == 'True'
            save_period = int(self.save_period.get())

            model_path = f"{selected_model}.pt"
            self.model = YOLO(model_path)

            results = self.model.train(data=yaml_path, epochs=epochs, batch=batch, imgsz=imgsz,
                                       cache=cache, amp=amp, val=val, save_period=save_period)
            print("Training results:", results)
        else:
            print("Please select a YAML file.")

    def browse_resume_lastpt(self):
        file_path = filedialog.askopenfilename(filetypes=[("LAST.PT", "*.pt")])
        if file_path:
            self.resume_lastpt_path.set(file_path)

    def resume_training(self):
        resume_lastpt_path = self.resume_lastpt_path.get()
        if resume_lastpt_path:
            selected_model = self.selected_model.get()

            model_path = f"{selected_model}.pt"
            self.model = YOLO(model_path)

            results = self.model.train(resume=True, data=resume_lastpt_path)
            print("Resume Training results:", results)
        else:
            print("Please select a last.pt file for resume training.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = YOLOTrainingGUI(root)
    root.mainloop()

