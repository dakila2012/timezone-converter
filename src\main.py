import argparse
import sys
from datetime import datetime
import pytz

def main():
    parser = argparse.ArgumentParser(description='CLI tool for converting datetimes between timezones.')
    parser.add_argument('--from', required=True, dest='from_tz', help='Source timezone (e.g., UTC, America/New_York)')
    parser.add_argument('--to', required=True, dest='to_tz', help='Target timezone (e.g., Asia/Tokyo)')
    parser.add_argument('--now', action='store_true', help='Use current time')
    parser.add_argument('datetime_str', nargs='?', help='Datetime string in YYYY-MM-DD HH:MM:SS format')
    args = parser.parse_args()

    try:
        from_tz_obj = pytz.timezone(args.from_tz)
    except pytz.UnknownTimeZoneError:
        print(f"Error: Unknown source timezone '{args.from_tz}'", file=sys.stderr)
        sys.exit(1)

    try:
        to_tz_obj = pytz.timezone(args.to_tz)
    except pytz.UnknownTimeZoneError:
        print(f"Error: Unknown target timezone '{args.to_tz}'", file=sys.stderr)
        sys.exit(1)

    if args.now:
        if args.datetime_str is not None:
            parser.error("Cannot specify both --now and datetime_str")
        dt_from = datetime.now(from_tz_obj)
    else:
        if args.datetime_str is None:
            parser.error("Must specify datetime_str or --now")
        try:
            dt_naive = datetime.strptime(args.datetime_str.strip(), '%Y-%m-%d %H:%M:%S')
            dt_from = from_tz_obj.localize(dt_naive)
        except ValueError:
            parser.error("Invalid datetime format. Use YYYY-MM-DD HH:MM:SS")

    dt_to = dt_from.astimezone(to_tz_obj)
    print(dt_to.strftime('%Y-%m-%d %H:%M:%S %Z'))

if __name__ == "__main__":
    main()
