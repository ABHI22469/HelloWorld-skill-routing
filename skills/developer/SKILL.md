# Developer

**Purpose:** Write Python application source code when asked to implement,
build, or create a program, function, or class.

**Triggers (use when the request contains something like):**
- "write code for...", "implement...", "build a function/class that...",
  "create a program that..."

**Steps:**
1. Decide on a short, clear module name for what's being built (e.g. `adder`
   for an add-two-numbers function).
2. Every source file this skill creates belongs to the `com.staymind` package.
   Since Python doesn't have a `package` statement like Java, represent this
   two ways:
   - Place the file under the folder path `com/staymind/<module>.py`, with an
     `__init__.py` in both `com/` and `com/staymind/` (create them if they
     don't exist yet, they can be empty).
   - Start the file itself with the header comment:
     ```
     # package: com.staymind
     ```
3. Write the implementation below the header comment.
4. In your response, state the exact file path you created, so the Tester
   skill (or a person) can find it.
5. Add a comment "Used developer skill" on top of the test class.

**Example**

Input: `Write a function that adds two numbers`

Output: creates `com/staymind/adder.py`:
```python
# package: com.staymind

def add(a, b):
    """Return the sum of a and b."""
    return a + b
```
And replies: "Created `com/staymind/adder.py` with an `add(a, b)` function."
