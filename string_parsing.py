"""
Fetch IDs from logs. Two functions: one for string input, one for file.
"""


def fetch_ids_from_string(log_content: str) -> list[str]:
    """Extract IDs from log string. Splits by spaces/commas/semicolons, keeps tokens that look like IDs."""
    if not log_content:
        return []

    # Replace common separators with spaces, then split
    cleaned = log_content.replace(",", " ").replace(";", " ").replace("|", " ")
    tokens = cleaned.split()

    ids = []
    for token in tokens:
        token = token.strip()
        
        # Handle id=value or id:value - extract the value part
        if "=" in token:
            parts = token.split("=", 1)
            token = parts[1] if len(parts) > 1 else parts[0]
        elif ":" in token:
            parts = token.split(":", 1)
            token = parts[1] if len(parts) > 1 else parts[0]
        
        # Remove quotes if present
        if token.startswith('"') and token.endswith('"'):
            token = token[1:-1]
        if token.startswith("'") and token.endswith("'"):
            token = token[1:-1]
        
        token = token.strip()
        
        # Check if it looks like an ID: alphanumeric, underscore, or hyphen
        if token and all(ch.isalnum() or ch in "_-" for ch in token):
            ids.append(token)

    # Remove duplicates, keep order
    result = []
    seen = set()
    for id_val in ids:
        if id_val not in seen:
            seen.add(id_val)
            result.append(id_val)
    
    return result


def fetch_ids_from_file(file_path: str) -> list[str]:
    """Read log file and return IDs. Uses fetch_ids_from_string on the file contents."""
    with open(file_path) as f:
        return fetch_ids_from_string(f.read())


if __name__ == "__main__":
    # Example: string
    s = "id=100 id=42 abc-123 req_xyz"
    print(fetch_ids_from_string(s))  # ['100', '42', 'abc-123', 'req_xyz']

    # Example: file
    with open("sample.log", "w") as f:
        f.write("id=1, id=2; req_xyz| abc-123\n")
    print(fetch_ids_from_file("sample.log"))  # ['1', '2', 'req_xyz', 'abc-123']
