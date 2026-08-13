# Convert

**Purpose:** Convert a number from one unit of measurement to another.

**Triggers (use when the request contains something like):**
- "convert", "how many X in Y", "in miles/kg/dollars/etc."
- a number followed by a unit, and a target unit

**Steps:**
1. Identify the number and the starting unit.
2. Identify the target unit.
3. Do the conversion using the standard conversion factor.
4. Show the answer rounded to two decimal places, with both units labeled.

**Example**

Input: `Convert 20 km to miles`

Output:
> 20 km ≈ 12.43 miles
