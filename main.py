import csv
from pprint import pprint
from typing import Counter

PATH = "./assignment.csv"
FALLBACK_DATASET = 30
HW1B_DATASETS = {0, 1, 5, 7, 8, 9, 18, 21, 22, 24, 27, 28}


def counter_mean(counter: Counter):
    values = counter.values()
    return sum(values) / len(values)


def ascii_bar_chart(counter: Counter, symbol="#", title=""):
    mean = counter_mean(counter)
    counter = counter.most_common()
    chart = {category: symbol * frequency for category, frequency in counter}
    max_len = max(len(str(frequency)) for frequency in chart)
    print(f"{'Distribution' if title == '' else title} (mean {mean:.3f}):")
    for category, frequency in sorted(chart.items()):
        padding = (max_len - len(str(category))) * " "
        print(f"{category}{padding} |{frequency}")
    print()


def read_csv(path: str):
    data_freq = Counter()
    students2datasets = {}
    student_to_process = set()

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f"> Columns:")
                pprint(row)
            else:
                matricola = row[0].strip()  # University ID
                datasets = row[3].strip()  # 'Assigned datasets'
                a, b = int(datasets.split(",")[0]), int(datasets.split(",")[1])
                datasets = {a, b}

                if matricola in students2datasets.keys():
                    print(
                        f"\t[WARN] >> student {matricola} already present with datasets {students2datasets[matricola]}, skipping {datasets}."
                    )
                    continue

                students2datasets[matricola] = []

                if a in HW1B_DATASETS:
                    students2datasets[matricola].append(a)
                    data_freq.update([a])

                if b in HW1B_DATASETS:
                    students2datasets[matricola].append(b)
                    data_freq.update([b])

                if a not in HW1B_DATASETS and b not in HW1B_DATASETS:
                    students2datasets[matricola].append(FALLBACK_DATASET)
                    data_freq.update([FALLBACK_DATASET])

                if a in HW1B_DATASETS and b in HW1B_DATASETS:
                    student_to_process.add(matricola)

            line_count += 1

    print(f"> Processed {line_count} lines.\n")
    return students2datasets, data_freq, student_to_process


if __name__ == "__main__":

    # Process the csv file
    s2d, data_freq, to_process = read_csv(PATH)
    ascii_bar_chart(
        data_freq,
        title="> Distribution of HW1B datasets BEFORE",
    )

    # Print the students having both datasets in the selected set and replace their choice
    print(
        f"{len(to_process)} students have 2 assigned datasets which are both in the selected list."
    )
    to_change = {}
    for matricola in to_process:
        a = s2d[matricola][0]
        b = s2d[matricola][1]
        if data_freq[a] < data_freq[b]:
            to_change[matricola] = a
            data_freq[a] += 1
            data_freq[b] -= 1
        else:
            to_change[matricola] = b
            data_freq[a] -= 1
            data_freq[b] += 1
        print(f"\t* {matricola}: {sorted(s2d[matricola])} --> {to_change[matricola]}")
    print()

    #   the actual replacement is here <--------
    for matricola, dataset in to_change.items():
        s2d[matricola] = [dataset]

    # compute the new frequency
    new_data_freq = Counter()
    for _, dataset in s2d.items():
        new_data_freq.update(dataset)

    # display the result
    ascii_bar_chart(
        new_data_freq,
        title="> Distribution of HW1B datasets AFTER",
    )

    # Write the new csv
    with open(PATH.replace(".csv", "_AFTER.csv"), "w") as fout:
        writer = csv.writer(fout)
        writer.writerows(s2d.items())

    print("> CSV written.")
