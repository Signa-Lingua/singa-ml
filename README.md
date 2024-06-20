# Singa (Sign Language Recognition)

Singa is a project focused on sign language recognition using deep learning techniques. This README provides instructions on setting up the virtual environment, downloading datasets, running TensorBoard, and recording your own dataset.

### Setting up the Virtual Environment

1. **Initialize the Virtual Environment:**

   - Run the setup script to create and configure the virtual environment.

   ```sh
   ./script/setup
   ```

2. **Activate the Virtual Environment:**

   - Use the activation script to start the virtual environment.

   ```sh
   ./script/activate
   ```

   - After activating the virtual environment for the first time, install the project requirements:

   ```
   pip install -r requirements.txt
   ```

### Downloading the Dataset

- Execute the dataset script to download the required dataset from our [dataset in Kaggle](https://www.kaggle.com/datasets/jirenmaa/asl-npy-20-action-60fps-225feature-no-augment).

  ```sh
  ./script/dataset
  ```

### Running TensorBoard

- Use the following command to start TensorBoard and visualize the training logs.

  ```sh
  tensorboard --logdir=./logs/train_log_directory
  ```

  - Replace `train_log_directory` with the actual name of the directory where your log files are stored.

### Recording your own dataset

- If you want to add your own dataset, refer to the detailed instructions in [RECORDING-DATASET.md](./tutorial/RECORDING-DATASET.md).

### Additional Notes:

- Ensure you have the Kaggle API installed. The Kaggle API should already be installed via pip:

  ```sh
  pip install kaggle
  ```

- The scripts assume that you have the necessary permissions to execute them. If you encounter permission issues, you may need to adjust the permissions using:

  ```sh
  chmod +x ./script/script_name
  ```

- The logs directory should contain the TensorFlow event files generated during model training, which TensorBoard uses for visualization.

By following these instructions, you can set up your environment, download the necessary datasets, monitor your model training, and record custom datasets for improving the sign language recognition model. For further details on dataset recording, refer to the RECORD_DATASET.md file.
