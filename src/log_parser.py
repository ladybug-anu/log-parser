import os 

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

def parse_line(line):
    # 2026-08-12 08:00:44 INFO service started successfully
    info = line.split()
    print(info)
    date = info[0]
    time = info[1]
    level = info[3]
    message = info[4:].join(' ')
    return date, time, level, message

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
    lines = read_log("../sample.log")
    for line in lines.split('\n'):
        log_date, log_time, log_level, log_message = parse_line(line)
        print(log_date, log_time, log_level, log_message)

  