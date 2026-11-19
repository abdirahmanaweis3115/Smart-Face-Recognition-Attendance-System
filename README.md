Writing

# Smart Face Recognition Attendance System

A contactless attendance management system developed using Python, Dlib, OpenCV, Flask, and SQLite.

## Features

- Face registration through a webcam interface.
- Face image storage in `data/data_faces_from_camera/`.
- Extraction of 128-dimensional face descriptors.
- Storage of extracted features in `data/features_all.csv`.
- Real-time face recognition through a webcam.
- Automatic attendance recording using SQLite.
- Web-based attendance viewing by date.

## Installation and Setup

### 1\. Create a Virtual Environment

bash

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

bash

```bash
.venv\Scripts\activate
```

**macOS / Linux**

bash

```bash
source .venv/bin/activate
```

### 2\. Install Dependencies

bash

```bash
pip install -r requirements.txt
```

### 3\. Download Required Model Files

bash

```bash
python download_models.py
```

### 4\. Register Faces

bash

```bash
python get_faces_from_camera_tkinter.py
```

### 5\. Extract Face Features

bash

```bash
python features_extraction_to_csv.py
```

This generates `data/features_all.csv`, containing the extracted face descriptors.

### 6\. Run the Attendance System

bash

```bash
python attendance_taker.py
```

The application performs real-time face recognition and records attendance in the SQLite database.

### 7\. Run the Web Application

bash

```bash
python app.py
```

Access the web application at:

`http://127.0.0.1:5000`

## Project Structure

| File / Directory | Description |
| --- | --- |
| `app.py` | Flask web application |
| `attendance_taker.py` | Face recognition and attendance recording |
| `get_faces_from_camera_tkinter.py` | Face registration interface |
| `features_extraction_to_csv.py` | Face feature extraction |
| `download_models.py` | Model file downloader |
| `requirements.txt` | Python dependencies |
| `attendance.db` | SQLite attendance database |
| `data/` | Face images, extracted features, and model files |

## GitHub Configuration

Dlib model files (`.dat`) are large and can be managed using Git LFS.

### Git LFS Setup

bash

```bash
git init
git lfs install
git lfs track "*.dat"
```

Add and commit the configuration files:

bash

```bash
git add .gitattributes .gitignore README.md
git commit -m "Initial project setup"
```

Connect the remote repository and push:

bash

```bash
git remote add origin <repository-url>
git push -u origin main
```

Alternatively, model files can be excluded from the repository and downloaded during project setup:

bash

```bash
python download_models.py
```

## Data Management

- `data/data_faces_from_camera/` stores registered face images.
- `data/features_all.csv` stores extracted face descriptors.
- `attendance.db` stores attendance records.
- `data/*.dat` contains required Dlib model files.
- Face images and local database files are excluded from version control through `.gitignore`.

## Requirements

- Python 3.x
- OpenCV
- Dlib
- Flask
- SQLite
- Webcam
- Required Dlib model files
