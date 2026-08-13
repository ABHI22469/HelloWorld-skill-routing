# Tester

**Purpose:** Write Python test files for existing source code produced by the
Developer skill.

**Triggers (use when the request contains something like):**
- "write tests for...", "add unit tests...", "test the ... function/class"

**Steps:**
1. Find the source file under `com/staymind/` that the request refers to. If
   it doesn't exist yet, say so instead of inventing what it might contain.
2. Create a test file next to it, named `com/staymind/test_<module>.py`.
3. This file also belongs to the `com.staymind` package — give it the same
   header comment as the Developer skill:
   ```
   # package: com.staymind
   ```
4. Import the code under test using its package path, e.g.
   `from com.staymind.adder import add`.
5. Write test cases covering a normal case and at least one edge case (e.g.
   negative numbers, empty input, zero).
6. Use Python's built-in `unittest` module unless the project already has a
   test framework in use.

**Example**

Input: `Write tests for the adder function`

Output: creates `com/staymind/test_adder.py`:
```python
# package: com.staymind

import unittest
from com.staymind.adder import add


class TestAdder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
```
