# Roadmap: NLP for Invenio Data
This document records our plan for further work in 2024.

Creator: Tianyi Kou-Herrema; December 2023

## Introduction
In the Fall semester 2023, TKH tested python libraries for text extraction. CL created a cli function to extract stats from Invenio. Our goal for the coming semester is to combine our tasks and really delve into Invenio's current data and write clis to extract, preprocess, and analyze data, potentially provide visualizations for various stakeholders.

### Workflow Overview (General)

1. Access files at Invenio using API
- Cassie has extensive experience on this
2. Write CLI for downloading files locally (or in the space HPCC provides)
- Write a script that interfaces with the API to list and download files
- Anything else?
3. Examine and process file types
- Identify the file type after downloading
- For each type of files, we will apply one/multiple python libraries to extract textual data. !!! Here we also have to think about how to store metadata or is that something Cassie can extract based on her experience working with stats???
4. Store extracted data in a dataframe and export to .json file(s)
- Maybe use *pandas* to create a dataframe?
- Export this dataframe using 'pandas.DataFrame.to_json()'
5. Delete files post-extraction
- Ensure data is stored correctly, maybe manually testing?
- Use python's 'os' module to delete files
6. Output for further analysis
- Ensure the .json file is accessible, make copies in the cloud (check copyright regulations)?
- Verify or modify json structure for further analysis

### Detailed Workflow with Python (Some initial code)
1. Access file using API:
@Cassie
2. Download files:

*Remember to install packages first, `pip install click`.*

```Python
import click
import requests

@click.group()
def cli():
    """File Downloader CLI"""
    pass

@click.command()
@click.option('--api-url', prompt='API URL',
              help='The API URL to fetch file information.')
@click.option('--auth-token', prompt='Auth Token', hide_input=True,
              help='Authentication token for API access.')

def download(api_url, auth_token):
    """
    Download files from the given API URL.
    """

    headers = {'Authorization': f'Bearer {auth_token}'}

    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        click.echo("Failed to fetch files.")
        return

    files = response.json()

    for file in files:
        file_url = file['url']
        file_name = file['name']

        # Download the file
        click.echo(f'Downloading {file_name}...')
        file_response = requests.get(file_url, headers=headers)
        if file_response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
        else:
            click.echo(f"Failed to download {file_name}")

    click.echo("Download completed.")

cli.add_command(download)

if __name__ == '__main__':
    cli()
```

```console
python download_cli.py --api-url "https://invenio.com/api/files?" --auth-token "your_auth_token"
```

3. Data Extraction

```Python
TBD
```

4. Store Data in .json file


5. Delete Files

```Python
for file in files:
  os.remove(file[])
```

### Other Considerations:
- Error Handling:
If we are dealing with large amount of data, maybe we can do it in different batch? What would we do if one file is corrupted? Things like that.
- Data Security:  
- Efficiency:
Check out HPCC's resource; Maybe looking into batching if we are dealing with large numbers of files.
- Testing:
We definitely need to test each component in smaller quantity before integrating.

### Prior to our analysis
There are other scholarly work we need to examine before deciding how to combine stats and textual data and conduct analysis.
