import os


def process_table_file(input_path, output_folder):
    # First pass: get headers
    with open(input_path) as f:
        first_line = f.readline().strip()
        columns = first_line.split(',')

    # Second pass: process each row
    for line in open(input_path).readlines()[1:]:
        if not line.strip():
            continue  # skip empty lines
        
        current_dir = os.path.dirname(os.path.basename(input_path))
        file_num = len([x for x in os.listdir(current_dir) if os.path.isfile(x)])
        
        # Create filename based on first column (Topic)
        filename = f"{file_num}_from_{os.path.basename(line).strip().replace(' ', '')}.md"
        
        content_parts = []
        # Extract content rows from available columns
        for col in columns[1:]:  # skip the first column (title) or any others you specify as needed
            content_parts.append(f"{col.split(':')[1]}")

        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        except Exception as e:
            print(f"Error creating directory for {filename}: {e}")
            continue

        with open(filename, 'w') as f:
            markdown = f"# {os.path.basename(current_dir)}/\"{content_parts[0] if content_parts else '---'}{join('\n'.join(content_parts))}"  # Note: Join lines to form proper markdown text f.write(markdown)



def __main__():
    # Example usage with sample table.md in the same directory
    table_file_path = "table.md"
    output_dir = os.path.dirname(table_file_path)
    os.makedirs(output_dir, exist_ok=True)

    process_table_file(table_file_path, output_dir)
