import os , datetime

def read_log(file):
    try:
        with open(file=file, mode='r') as f:
            lines = f.read()
        return lines
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "don't have permission to access file"
    except Exception as e:
        print(f"Something else broke: {e}")


def validate_date(date):
    try:
        return datetime.date.fromisoformat(date)
    except ValueError:
        return False


def validate_time(time):
    try:
        return datetime.datetime.strptime(time, '%H:%M:%S')
    except:
        return False

def validate_level(info):
    if info.upper() in ['ERROR', 'WARN', 'INFO']:
        return info
    return False

def parse_line(line):
    # 2026-08-12 08:00:44 INFO service started successfully
    # check all parameters are correct values
    # check all parameters are present
    try:
        info = line.split()
        print(info)
        date_check = validate_date(info[0])
        time_check = validate_time(info[1])
        level_check = validate_level(info[2])
        if not bool(date_check):
            return '==BROKEN== Wrong Date format, continuing....'
        elif not bool(time_check):
            return '==BROKEN== wrong time format, continuing...'
        elif not bool(level_check):
            return '==BROKEN== wrong info label, continuing... '
        else:
            message = (' ').join(info[3:])
            return info[0], info[1], info[2], message
    except Exception as e:
        print(f"==BROKEN== Something else broke: {e}")

def total_lines():
    pass

def count_per_level():
    pass

def common_messages():
    pass

def save_report_to_json():
    pass

if __name__ == "__main__":
    print(os.getcwd())
    lines = read_log("sample.log")
    for line in lines.split('\n'):
        if bool(line.strip()):
            parsed_line = parse_line(line)
            print(parsed_line)
            if '==BROKEN==' not in parsed_line:
                (log_date, log_time, log_level, log_message) = parsed_line


  