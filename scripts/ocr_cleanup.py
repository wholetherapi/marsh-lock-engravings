"""Clean up the OCR layer produced from the plate versos."""

import re

NOISE = re.compile(r"[^A-Za-z0-9 .,;:()\-]")


def clean(text: str) -> str:
    text = text.replace("\n", " ")
    text = NOISE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def merge_blocks(blocks: list[str]) -> str:
    return "\n".join(clean(block) for block in blocks if block.strip())
