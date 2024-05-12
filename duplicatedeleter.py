def remove_duplicates(file_path):
    # open input file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # create a dictionary to store unique lines and their order of occurrence
    unique_lines = {}
    for line in lines:
        if line.strip() not in unique_lines:
            unique_lines[line.strip()] = len(unique_lines)

    # write unique lines to output file in the order they appeared in the input file
    with open("output.txt", "w") as f:
        for line in lines:
            stripped_line = line.strip()
            if stripped_line in unique_lines:
                f.write(line)
                unique_lines.pop(stripped_line)


remove_duplicates('data.txt')