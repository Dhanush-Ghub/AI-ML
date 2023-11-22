/* 4. a)*/
% Student Info & Percentage Calculation
subject('Math', 100, 90).
subject('Science', 100, 85).
subject('English', 100, 75).
subject('History', 100, 80).
subject('Art', 100, 70).
subject('Computer', 100, 95).

calculate_percentage(Student, Percentage) :-
    findall(Marks, subject(_, _, Marks), AllMarks),
    sum_list(AllMarks, Total),
    length(AllMarks, NumSubjects),
    Percentage is Total / (NumSubjects * 100) * 100,
    format('Student: ~w, Percentage: ~2f%', [Student, Percentage]).


/* 4. b)*/

% Employee Information & Salary Calculation
employee_info('IT', 'Developer', 'John', 30, 50000, 15000).

calculate_salary(Department, Designation, Name, Age, BasicSalary, HRA) :-
    DA is 0.15 * BasicSalary,
    GrossSalary is BasicSalary + HRA + DA,
    format('Department: ~w, Designation: ~w, Name: ~w, Age: ~w~nBasic Salary: ~w~nHRA: ~w~nDA: ~w~nGross Salary: ~w', [Department, Designation, Name, Age, BasicSalary, HRA, DA, GrossSalary]).
