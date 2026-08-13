# Summarize

**Purpose:** Shorten a piece of text down to its main points.

**Triggers (use when the request contains something like):**
- "summarize", "summarise", "shorten", "tl;dr"
- "in N bullets/points/sentences"
- a block of text pasted along with a request to condense it

**Steps:**
1. Read the text provided.
2. Pull out the main points only — drop examples, filler, and repetition.
3. If the person asked for a specific number of bullets/sentences, match that
   number exactly.
4. If no text was actually provided to summarize, ask for it instead of
   summarizing the request itself.

**Example**

Input: `Summarise this paragraph in three bullets: [a paragraph about a
company's Q2 results — revenue up 12%, new product launched in June, hiring
paused until Q4]`

Output:
> - Revenue grew 12% in Q2.
> - A new product launched in June.
> - Hiring is paused until Q4.
