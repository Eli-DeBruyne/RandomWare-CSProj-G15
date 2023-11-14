import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.in_loop = False
        self.opening_files = False
        self.encrypting_files = False

    def visit_For(self, node):
        self.in_loop = True
        self.generic_visit(node)

    def visit_While(self, node):
        self.in_loop = True
        self.generic_visit(node)

    def visit_With(self, node):
        for item in node.items:
            if isinstance(item.context_expr, ast.Call) and isinstance(item.context_expr.func, ast.Name):
                if item.context_expr.func.id == 'open':
                    self.opening_files = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'encrypt':
            self.encrypting_files = True
        self.generic_visit(node)

def analyze_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        code = file.read()

    # Parse the code into an AST
    parsed_code = ast.parse(code)

    # Create an analyzer instance and visit the AST
    analyzer = CodeAnalyzer()
    analyzer.visit(parsed_code)

    return {
        'in_loop': analyzer.in_loop,
        'opening_files': analyzer.opening_files,
        'encrypting_files': analyzer.encrypting_files
    }

# Example usage
file_path = 'C:/Users/Pause/Documents/antivirus/virus/virus.py'
results = analyze_file(file_path)
print(results)
