# Instructions for Claude

This project is called HelloWorld (STA-41, engineer track). It's a learning
sandbox, not production code.

When you get a request in this project, follow these steps in order:

1. Read `README.md` first. It lists every available skill and a one-line
   description of when to use each one.
2. Compare the request against each skill's "use when" description.
3. If exactly one skill is a clear match, open `skills/<that-skill>/SKILL.md`
   and follow its steps exactly, including its example format.
4. If the request could reasonably match more than one skill, or matches none
   clearly, do not pick one and guess. Ask the person a short clarifying
   question instead, naming the skills from README.md's table that seem
   closest, e.g. "Do you want me to greet someone, summarize some text,
   convert a unit, write code, or write tests? Let me know which."
5. Never invent a new skill on the fly. If nothing in `skills/` fits, say so
   and suggest the person add a new skill (see the "How to add another skill"
   section of `README.md`).

Do not skip step 1, even if a request looks obvious — the point of this
project is that routing always starts from the entry file.
