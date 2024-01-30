import requests

api_url = "https://invenio-dev.hcommons-staging.org"
api_key = "playholder for security"
api_endpoint = "api/records"

def get_api_data(base_url, endpoint, api_key):
    url = f"{base_url}/{endpoint}"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
 
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
 
        return response.json()
 
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
 
data = get_api_data(api_url, api_endpoint, api_key)

#show the data and check
if data:
    print(data)
else:
    print("No data retrieved.")

#check how many records i am getting
if data and 'hits' in data and 'hits' in data['hits']:

    total_records = len(data['hits']['hits'])
    print(f"Total records: {total_records}")
 
    # only get the first x records
    for record in data['hits']['hits'][:10]:  # Slicing to get the first 10 records

        try:
            record_id = record['id']
            print(f"Record ID: {record_id}")
 
            languages = record['metadata'].get('languages', [])
            for language in languages:
                print(f"Language: {language['id']}")
 
            file_entries = record['files'].get('entries', {})
            for file_name, file_info in file_entries.items():
                print(f"File Name/ID: {file_name}")
 
        except KeyError as e:
            print(f"Error in record {record.get('id', 'Unknown')}: Missing key {e}")

        except Exception as e:
            print(f"An unexpected error occurred in record {record.get('id', 'Unknown')}: {e}")

else:
    print("No records found.")
