def load_input_file(filename):
    reports = []

    with open(filename) as input_file:

        for report in input_file:
            report = report.strip().split(' ')

            for i in range(0, len(report)):
                report[i] = int(report[i])
            
            reports.append(report)

    return reports


def check_levels_all_decreasing(report):

    for i in range(len(report)-1):
        if report[i] < report[i+1]:
            return False
    
    return True


def check_levels_all_increasing(report):

    for i in range(len(report)-1):
        if report[i] > report[i+1]:
            return False
        
    return True


def check_levels_all_changing_gradually(report):

    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) not in range(1, 4):
            return False
        
    return True


def count_number_of_safe_reports(reports):
    number_of_safe_reports = 0

    for report in reports:
        if test_report_safety(report) == True:
            number_of_safe_reports += 1
        elif account_for_tolerance(report) == True:
            number_of_safe_reports += 1

    return number_of_safe_reports


def test_report_safety(report):
    all_increasing = check_levels_all_increasing(report)
    all_decreasing = check_levels_all_decreasing(report)

    if all_increasing or all_decreasing:
        if check_levels_all_changing_gradually(report):
            return True
    
    return False


def account_for_tolerance(report):
    for i in range(len(report)):
        test_safety_adjustments = report.copy()

        del test_safety_adjustments[i]
        
        if test_report_safety(test_safety_adjustments) == True:
            return True
        
    return False


if __name__ == '__main__':
    reports = load_input_file('input.txt')
    print(count_number_of_safe_reports(reports))