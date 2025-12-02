import os
import json
from extractor import extract_info

def run_tests():
    """
    Run tests on all samples in test-data directory.
    """
    test_data_dir = 'test-data'
    passed = 0
    total = 0

    if not os.path.exists(test_data_dir):
        print(f"Test data directory '{test_data_dir}' not found.")
        return

    for source_dir in os.listdir(test_data_dir):
        source_path = os.path.join(test_data_dir, source_dir)
        if not os.path.isdir(source_path):
            continue

        image_path = os.path.join(source_path, 'image.jpg')
        output_path = os.path.join(source_path, 'output.json')

        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            continue
        if not os.path.exists(output_path):
            print(f"Output file not found: {output_path}")
            continue

        total += 1

        try:
            # Load expected output
            with open(output_path, 'r') as f:
                expected = json.load(f)

            # Run extraction
            result = extract_info(image_path)

            # Compare
            if result == expected:
                print(f"✓ PASS: {source_dir}")
                passed += 1
            else:
                print(f"✗ FAIL: {source_dir}")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")

        except Exception as e:
            print(f"✗ ERROR: {source_dir} - {str(e)}")

    print(f"\nResults: {passed}/{total} tests passed")

if __name__ == '__main__':
    run_tests()
