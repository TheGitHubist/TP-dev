import requests
import sys
import os

def get_content(url) :
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        sys.exit(1)
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Error connecting: {conn_err}')
        sys.exit(1)
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')
        sys.exit(1)

def write_content(content, file):
    try:
        with open(file, 'w') as f:
            f.write(content)
        print(f'Content saved to {file}')
    except Exception as e:
        print(f'Error writing to file: {e}')

def main(file_to_urls):
    urls = []
    with open(file_to_urls, 'r') as f:
        for line in f:
            urls.append(line.strip())
    for url in urls:
        content = get_content(url)
        file_name = 'web_' + os.path.basename(url)
        write_content(content, file_name)

if __name__ == "__main__":
    main(sys.argv[1])