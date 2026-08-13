# Routing transcript

This is a record of running example commands against this project
(README.md → CLAUDE.md → skills/) to show the routing working. The earliest
tests below were run when the project had only two active skills — Developer
and Tester. The project has since grown to five active skills: Developer,
Tester, Greet, Summarize, and Convert. The QA section further down covers
routing for the full five-skill set.

---

**Command:** `Write a function that adds two numbers`

**Routing:** Matches `skills/developer/` ("write a function that...") →
opened `skills/developer/SKILL.md` → followed its steps.

**Result:** created `com/staymind/adder.py` (with `com/__init__.py` and
`com/staymind/__init__.py`):
```python
# package: com.staymind

def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

---

**Command:** `Write tests for the adder function`

**Routing:** Matches `skills/tester/` ("write tests for...") → opened
`skills/tester/SKILL.md` → found `com/staymind/adder.py` → followed its steps.

**Result:** created `com/staymind/test_adder.py`, importing from
`com.staymind.adder`. Ran it to confirm it actually passes:
```
test_negative_numbers ... ok
test_positive_numbers ... ok

Ran 2 tests in 0.000s

OK
```

---

**Command:** `Write something for the adder module`

**Routing:** Ambiguous — could mean "write more code" (Developer) or "write
tests" (Tester); the request doesn't say which. Per the routing rules in
`README.md`/`CLAUDE.md`, this does not get guessed at.

**Response:**
> I'm not sure what you'd like me to do — do you want me to add more code to
> the adder module (Developer), or write tests for it (Tester)? Let me know
> which, and I can help.

---

**Command:** `Create a temperature conversion calculator`

**Routing:** Matches `skills/developer/` ("create a ... calculator") → opened
`skills/developer/SKILL.md` → followed its steps.

**Result:** created `com/staymind/temperature_converter.py` — converts between
Celsius, Fahrenheit, and Kelvin (`celsius_to_fahrenheit`,
`fahrenheit_to_celsius`, `celsius_to_kelvin`, `kelvin_to_celsius`,
`fahrenheit_to_kelvin`, `kelvin_to_fahrenheit`), raises `ValueError` for
temperatures below absolute zero, and includes a small interactive CLI.

---

**Command:** `Write the required test cases for the temperature conversion calculator`

**Routing:** Matches `skills/tester/` ("write the ... test cases for...") →
opened `skills/tester/SKILL.md` → found `com/staymind/temperature_converter.py`
→ followed its steps.

**Result:** created `com/staymind/test_temperature_converter.py` with 13 test
cases — freezing/boiling points, the -40° crossover point where Celsius and
Fahrenheit agree, conversions to/from Kelvin, the absolute-zero boundary
(including that going below it raises `ValueError`), and a round-trip check.
Ran it to confirm it actually passes:
```
Ran 13 tests in 0.000s

OK
```

---

## Takeaway

The `Write something for the adder module` ambiguous case above (from when
the project had only Developer and Tester active) is different from a
request that matches nothing at all: it's "this could match either skill
equally well," not "this doesn't match anything." Both situations are
handled the same way by the routing rules — ask, don't guess. The QA section
below repeats this same check against the current five-skill project.

---

## QA routing tests — five skills (Developer, Tester, Greet, Summarize, Convert)

After Greet, Summarize, and Convert were reactivated (moved out of
`_to_delete/` back into `skills/`), the four required example behaviors were
tested.

**Methodology:** the literal Claude Code CLI was not available to execute
directly against this project. Instead, an equivalent routing test was run:
the current contents of `CLAUDE.md`, `README.md`, and all five `SKILL.md`
files were copied verbatim into an isolated scratch copy of the project, and
for each test a fresh agent with no memory of building this project — and no
foreknowledge of the expected answer — was given only the user's message and
told to read the project's own files itself, starting from the entry file,
and follow whatever routing instructions it found. This exercises the actual
routing logic (reading the entry file, matching against skill descriptions,
and asking rather than guessing when appropriate), since that logic is plain
instruction-following and not a Claude Code–specific mechanism.

**Test 1 — `Greet Priya in Hindi`**
- Route: `skills/greet/`
- Result: PASS
- Response: नमस्ते, Priya! (Hello, Priya!)

**Test 2 — `Summarise this paragraph in three bullets: Claude Code can use project instructions and skills to organize work.`**
- Route: `skills/summarize/`
- Result: PASS
- Exactly three bullets were produced.

**Test 3 — `Convert 20 km to miles`**
- Route: `skills/convert/`
- Result: PASS
- Response: 20 km ≈ 12.43 miles

**Test 4 — `Do the thing`**
- Route: no skill
- Result: PASS
- A clarifying question was asked instead of guessing.
