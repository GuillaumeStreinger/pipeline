import json

def generate_html(json_file, output_html):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # HTML Header
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SBOM Viewer</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                padding: 20px;
                background-color: #f4f4f9;
                color: #333;
            }}
            h1, h2 {{
                color: #0078d7;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            table, th, td {{
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #0078d7;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>SBOM</h1>
        <h2>Metadata</h2>
        <p><strong>BOM Format:</strong> {bom_format}</p>
        <p><strong>Specification Version:</strong> {spec_version}</p>
        <p><strong>Version:</strong> {version}</p>
        <p><strong>Timestamp:</strong> {timestamp}</p>

        <h2>Components</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Version</th>
                <th>Type</th>
                <th>Description</th>
                <th>License</th>
                <th>Publisher</th>
            </tr>
    """.format(
        bom_format=data['bomFormat'],
        spec_version=data['specVersion'],
        version=data['version'],
        timestamp=data['metadata']['timestamp']
    )

    # Add Components
    for component in data.get('components', []):
        html_content += """
        <tr>
            <td>{name}</td>
            <td>{version}</td>
            <td>{type}</td>
            <td>{description}</td>
            <td>{license}</td>
            <td>{publisher}</td>
        </tr>
        """.format(
            name=component.get('name', 'N/A'),
            version=component.get('version', 'N/A'),
            type=component.get('type', 'N/A'),
            description=component.get('description', 'N/A'),
            license=component.get('licenses', [{'license': {'id': 'N/A'}}])[0]['license'].get('id', 'N/A'),
            publisher=", ".join([author.get('name', '') for author in component.get('authors', [])]) or 'N/A'
        )

    # HTML Footer
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write to output file
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Usage
generate_html('sbom.json', 'sbom.html')
