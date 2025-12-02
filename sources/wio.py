import re

NUMBER_REGEX = r"\b(?:\d{1,3}(?:,\d{2,3})+|\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?\b"

class Wio:
    def __init__(self, text: str):
        self.text = text.lower()

    def detect(self) -> bool:
        return 'wio' in self.text or 'wealth' in self.text

    @property
    def value(self) -> float:
        # Look for currency-like numbers after $
        dollar_pattern = r'\$([0-9,]+\.?[0-9]*)'
        matches = re.findall(dollar_pattern, self.text)
        if matches:
            # Take the largest
            values = [float(m.replace(',', '')) for m in matches]
            return max(values)
        
        raise ValueError("Could not extract value for Wio")

    @property
    def currency(self) -> str:
        return 'USD'