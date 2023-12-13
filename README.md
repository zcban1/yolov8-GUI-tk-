# YOLO Training GUI

This Python script provides a graphical user interface (GUI) for training YOLO (You Only Look Once) models using the Ultralytics YOLO library. The GUI is built using the Tkinter library.

## Usage
1. Run the script by executing the `main` block.
2. The GUI will appear with various input fields and options for configuring YOLO training.
3. Fill in the required information, such as selecting the YOLO model, specifying the YAML file, and setting training parameters.
4. Click the "Train Model" button to start the training process.
5. Optionally, you can resume training by providing a pre-trained model checkpoint (last.pt) using the "Resume Training" section.

## GUI Components

### YOLO Model Selection
- Choose the YOLO model architecture from the dropdown menu.

### YAML File Selection
- Use the "Browse" button to select the YAML file containing dataset and training configurations.

### Training Parameters
- Set parameters such as image size, batch size, number of epochs, caching, Automatic Mixed Precision (AMP), validation, and save period.

### Training Actions
- Click "Train Model" to initiate training with the specified configurations.
- Click "Browse for last.pt" to select a pre-trained model checkpoint for resuming training.
- Click "Resume Training" to continue training from the specified checkpoint.

## Note
- Ensure you have the required dependencies, including Tkinter and Ultralytics, installed.
- Monitor the console for training progress and results.

Feel free to contribute, report issues, or provide feedback!
