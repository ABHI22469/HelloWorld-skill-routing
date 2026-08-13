# Greet

**Purpose:** Say hello to a named person, in whatever language is requested (or
English if none is named).

**Triggers (use when the request contains something like):**
- "greet", "say hi/hello to", "welcome"
- a person's name, optionally with a language ("...in Hindi/Spanish/French")

**Steps:**
1. Find the name of the person to greet in the request.
2. Find the language, if one is named. If none is named, use English.
3. Say hello to that person in that language.
4. If the language is one you're not confident translating correctly, say the
   greeting in English and mention you're unsure of the translation, rather
   than guessing at a wrong translation.

**Example**

Input: `Greet Priya in Hindi`

Output:
> नमस्ते, Priya! (Hello, Priya!)
