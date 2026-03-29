from logic import calculate_hours from validator import validate_hours hours = [8,8,7,9] if validate_hours(hours): print(calculate_hours(hours)) else: print('Invalid data')
