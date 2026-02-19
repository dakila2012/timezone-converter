# Timezone Converter

A lightweight CLI tool for converting datetimes between timezones. It supports parsing specific datetime strings in `YYYY-MM-DD HH:MM:SS` format or using the current time (`--now`), with accurate handling of timezone offsets and Daylight Saving Time via `pytz`. Required source (`--from`) and target (`--to`) timezones are validated, and clear error messages are provided for invalid inputs.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/timezone-converter.git
   cd timezone-converter
   ```

2. Install the dependency:
   ```
   pip install pytz
   ```

3. Run the tool:
   ```
   python src/main.py --help
   ```

## Usage

```
usage: main.py [-h] --from FROM_TZ --to TO_TZ [--now] [datetime_str]

CLI tool for converting datetimes between timezones.

positional arguments:
  datetime_str    Datetime string in YYYY-MM-DD HH:MM:SS format

options:
  -h, --help      show this help message and exit
  --from FROM_TZ  Source timezone (e.g., UTC, America/New_York)
  --to TO_TZ      Target timezone (e.g., Asia/Tokyo)
  --now           Use current time
```

### Examples

- Show help:
  ```
  python src/main.py --help
  ```

- Convert specific UTC datetime to America/New_York:
  ```
  python src/main.py --from UTC --to America/New_York "2023-10-01 12:00:00"
  ```
  Output: `2023-10-01 08:00:00 EDT`

- Convert current time from Europe/London to Asia/Tokyo:
  ```
  python src/main.py --from Europe/London --to Asia/Tokyo --now
  ```
  Output: `2026-02-19 09:22:41 JST` (example; actual output uses current time)

## Features

- Supports specific datetime input (`YYYY-MM-DD HH:MM:SS`) or current time (`--now`)
- Required `--from` and `--to` timezones with `pytz` validation
- Automatic handling of DST and timezone localization
- Mutually exclusive `--now` and datetime argument with `parser.error`
- Invalid timezone or format errors printed to stderr with exit code 1
- Clean output format: `YYYY-MM-DD HH:MM:SS TZ`

## Dependencies

- Python 3.x (stdlib: `argparse`, `datetime`, `sys`)
- `pytz` (for timezone handling)

## License

MIT License - see [LICENSE](LICENSE) for details.