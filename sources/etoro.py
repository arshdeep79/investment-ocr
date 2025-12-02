import re

NUMBER_REGEX = r"\b(?:\d{1,3}(?:,\d{2,3})+|\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?\b"

class Etoro:
    def __init__(self, text: str):
        self.text = text.lower()

    def detect(self) -> bool:
        return 'etoro' in self.text

    @property
    def value(self) -> float:
        # Look for currency-like numbers (with commas and decimals)
        currency_pattern = r'(\d{1,3}(?:,\d{3})+\.\d{2})'
        matches = re.findall(currency_pattern, self.text)
        if matches:
            values = [float(m.replace(',', '')) for m in matches]
            return max(values)
        
        # Fallback to largest number
        numbers = re.findall(NUMBER_REGEX, self.text)
        if not numbers:
            raise ValueError("Could not extract value for Etoro")
        
        clean_numbers = [float(n.replace(",", "")) for n in numbers]
        balance = max(clean_numbers)
        
        return balance

    @property
    def currency(self) -> str:
        return 'USD'