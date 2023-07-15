import tabula

pdf_path = "MyGrades.pdf"

tables = tabula.read_pdf(pdf_path, pages=2)

merge_column = []
finalunits = []

for grade2 in tables:
    filtered_table = grade2[
        ~grade2.iloc[:, 8]
        .astype(str)
        .str.contains(
            "Total Units :|1st Semester SY 2022-2023|2nd Semester SY 2022-2023"
        )
    ]
    filtered_table = filtered_table.dropna(subset=[filtered_table.columns[8]])
    grade2_column = filtered_table.iloc[:, 8]
    

    if not filtered_table.iloc[:, 8].empty:
        for unit in tables:
            filtered_table = unit[
                ~unit.iloc[:, 3]
                .astype(str)
                .str.contains(
                    "Total Units :|1st Semester SY 2022-2023|2nd Semester SY 2022-2023"
                )
            ]
            filtered_table = filtered_table.dropna(subset=[filtered_table.columns[3]])
            unit_column = filtered_table.iloc[:, 3]
        for grades in tables:
            filtered_table = grades[
                ~grades.iloc[:, 7]
                .astype(str)
                .str.contains(
                    "Total Units :|1st Semester SY 2022-2023|2nd Semester SY 2022-2023"
                )
            ]
            filtered_table = filtered_table.dropna(subset=[filtered_table.columns[2]])
            grade_column = filtered_table.iloc[:, 7]

        computations = 0
        total_grades = 0
        total_units = 0
        ave = 0
        for value in unit_column.dropna():
            if value > 10:
                pass
            else:
                finalunits.append(value)
        print()
        for value2 in grade_column.dropna():
            merge_column.append(value2)
        for grade2 in grade2_column.dropna():
            merge_column.append(grade2)
        print(merge_column)
        print(finalunits)
        for i in range(len(merge_column)):
            computations = finalunits[i] * grade_column
            total_grades = total_grades + computations
            total_units = total_units + finalunits[i]
        ave = total_grades / total_units
        print(f'{ave}')

