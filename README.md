# hw1b_nlp2024

After having put in the root folder of the repo the `.csv` file containing the list of students and their assigned datasets, run:

```bash
python main.py
```

The `.csv` schema should be as follow:
```python
['University ID',   # mandatory in position 1
 'In need for Italian speakers or for more project members (Y/N)',
 'Group ID (make sure the ID you specify is NOT already present in previous rows, unless the student belongs to the same group!)',
 'Assigned datasets', # mandatory in position 3
 'New assigned dataset (for students previously having only one)',
 'Assigned distractor dataset (EXTRA)'
]
```

Example output:
```bash
> Distribution of HW1B datasets BEFORE (mean 9.333):
0  |#######
1  |##########
5  |######
7  |#######
8  |#######
9  |###############################
18 |########
21 |#######
22 |######
24 |########
27 |########
28 |#######

> Distribution of HW1B datasets AFTER (mean 8.083):
0  |######
1  |######
5  |#####
7  |#####
8  |######
9  |##############################
18 |######
21 |#####
22 |######
24 |########
27 |#######
28 |#######
```