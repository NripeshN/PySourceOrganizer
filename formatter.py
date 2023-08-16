import ast
from typing import Tuple, List


def extract_node_with_leading_comments(
    node: ast.AST, source_code: str
) -> Tuple[str, ast.AST]:
    """Extract the source code of a node along with its leading comments, decorators, and whitespaces."""
    if hasattr(node, "decorator_list"):
        start_line = (
            node.decorator_list[0].lineno if node.decorator_list else node.lineno
        )
    else:
        start_line = node.lineno

    end_line = getattr(node, "end_lineno", node.lineno)

    lines = source_code.splitlines()
    extracted_lines = []

    # Get the actual code for the node
    for line_num in range(start_line - 1, end_line):
        extracted_lines.append(lines[line_num])

    # Get the leading comments and whitespaces
    for line_num in range(start_line - 2, -1, -1):
        stripped = lines[line_num].strip()
        if not stripped or stripped.startswith("#"):
            extracted_lines.insert(0, lines[line_num])
        else:
            break

    return "\n".join(extracted_lines), node


def extract_all_nodes_with_comments(
    tree: ast.AST, source_code: str
) -> List[Tuple[str, ast.AST]]:
    """Extract all the nodes in the AST with their associated comments and whitespaces."""
    return [extract_node_with_leading_comments(node, source_code) for node in tree.body]


def rearrange_functions_and_classes(source_code: str) -> str:
    """Rearrange classes and functions in source code alphabetically with comments."""
    tree = ast.parse(source_code)

    nodes_with_comments = extract_all_nodes_with_comments(tree, source_code)

    # Define a helper function to determine sorting precedence
    def sort_key(item):
        node = item[1]
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return (0, 0, getattr(node, "name", ""))
        if isinstance(node, ast.ClassDef):
            return (1, 0, node.name)
        if isinstance(node, ast.FunctionDef):
            return (2, 0, node.name)
        return (3, 0, getattr(node, "name", ""))

    # Sort nodes
    nodes_sorted = sorted(nodes_with_comments, key=sort_key)

    return "\n".join([code for code, _ in nodes_sorted]).strip()


def main(file_path: str):
    """Read, rearrange, and write back to the file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        reordered_code = rearrange_functions_and_classes(original_code)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(reordered_code)

    except SyntaxError:
        print(
            f"Error: The provided file '{file_path}' does not contain valid Python code."
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide the path to a Python file as an argument.")
    else:
        main(sys.argv[1])
