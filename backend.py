def extract_text(msg):
    if isinstance(msg, dict):
        return msg.get("content") or msg.get("text") or msg.get("message") or str(msg)
    if hasattr(msg, "content"):
        return getattr(msg, "content")
    return str(msg)
