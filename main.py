<<<<<<< HEAD
import logging from logic import calculate_hours from validator import validate_hours hours = [8,8,7,9] if validate_hours(hours): logging.info(calculate_hours(hours)) else: logging.error('Invalid data')

=======
import logging from logic import calculate_hours from validator import validate_hours logging.basicConfig(level-logging.INFO) hours = [8,8,7,9] if validate_hours(hours): logging.info(calculate_hours(hours)) else: logging.error('Invalid data')
>>>>>>> 5643597 (fix logging configuration)
