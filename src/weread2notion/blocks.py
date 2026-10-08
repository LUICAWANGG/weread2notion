def get_heading(level, content):
    if level == 1:
        heading = "heading_1"
    elif level == 2:
        heading = "heading_2"
    else:
        heading = "heading_3"
    return {
        "type": heading,
        heading: {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content,
                    },
                }
            ],
            "color": "default",
            "is_toggleable": False,
        },
    }


def get_table_of_contents():
    """获取目录"""
    return {"type": "table_of_contents", "table_of_contents": {"color": "default"}}


def get_title(content):
    return {"title": [{"type": "text", "text": {"content": content}}]}


def get_rich_text(content):
    return {"rich_text": [{"type": "text", "text": {"content": content}}]}


def get_url(url):
    return {"url": url}


def get_file(url):
    return {"files": [{"type": "external", "name": "Cover", "external": {"url": url}}]}


def get_multi_select(names):
    return {"multi_select": [{"name": name} for name in names]}


def get_date(start):
    return {
        "date": {
            "start": start,
            "time_zone": "Asia/Shanghai",
        }
    }


def get_icon(url):
    return {"type": "external", "external": {"url": url}}


def get_select(name):
    return {"select": {"name": name}}


def get_status(name):
    return {"status": {"name": name}}


def get_number(number):
    return {"number": number}


def _safe_rich_text(content, max_units=1800):
    """Preserve long text by splitting it below Notion's 2000-unit limit.

    Count non-BMP characters as two units so emoji cannot exceed the limit.
    """
    content = str(content or "")
    segments = []
    current = []
    units = 0
    for character in content:
        size = 2 if ord(character) > 0xFFFF else 1
        if current and units + size > max_units:
            segments.append("".join(current))
            current = []
            units = 0
        current.append(character)
        units += size
    if current or not segments:
        segments.append("".join(current))
    return [{"type": "text", "text": {"content": segment}} for segment in segments]


def get_quote(content):
    return {
        "type": "quote",
        "quote": {
            "rich_text": _safe_rich_text(content),
            "color": "default",
        },
    }


def get_callout(content, icon=None):
    callout = {"rich_text": _safe_rich_text(content)}
    if icon:
        callout["icon"] = {"type": "emoji", "emoji": icon}
    return {
        "type": "callout",
        "callout": callout,
    }
