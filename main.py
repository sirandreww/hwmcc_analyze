# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv


def main():
    # Use a breakpoint in the code line below to debug your script.
    with open('hwmcc20-bv-all.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        unsolved_problems = []
        for row in reader:
            if row.count("sat") + row.count("uns") == 0:
                unsolved_problems.append(row)

    # write file
    with open('hwmcc20-bv-all-unsolved.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in unsolved_problems:
            writer.writerow(row)

    print(f"Number of unresolved = {len(unsolved_problems)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
