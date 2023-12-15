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
- Set parameters
- Configuration

| Key                | Value      | Description                                                                                         |
| ------------------ | ---------- | --------------------------------------------------------------------------------------------------- |
| model              | None       | Path to the model file, e.g., yolov8n.pt, yolov8n.yaml                                               |
| data               | None       | Path to the data file, e.g., coco128.yaml                                                           |
| epochs             | 100        | Number of epochs to train for                                                                       |
| patience           | 50         | Epochs to wait for no observable improvement for early stopping of training                        |
| batch              | 16         | Number of images per batch (-1 for AutoBatch)                                                      |
| imgsz              | 640        | Size of input images as an integer                                                                  |
| save               | True       | Save train checkpoints and predict results                                                         |
| save_period        | -1         | Save checkpoint every x epochs (disabled if < 1)                                                  |
| cache              | False      | True/ram, disk, or False. Use cache for data loading                                                |
| device             | None       | Device to run on, e.g., cuda device=0 or device=0,1,2,3 or device=cpu                              |
| workers            | 8          | Number of worker threads for data loading (per RANK if DDP)                                          |
| project            | None       | Project name                                                                                        |
| single_cls         | False      | Train multi-class data as single-class                                                            |
| ... (other keys)   | ...        | ...

### Training Actions
- Click "Train Model" to initiate training with the specified configurations.
- Click "Browse for last.pt" to select a pre-trained model checkpoint for resuming training.
- Click "Resume Training" to continue training from the specified checkpoint.

## Note
- Ensure you have the required dependencies, including Tkinter and Ultralytics, installed.
- Monitor the console for training progress and results.

Feel free to contribute, report issues, or provide feedback!
