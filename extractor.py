import cv2
import easyocr
from sources.etoro import Etoro
from sources.fundsindia import FundsIndia
from sources.wio import Wio
from typing import Dict, Any

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

def extract_info(image_path: str) -> Dict[str, Any]:
    """
    Extract source and value from an investment platform screenshot.

    Args:
        image_path: Path to the image file

    Returns:
        Dict with 'source' (str) and 'value' (float), 'currency' (str)
    """
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")

    # Preprocess: convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Optional: enhance contrast
    gray = cv2.equalizeHist(gray)

    # Extract text using OCR
    text_results = reader.readtext(gray)

    # Combine all detected text
    full_text = ' '.join([result[1] for result in text_results]).lower()

    # Clean text: replace common OCR errors
    full_text = full_text.replace('s', '$')  # 's' might be '$'

    # Try each source
    sources = [Etoro(full_text), FundsIndia(full_text), Wio(full_text)]
    for source_class in sources:
        if source_class.detect():
            return {
                'source': source_class.__class__.__name__.lower(),
                'value': source_class.value,
                'currency': source_class.currency
            }

    raise ValueError("Could not detect source from image")