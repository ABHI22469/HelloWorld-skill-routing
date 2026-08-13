# HelloWorld

Practice project for STA-41 (starter project, engineer track). This is a learning
exercise — not real product code. It lives in a sandbox / practice repo, agreed
with the reviewer, and should never be copied into a product application path.

## What this project is

A tiny demo of how Claude reads a project's entry file and picks the right
"skill" (a small folder of instructions) to answer a request with, instead of
just guessing.

## Skills in this project

| Skill | Folder | Use when |
|---|---|---|
| Developer | `skills/developer/` | The request asks to write/implement/build a Python function, class, or program. |
| Tester | `skills/tester/` | The request asks to write or add unit tests for existing Python code. |
| Greet | `skills/greet/` | The request asks to greet/say hello to someone, in any language. |
| Summarize | `skills/summarize/` | The request asks to shorten, summarize, or bullet-point some text. |
| Convert | `skills/convert/` | The request asks to convert a number from one unit to another. |

## Coding convention: the `com.staymind` package

The Developer and Tester skills both produce Python source files. Every file
they create belongs to the `com.staymind` package. Since Python doesn't have a
`package` statement like Java, this is represented two ways in every file:

1. The file lives under the folder path `com/staymind/...` (with an empty
   `__init__.py` in `com/` and `com/staymind/`).
2. The file starts with the header comment `# package: com.staymind`.

See `skills/developer/SKILL.md` and `skills/tester/SKILL.md` for the full
details and a worked example of each.

## Routing rules

1. Read this file (`README.md`) first — it's the map of the project.
2. Look at the request and compare it to each skill's "use when" line above.
3. If exactly one skill clearly matches, open that skill's `SKILL.md` and follow
   its steps.
4. If the request is too vague to tell which skill applies (or it could match
   more than one equally well), do not guess — ask a short clarifying question
   instead.
5. If no skill matches at all, say so plainly instead of forcing a fit.

See `CLAUDE.md` for the exact instructions given to Claude.

## How to add another skill (under 5 minutes)

1. Make a new folder: `skills/<your-skill-name>/`
2. Add one file inside it: `skills/<your-skill-name>/SKILL.md`, with four
   sections: Purpose, Triggers (when to use it), Steps (what to do), and one
   worked Example (input → output). Copy the shape of `skills/developer/SKILL.md`
   if it helps to start from a template.
3. Add one row to the skills table above: the skill's name, its folder, and a
   one-line "use when" description.

That's it — no code changes anywhere else are needed. The routing rules above
already say to check every skill listed in this table.
