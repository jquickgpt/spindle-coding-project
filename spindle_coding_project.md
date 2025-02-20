
# Spindle Coding Project for AI Engineer (Lead/Principal IC)
## Agents, Agentic Systems & Applied LLMs

# 🎯 Your Mission

**This mission represents a stripped-down but realistic “toy version” of the kind of multi-agent system Spindle AI is engineering. (including some actual challenges we’ve already faced):**

1. **The Setup:** First, create ≥5 distinct, simple, deterministic tools that an LLM-based agent could call to help solve user-provided math problems (*e.g.* `SUM`, `DELTA`, `PRODUCT`, `QUOTIENT`, `MODULO`, `POWER`, `ABS`, `LOG`, `TRIG`, `SQRT`, `AVG`, `MODE`, `ROUND`, `UNION`, `INTERSECT`, `DIFFERENTIATE`, `INTEGRATE`, `FACTORIZE`, **…** *— the specific tools are entirely up to you*). 
    1. **Modify 1-2 of the most basic tools to *intentionally but silently throw errors (and/or silently give incorrect answers) 30%-50% of the time the tool is called*.** You *may* also want to include a basic `GET_USER_INPUT` tool for requesting input/clarification from a human user. (You can organize all tools in some form of “toolbox” if you want, but we’d prefer you do **not** hardcode a string listing all the tools, their docs, and their usage examples in a *single* prompt file or prompt mega-string anywhere in the project.)
2. **The Architecture:** Prototype a multi-agent system with ***at least* 2 agents** and *at most* 5 agents (for whatever definition of “agent” you believe makes sense in this context), that discovers which tools are available and sequences tool calls to **reliably** solve basic user-provided math problems (or if you prefer, mathy word problems). The agents can *only* ****use the available tools ***(including the unreliable tool[s])***, *i.e.* no LLM-hallucinated arithmetic should be used for user-facing answers (*even* if that arithmetic is correct, as is increasingly the case among frontier models).
    1. You might well choose to include a lightweight planning, reasoning, and/or task decomposition layer in your prototype — but unless you have a compelling justification, all *user-facing* outputs (and most intermediate outputs) should be structured or semistructured, not unstructured. 
    
    - **Don’t hesitate to ask us for an OpenAI API key or Anthropic API key.** Otherwise, we’re happy to reimburse these costs after submission *(within reason/at Spindle’s discretion)*.
3. **The Twist:** When your prototype identifies a sequence of tool calls that reliably *or fairly reliably* solves a certain class of math problem(s) **based on successful execution(s)**, it should do something like *(e.g.)* **memoize or semantically cache that sequence of tool calls as a single, idempotent new `VirtualTool`** (*i.e.* some behavior akin to **“bundling” the tool calls into a *single* new idempotent tool, to which a *single* call can be made, which can be reliably invoked *next time a math problem of the same or similar form is encountered*). 
4. **The Finish Line:** Prove programmatically that your prototype works reasonably well (or at least that it could be *completed* to work reasonably well, if short on time). 
    1. **Bonus points for using actual evals to show this.** 
        1. ***(If you’re are an “evals-focused” candidate, consider reframing/approaching the entire task through the lens of an evals system instead, i.e. evals-driven development. Just tell us to judge your quality vs. emphasis vs. completion accordingly.)***
5. **Bonus Points:**
    1. Create the math toolbox/interfaces in a non-Python language (ideally Rust, Go, or Typescript).
    2. *If* you decide to use a vector database anywhere, consider prototyping your *own* vector DB or VDB-like utility. (Not if this takes up all your time, though. It’s not the most important part.)

- **If you don’t have enough time for a project like this, or have alternate ideas, please let us know so we can find a path forward that we all feel good about!** Either way, we really look forward to seeing you through these next steps.

# 🛠️ Does it matter “how” I accomplish this?

- **Not really:** The priority of this project is to ship useful software in a way that **shows off some *creativity* and *your strengths*** (at Spindle AI we “hire for strengths, not for lack of weaknesses” and “hire people, not roles”), within certain constraints. (All this being said, *(1)* we’d generally *prefer* that you don’t use LangChain, unless doing so is important to showing off your strengths or creativity, and *(2)* most successful submissions will treat this as an engineering project, not a data science project.)
- **You can use an LLM to help you write any code you want.** *No* bonus points for writing all your code by hand. 
- **There is no single “correct” answer or “correct” approach;** there are only *tradeoffs* (and, we expect you to be able to discuss tradeoffs in depth, either in your README or when reviewing the results together).
- **If you are inspired to go a different direction and feel confident it will result in a more compelling outcome, feel free to do so.** This works *as long as* you’re confident we’ll be able to evaluatue your project using many of the same criteria as we’d evaluate using the scope proposed originally.
    - **Rescope the work based on what you can *fully* accomplish *(at least steel thread with demoable functionality)* in the time available.** We’d ask that you don’t spend an excessive or unusual amount of time **(we’re *not* trying to test how much free time you have)**. If you’re feeling pressed for time, you might focus on a narrower scope! If you’re feeling more adventurous, you might push it further! (We trust your judgement either way, but the consequences are yours to own.)

# 📬 Delivering your project

*If live-coding this with us today, ignore this section. Otherwise:*

- Please **include a short README with a link to a quick-n-dirty demo video (Loom or similar), foolproof instructions on running the software**, and ≥2 “next steps” or “future work” bullet points. (It would also be helpful if you indicated roughly how much time you spent on the project in the README so we can recallibrate our evaluation accordingly.)
- Feel free to ask us clarifying questions anytime!

---

**`*Sensitive & confidential.`** Please do not share with other potential recruits.* 
**©** *2025 Spindle Technologies, Inc. d/b/a [Spindle AI](https://spindle.ai). All rights reserved. [Email us ›](mailto:carson@spindle.ai)*
