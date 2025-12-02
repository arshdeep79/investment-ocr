# Investment OCR Extractor

A Python library that extracts investment information from screenshots using OCR.

## Features

- Extracts source platform (e.g., "etoro") and numerical value from images
- Uses EasyOCR for accurate text recognition
- Handles common OCR errors and text cleaning

## Installation

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from extractor import extract_info

result = extract_info('path/to/screenshot.jpg')
print(result)  # {'source': 'etoro', 'value': 55985.97}
```

## Testing

Run the test suite:
```bash
python test.py
```

Add more test samples in `test-data/<source>/` with `image.jpg` and `output.json`.

## Dependencies

- easyocr
- pillow
- opencv-python