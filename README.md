# Investment OCR Extractor

A Python library that extracts investment balance information from screenshots using OCR.

## Features

- Extracts source platform (e.g., "etoro", "fundsindia") and numerical value from images
- Uses EasyOCR for accurate text recognition with preprocessing
- Robust number extraction with support for commas, decimals, and various formats
- Handles common OCR errors and text cleaning
- Supports multiple investment platforms with platform-specific extraction logic

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
print(result)  # {'source': 'etoro', 'value': 55985.97, 'currency': 'USD'}
```

## Supported Platforms

- **Etoro**: Extracts balance from USD currency displays
- **FundsIndia**: Extracts current value from mutual fund dashboards

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