# task name - 26
---
## Task Comprehension - 2 points
ok
## Report - 1.45 points
- [x] The description of the dataset (brief)
- [x] The format of the given dataset, give to us a sample of the input format.
- [x] Methodology used to reframe the dataset
	- [ ] not clear how distractors were chosen (**-0.5**)
- [x] The list of suitable prompts
- [x] The instructions to run your code and any other information you think it will be useful for us
---
- she used FastLang to check the language of a word and remove non-italians, which seems cool but she doesn't mention any tests done to inspect the output of this tool (es. what about 'sauna')
	- Her name is not Italian tho, maybe she is not confident with it
- slight report overflow due to formatting (**-0.05**)
- table a bit ugly
## Data - 1.75 points
- prompt file not compliant to jinja template (`{}` instead of `{{}}`) (**-0.25**)

## Code - 1.75 points
- `find_distractor` function does not assure the numbers of distractors is always at least 3 (**-0.25**)
---
# Total - 6.95 points
26 / 30
