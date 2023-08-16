import token
import tokenize
from io import BytesIO
from typing import List


def extract_top_level_definitions(
    tokens: List[tokenize.TokenInfo],
) -> List[List[tokenize.TokenInfo]]:
    """Extract top-level classes and functions as separate token groups."""
    definitions = []
    buffer = []
    depth = 0
    for tok in tokens:
        if tok.type == token.INDENT:
            depth += 1
        if tok.type == token.DEDENT:
            depth -= 1

        buffer.append(tok)

        if depth == 0 and (tok.type == token.NEWLINE or tok.type == token.ENDMARKER):
            if buffer:
                definitions.append(buffer)
                buffer = []

    return definitions


def rearrange_code_using_tokens(source_code: str) -> str:
    tokens = list(tokenize.tokenize(BytesIO(source_code.encode()).readline))

    top_level_definitions = extract_top_level_definitions(tokens)

    def sort_key(toks: List[tokenize.TokenInfo]):
        for t in toks:
            if t.type == token.NAME:
                return t.string
        return ""

    sorted_definitions = sorted(top_level_definitions, key=sort_key)

    reordered_tokens = []
    for chunk in sorted_definitions:
        reordered_tokens.extend(chunk)

    # Construct source code from reordered tokens
    output = "".join(
        tok.string for tok in reordered_tokens if tok.type != token.ENDMARKER
    )

    return output


def main(file_path: str):
    """Read, rearrange, and write back to the file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        reordered_code = rearrange_code_using_tokens(original_code)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(reordered_code)

    except (tokenize.TokenError, SyntaxError):
        print(
            f"Error: The provided file '{file_path}' does not contain valid Python code."
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide the path to a Python file as an argument.")
    else:
        main(sys.argv[1])
