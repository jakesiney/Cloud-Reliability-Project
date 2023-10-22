import json
import requests


def results_handler(event, context):
    try:
        # Extract patient ID from the incoming request
        patient_id = int(event.get('pathParameters', {}).get('patient_id'))

        # Make a GET request to the API endpoint using the extracted patient_id
        response = requests.get(
            f'http://earth-reliability-server.animal-hospital.mkrs.link/patients/{patient_id}/screen')

        # Process the response data
        if response.status_code == 200:
            api_data = response.json()

            # Include the patient_id in the response data
            api_data['patient_id'] = patient_id

            # Create the POST request body with title, body, and modified API response
            post_data = {
                "title": "Screen Results",
                # Include the entire API response here
                "body": json.dumps(api_data),
                "patient_id": patient_id  # Include the patient_id in the post_data
            }

            # Make a POST request to forward the modified response
            post_response = requests.post(
                'http://earth-reliability-server.animal-hospital.mkrs.link/notes',
                data=json.dumps(post_data),
                headers={
                    'Content-Type': 'application/json',
                    # Add your authorization header here
                    'Authorization': 'Basic XXXXXXXXXXXXX'
                }
            )

            # Check the response from the POST request
            if post_response.status_code == 201:  # Assuming 201 Created for a successful POST request
                return {
                    'statusCode': 200,
                    'body': json.dumps({'message': 'Response forwarded successfully.'}),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                # Handle non-201 status codes from the POST request if necessary
                return {
                    'statusCode': post_response.status_code,
                    'body': json.dumps({'error': 'Failed to forward response.'}),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        else:
            # Handle non-200 status codes if necessary
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': 'Internal Server Error'}),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
    except Exception as e:
        # Handle exceptions and errors
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
