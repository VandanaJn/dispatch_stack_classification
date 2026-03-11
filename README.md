# dispatch_stack_classification

Repository for a coding challenge to categorize packages for dispatch based on dimensions and mass.

## Installation
**Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```
**Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

```python
from src.sorter import sort

# Sort packages by: width, height, length, mass
print(sort(10, 10, 10, 5))      # Returns "STANDARD"
print(sort(150, 10, 10, 5))     # Returns "SPECIAL" (bulky)
print(sort(10, 10, 10, 25))     # Returns "SPECIAL" (heavy)
print(sort(150, 150, 150, 25))  # Returns "REJECTED" (both)
```

## Testing

```bash
python -m pytest tests
```
