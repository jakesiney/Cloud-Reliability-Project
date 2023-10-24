import json
import requests


def lambda_handler(event, context):

    try:
        # Extract patient ID from the incoming request
        patient_id = int(event.get('pathParameters', {}).get('patient_id'))

        # Debug
        print("Incoming patient id HERE:", patient_id)

        # # Extract the body from the incoming event
        # request_body = event.get('body', '{}')
        request_body = json.loads(event['body'])

        # Convert the request body to JSON using double quotes for strings
        # request_body_json = json.dumps(request_body)

        # Debug
        print("First POST Request Payload:", request_body)

        # images = {"images": ["AOTLRTDWGVPKJHWYXQMSKDDPSQFKFTTEPPHFG", "NWLGBMHCEHIBYMKOPKBHQDEPPWOCCHNUOLVZFLSEMU"]}
        # Make a POST request to the API endpoint using the extracted patient_id and request body
        response = requests.post(f'http://35.177.47.173/patients/{patient_id}/screen', json=request_body, headers={
                                 'Content-type': 'application/json', 'Authorization': 'Basic dGVzdC1hY2NvdW50OnN1cGVyc2VjcmV0'})

        print(response.status_code, response.text)

        # Check the response from the POST request
        if response.status_code == 200:
            api_data = response.json()
            print("api data:", api_data)

            # Include the patient_id in the response data
            api_data['patient_id'] = patient_id

            # Include the request body data in the response
            api_data['request_body'] = request_body
            # print(api_data)
            return_value = api_data['request_body'] = request_body
            # Create the POST request body with title, body, and modified API response
            post_data = {
                "title": "Screen Results",
                # Include the entire API response here
                "body": json.dumps(api_data),
                "patient_id": patient_id,  # Include the patient_id in the post_data
                "staff_id": 27  # Staff ID (yours)
            }

            # Debug
            print("body in request", post_data)

            # Make a POST request to forward the modified response
            post_response = requests.post(
                'http://earth-reliability-server.animal-hospital.mkrs.link/notes',
                data=json.dumps(post_data),
                headers={
                    'Content-Type': 'application/json',
                    # Add your authorization header here
                    'Authorization': 'Basic dGVzdC1hY2NvdW50OnN1cGVyc2VjcmV0'
                }
            )

            # Check the response from the POST request
            if post_response.status_code == 200:  # Assuming 201 Created for a successful POST request
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
                    'body': response.text,
                    # 'body': json.dumps({'message': 'Successfully forwarded to the HOSP Server.'})
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        else:
            # Handle non-200 status codes from the POST request if necessary
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': 'Failed to fetch data from the API.'}),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }

    except Exception as e:
        # Handle any unexpected exceptions that might occur during the execution
        print("Error:", str(e))
        return {
            # 'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
