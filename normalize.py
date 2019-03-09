import csv


def normalize(filename, prefix, min_value, max_value, zero_strings=["Needs Grading", "In Progress", ""], output_filename="corrected.csv"):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        header = list(next(reader))
        output_sheet = []
        remainder = [row for row in reader]
        for row in remainder:
            output_row = list()
            for header_label, element in zip(header, row):
                output = element
                if header_label.startswith(prefix):
                    try:
                        if float(element) > max_value:
                            output = max_value
                    except ValueError:
                        pass
                    if element in zero_strings:
                        output = min_value
                output_row.append( str(output) )

            output_sheet.append(output_row)

        with open(output_filename, 'w') as o:
            writer = csv.writer(o, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow([str(item) for item in header])
            for row in output_sheet:
                writer.writerow(row)


if __name__ == '__main__':
    normalize("grades.csv", "Pre Lab", 0, 2)