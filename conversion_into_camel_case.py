def to_camel_case(name: str) -> str:
    words = name.split("_")
    return "".join([word.title() for word in words])
