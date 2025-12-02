import re

NUMBER_REGEX = r"\b(?:\d{1,3}(?:,\d{2,3})+|\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?\b"

class FundsIndia:
    def __init__(self, text: str):
        self.text = text.lower()

    def detect(self) -> bool:
        return 'mutual' in self.text or 'fundsindia' in self.text

    @property
    def value(self) -> float:
        # Look for numbers in {}, like {1352982} {3802615
        brace_pattern = r'\{([^{}]+)\}'
        matches = re.findall(brace_pattern, self.text)
        if not matches:
            # Try without requiring closing brace
            brace_pattern = r'\{([^}\s]+)'
            matches = re.findall(brace_pattern, self.text)
        if matches:
            # The current value is typically the second one
            if len(matches) >= 2:
                # Extract number from the second brace
                numbers = re.findall(r'\d+(?:,\d+)*', matches[1])
                if numbers:
                    return float(numbers[0].replace(",", ""))
            # Or take the largest from all braces
            all_numbers = []
            for match in matches:
                numbers = re.findall(r'\d+(?:,\d+)*', match)  # Match comma-separated numbers
                all_numbers.extend(numbers)
            if all_numbers:
                values = [float(n.replace(",", "")) for n in all_numbers]
                return max(values)
        
        raise ValueError("Could not extract value for FundsIndia")

    @property
    def currency(self) -> str:
        return 'INR'