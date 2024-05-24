## Singa (Sign Language Recognition)

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

    - After the first activation, you should install the requirement for this project

    ```
    py pip install -r requirements.txt
    ```

### Downloading the Dataset

  - Execute the dataset script to download the required dataset from Kaggle.

    ```sh
    ./script/dataset
    ```

### Running TensorBoard

  - Use the following command to start TensorBoard and visualize the training logs.

    ```sh
    tensorboard --logdir=./logs/train_log_directory
    ```

    - Replace `train_log_directory` with the actual name of the directory where your log files are stored.

### Recoding you own dataset

   - If you want to add your own dataset, you can read this documentation here [coming soon]()

### Additional Notes:

- Ensure you have the [Kaggle API](https://github.com/Kaggle/kaggle-api) installed (`The kaggle-api should be already installed using pip install`).
- The scripts assume that you have the necessary permissions to execute them. If you encounter permission issues, you may need to adjust the permissions using `chmod +x ./scripts/script_name`.
- The logs directory should contain the TensorFlow event files generated during model training, which TensorBoard uses for visualization.
