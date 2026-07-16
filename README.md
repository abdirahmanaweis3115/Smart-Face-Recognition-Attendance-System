# Smart Face Recognition Attendance System

This repository contains a contactless attendance system using Dlib and OpenCV.

## What it does
- Register people via webcam GUI and save face images under `data/data_faces_from_camera/`.
- Extract 128-D face descriptors (Dlib) and save averaged descriptors per person into `data/features_all.csv`.
- Run real-time recognition to log attendance into `attendance.db` (SQLite).
- Small Flask app (`app.py`) to view attendance by date.

## Quick setup
1. Create and activate a Python virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download required Dlib models (script will place them into `data/`):

```bash
python download_models.py
```

4. Register faces (GUI):

```bash
python get_faces_from_camera_tkinter.py
```

5. Extract features and create `data/features_all.csv`:

```bash
python features_extraction_to_csv.py
```

6. Run the attendance recognizer (camera):

```bash
python attendance_taker.py
```

7. (Optional) Run the web UI to view attendance:

```bash
python app.py
# Then open http://127.0.0.1:5000
```

## GitHub / Large files guidance
- The Dlib model files are large (`.dat`) and should NOT be committed directly to the repository.
- Recommended: use Git LFS for `.dat` files.

Basic Git + LFS workflow:

```bash
git init
git lfs install
git lfs track "*.dat"
# commit .gitattributes and .gitignore first
git add .gitattributes .gitignore README.md
git commit -m "Prepare repo for GitHub (ignore large files)"
# add remote and push
git remote add origin <your-repo-url>
git push -u origin main
```

If you prefer not to use Git LFS, do NOT commit `data/*.dat`; instead keep them out of the repo and run `python download_models.py` on each machine.

## Notes
- `data/data_faces_from_camera/` and `attendance.db` are excluded by `.gitignore` to protect user images and local data.
- If you want to include model files in the repo, enable Git LFS and commit them.

## License
Add your preferred open-source license if you plan to publish this publicly.
