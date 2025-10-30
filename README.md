# APS Automation SDK

A Python SDK that wraps the Autodesk Platform Services (APS) Design Automation API, making it faster and easier to automate Revit workflows in the cloud.

## Installation

### Prerequisites

1. **Install uv** (fast Python package manager):
   ```powershell
   pip install uv
   ```
   
   For other installation methods, see: https://docs.astral.sh/uv/getting-started/installation/

2. **Clone or download this repository**

### Install the SDK

From the project root directory:

```powershell
# Install the package in editable mode
uv pip install -e .
```

**Note:** When running the Jupyter notebook in VS Code for the first time, you may be prompted to install the `ipykernel` package. Click "Install" or run:

```powershell
uv add ipykernel
```

## Configuration

Create a `.env` file in the project root with your APS credentials:

```ini
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

Get your credentials from the [APS Developer Portal](https://aps.autodesk.com/).

## Quick Start

Open and run the `example.ipynb` notebook to see a complete IFC export workflow:

1. Authenticate with APS
2. Deploy an AppBundle
3. Create an Activity
4. Execute a WorkItem
5. Download results

The notebook demonstrates exporting IFC files from a Revit model using Design Automation.
