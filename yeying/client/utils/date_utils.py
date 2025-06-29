from datetime import datetime, timedelta, timezone

from dateutil import parser
from dateutil import tz


def get_current_utc_datetime():
    return convert_to_utc_datetime(datetime.now())


def get_current_utc_string():
    return format_datetime(get_current_utc_datetime())


def get_current_iso_string():
    now_utc = datetime.now(timezone.utc)
    return now_utc.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def parse_datetime(s):
    return parser.isoparse(s)


def is_expired(s, minutes):
    # 解析ISO字符串
    time_parsed = parse_datetime(s)

    # 获取当前时间并保留时区信息
    now = datetime.now(time_parsed.tzinfo)

    # 计算5分钟之后的时间
    five_minutes_later = time_parsed + timedelta(minutes=minutes)

    # 比较时间，判断是否超过5分钟之后
    return now > five_minutes_later


def format_datetime(dt):
    formatted_dt = dt.isoformat(timespec="milliseconds")
    return formatted_dt.replace("+00:00", "Z")


def convert_to_local_datetime(dt):
    return dt.astimezone(tz.tzlocal())


def convert_to_utc_datetime(dt):
    return dt.astimezone(tz.tzutc())
