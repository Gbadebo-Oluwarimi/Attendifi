# Facial Recognition Attendance System


The **Facial Recognition Attendance System** is a Python-based application designed to automate attendance tracking using advanced computer vision and machine learning techniques. Leveraging libraries such as **OpenCV**, **dlib**, and **face_recognition**, the system detects and recognizes faces in real-time, ensuring efficient and accurate attendance recording.

## Features

- **Real-Time Face Detection**: Utilizes webcam input to detect faces instantaneously.
- **Deep Learning-Based Face Recognition**: Employs deep convolutional neural networks (CNNs) to generate unique facial embeddings for individual identification.
- **Automated Attendance Logging**: Records attendance data with timestamps in a CSV file.
- **User-Friendly Interface**: Provides a straightforward interface for seamless operation.
- **Scalability**: Adaptable for various environments, including educational institutions, corporate offices, events, and healthcare facilities.

## Technical Details

### Face Detection and Recognition Process

The system follows a structured pipeline for face recognition:

1. **Face Detection**: Identifies faces within the video stream using Histogram of Oriented Gradients (HOG) combined with a linear classifier, an approach that balances accuracy and computational efficiency.

2. **Face Alignment**: Aligns detected faces to a standard orientation, enhancing recognition accuracy by mitigating variations due to head tilts or rotations.

3. **Feature Extraction**: Utilizes a deep CNN to compute a 128-dimensional embedding for each face. This embedding captures the unique features of a face, enabling differentiation between individuals.

4. **Face Matching**: Compares the computed embeddings with a database of known embeddings using Euclidean distance. A threshold is applied to determine if a detected face matches a known individual.

### Deep Learning Insights

Modern face recognition systems, such as the one implemented here, are inspired by advancements in deep learning. Notably, models like **FaceNet** have demonstrated the effectiveness of mapping faces into a high-dimensional space where similar faces are positioned closer together. This method involves training the network with a triplet loss function, which ensures that embeddings of the same person are closer than those of different people. ([article link](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)))

## Installation

### Prerequisites

- **Python 3.x**
- **pip** (Python package installer)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clonehttps://github.com/Gbadebo-Oluwarimi/Attendifi.git
   cd facial-recognition-attendance-system
   ```

2. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Dataset**:
   - Place reference images in the `imagedesc/` directory.
   - Ensure filenames correspond to the individuals' names (e.g., `john_doe.jpg`).

4. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Launch the Application**: The webcam will activate, and the system will begin detecting faces in real-time.
2. **Face Recognition**: The system matches detected faces against the reference images.
3. **Attendance Logging**: Recognized individuals' names and timestamps are recorded in the `Attendance.csv` file.

## Project Structure

```
facial-recognition-attendance-system/
├── imagedesc/                  # Directory containing reference images
├── Attendance.csv              # CSV file storing attendance records
├── main.py                     # Main script to run the application
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Special thanks to:

- **Adam Geitgey** for his insightful article on modern face recognition with deep learning.
- **OpenCV** for the comprehensive computer vision library.
- **dlib** for robust facial recognition algorithms.
- **face_recognition** for simplifying the face detection and recognition process.
- **Python** for being a versatile programming language suitable for AI and machine learning projects.

