# AI-Based Laboratory Theft Detection & Prevention System

**Air University Islamabad**  
**Department of Creative Technologies | Faculty of Computing & AI**  
**Course:** AI Project Design and Development (AI-316)  
**Lab 01:** Foundations of AI Engineering & Project Setup  
**Instructor:** Farhan Zafar  
**Student:** Kamran Ahmed  

---

## 1. Overview

The **AI-Based Laboratory Theft Detection & Prevention System** is an intelligent computer vision security solution engineered to protect high-value laboratory equipment (such as laptops, scientific instruments, monitors, and specialized tools). 

Unlike conventional CCTV solutions that rely on passive recording and post-incident investigation, this automated system actively ingests video streams, detects people and monitored assets, tracks interactions over time, evaluates spatial movement against defined Regions of Interest (ROIs), and generates real-time alerts with preserved evidence whenever unauthorized removal behavior is detected.

---

## 2. Problem Statement

Educational and industrial laboratories house sensitive and expensive hardware that is vulnerable to unauthorized relocation and theft. Traditional security infrastructures present critical vulnerabilities:
1. **Passive Observation:** Security guards cannot vigilantly monitor dozens of live camera feeds simultaneously.
2. **Delayed Investigation:** Incidents are typically noticed hours or days after the theft occurred.
3. **Manual Review Bottlenecks:** Security personnel must review extensive hours of unindexed footage to locate the timestamp of an incident.

By deploying computer vision models at the edge or local server, this project automates surveillance, detects unauthorized object movement toward exits in real time, and logs verifiable evidence immediately.

---

## 3. Core Objectives

- **Asset & Human Detection:** Detect people and designated laboratory equipment using state-of-the-art object detection models (YOLO).
- **Multi-Object Tracking:** Assign persistent tracking IDs to people and assets across video frames (ByteTrack / BoT-SORT).
- **Spatial ROI Analysis:** Monitor predefined spatial zones including Equipment Zones, Restricted Areas, and Exit Passages.
- **Temporal Event Logic:** Analyze spatio-temporal interactions across consecutive frames (e.g., person enters $\rightarrow$ approaches asset $\rightarrow$ picks up item $\rightarrow$ moves toward exit).
- **Automated Alerts & Evidence Preservation:** Trigger warnings, save annotated image snapshots or video clips, and store event logs for security operators.

---

## 4. High-Level Future Pipeline

```
Camera / RTSP Stream
        │
        ▼
Frame Ingestion & Preprocessing (OpenCV)
        │
        ▼
Object & Human Detection (Ultralytics YOLO)
        │
        ▼
Multi-Object Tracking (ByteTrack / BoT-SORT)
        │
        ▼
Spatial Analysis & ROI Mapping (Equipment / Exit Zones)
        │
        ▼
Temporal Event Logic & Interaction Analysis
        │
        ▼
Suspicious Activity Decision Engine
   ├── If Normal: Resume monitoring
   └── If Suspicious: Trigger Alert -> Save Evidence Snapshot -> Record Event Log
```

> **Note on Lab 01 Scope:** Lab 01 focuses strictly on foundational AI engineering practices—standardized project structure, virtual environment configuration, package pinning, version control branching strategies, and interactive notebook verification. The AI models and pipeline modules will be systematically developed and integrated in subsequent labs.

---

## 5. Project Directory Structure

```text
AIDP-Lab/
│
├── configs/                # Configuration files (model YAMLs, ROI coordinates, thresholds)
│   └── .gitkeep
│
├── data/                   # Data storage (excluded from Git version control)
│   ├── raw/                # Original video streams, surveillance recordings, calibration media
│   │   └── .gitkeep
│   └── processed/          # Preprocessed datasets, annotations, extracted frames
│       └── .gitkeep
│
├── logs/                   # System and event logs
│   └── .gitkeep
│
├── models/                 # Model checkpoints, ONNX/TensorRT exports (weights excluded via .gitignore)
│   └── .gitkeep
│
├── notebooks/              # Jupyter notebooks for exploratory data analysis, testing & verification
│   ├── .gitkeep
│   └── lab01_setup.ipynb   # Lab 01 environment verification and project specification notebook
│
├── src/                    # Source code for future modular AI components
│   └── .gitkeep
│
├── .gitignore              # Git ignore rules for venvs, checkpoints, logs, and model binaries
├── README.md               # Project documentation and setup guide
├── requirements.txt        # Pinned project dependencies
└── setup_project.py        # Automation script to verify/initialize directory structure
```

---

## 6. Environment Setup & Installation

### Prerequisites
- Python 3.10 to 3.13 installed
- Git installed and configured

### Step 1: Clone the Repository
```bash
git clone https://github.com/Kamranahmed231232/AIDP-Lab.git
cd AIDP-Lab
```

### Step 2: Create the Virtual Environment
Create an isolated virtual environment named `aipdd_env`:

**Windows (PowerShell / Command Prompt):**
```powershell
python -m venv aipdd_env
```

**Linux / macOS:**
```bash
python3 -m venv aipdd_env
```

### Step 3: Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.\aipdd_env\Scripts\Activate.ps1
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

**Windows (Command Prompt):**
```cmd
aipdd_env\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source aipdd_env/bin/activate
```

### Step 4: Install Dependencies
Install all pinned dependencies from `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Register Jupyter Kernel
Register the `aipdd_env` environment with Jupyter:
```bash
python -m ipykernel install --user --name aipdd_env --display-name "Python (aipdd_env)"
```

---

## 7. Running the Verification Notebook

Launch Jupyter Notebook:
```bash
jupyter notebook
```
Navigate to `notebooks/lab01_setup.ipynb`. Ensure the selected kernel is **Python (aipdd_env)**, then run all cells to verify that OpenCV, PyTorch, Ultralytics YOLO, Matplotlib, and NumPy import successfully with their installed versions printed.

---

## 8. Git Version Control & Branching Strategy

This project adheres to professional Git branching practices:
- **`main`**: Production-ready, stable codebase.
- **`feature/lab01-setup`**: Feature branch used to set up the environment, pin dependencies in `requirements.txt`, configure notebooks, and perform verification before merging back into `main`.

---

## 9. Current Status

- [x] Standard AI project repository structure defined and verified.
- [x] Root `.gitignore` configured to exclude `.venv`, binary weights (`.pt`, `.onnx`, `.h5`), and `.ipynb_checkpoints`.
- [x] Python virtual environment `aipdd_env` configured with required libraries.
- [x] Pinned `requirements.txt` exported.
- [x] Jupyter Notebook (`notebooks/lab01_setup.ipynb`) created and executed with full environment verification.
- [x] Feature branch `feature/lab01-setup` created, committed, and merged into `main`.
