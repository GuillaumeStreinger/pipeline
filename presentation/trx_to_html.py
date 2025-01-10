import xml.etree.ElementTree as ET

def generate_html_from_trx(trx_file, output_html):
    tree = ET.parse(trx_file)
    root = tree.getroot()

    namespace = {'ns': 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'}

    # Extract metadata
    test_run = root.attrib
    result_summary = root.find('ns:ResultSummary', namespace)
    counters = result_summary.find('ns:Counters', namespace).attrib

    # Start building the HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test Results</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #0078d7; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            table, th, td {{ border: 1px solid #ddd; }}
            th, td {{ padding: 10px; text-align: left; }}
            th {{ background-color: #0078d7; color: white; }}
        </style>
    </head>
    <body>
        <h1>Test Results</h1>
        <p><strong>Test Run ID:</strong> {test_run['id']}</p>
        <p><strong>Name:</strong> {test_run['name']}</p>
        <p><strong>Total Tests:</strong> {counters['total']}</p>
        <p><strong>Passed:</strong> {counters['passed']}</p>
        <p><strong>Failed:</strong> {counters['failed']}</p>
        <p><strong>Duration:</strong> {root.find('ns:Times', namespace).attrib['finish']}</p>

        <h2>Test Details</h2>
        <table>
            <tr>
                <th>Test Name</th>
                <th>Outcome</th>
                <th>Duration</th>
                <th>Start Time</th>
                <th>End Time</th>
            </tr>
    """

    # Extract test results
    results = root.find('ns:Results', namespace)
    for result in results.findall('ns:UnitTestResult', namespace):
        html_content += f"""
        <tr>
            <td>{result.attrib['testName']}</td>
            <td>{result.attrib['outcome']}</td>
            <td>{result.attrib['duration']}</td>
            <td>{result.attrib['startTime']}</td>
            <td>{result.attrib['endTime']}</td>
        </tr>
        """

    # Close HTML
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write to the output HTML file
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Usage
generate_html_from_trx('test-results.trx', 'test-results.html')