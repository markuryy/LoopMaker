# LoopMaker

LoopMaker is a Python application designed to automatically identify and create looping segments from video files. It utilizes deep learning models to extract features from video frames and identifies segments with high similarity to create seamless loops. This tool is perfect for creating engaging video loops for social media, art projects, and more.

## Features

- Video feature extraction using pre-trained deep learning models.
- Automatic identification of potential looping points in a video.
- Export loops as MP4 or GIF files.
- Easy setup and execution on any machine with Python and CUDA GPU support.

## Installation

This guide assumes you have Git, Python, and a CUDA-compatible GPU setup on your machine.

### Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/markuryy/LoopMaker.git
cd LoopMaker
```

### Install Dependencies

Run the `install.bat` file to set up a virtual environment and install all required dependencies. Right-click on `install.bat` and select "Run as administrator" or run it via command prompt:

```bash
install.bat
```

This script will create a virtual environment named `venv` and install the necessary Python packages listed in `requirements.txt`.

## Usage

After installation, you can start LoopMaker by running the `start.bat` script. This script activates the virtual environment, sets necessary environment variables, and starts the application:

```bash
start.bat
```

When prompted, enter the path to your video file and follow the on-screen instructions to select the best loop and the desired output format.

## Contributing

Contributions to LoopMaker are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

LoopMaker is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- PyTorch and torchvision for providing the deep learning framework and models.
- moviepy for handling video file operations.

## Contact

For any questions or feedback, please open an issue in the GitHub repository.
