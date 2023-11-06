import boto3


def lambda_handler(event, context):
    # Assuming you have appropriate IAM role permissions to interact with Athena
    athena_client = boto3.client('athena')

    # Athena query string
    query_string = "SELECT * FROM cloudfront_logs LIMIT 100;"

    # Athena query execution
    response = athena_client.start_query_execution(
        QueryString=query_string,
        QueryExecutionContext={
            'Database': 'earth_db'
        },
        ResultConfiguration={
            'OutputLocation': 's3://earth-lb-logs'
        }


    )
    # print("ResultConfiguration: ", ResultConfiguration)

    query_execution_id = response['QueryExecutionId']
    print("Query Execution ID: ", query_execution_id)
    # Wait for the query to complete
    while True:
        query_status = athena_client.get_query_execution(
            QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
        print(query_status)
        if query_status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break

    if query_status == 'SUCCEEDED':
        # Check if 'ResultConfiguration' is present in the response
        # if 'ResultConfiguration' in response:
        #     # Retrieve the results from the S3 location
        #     results_location = response['ResultConfiguration'].get('OutputLocation')

        # Generate a pre-signed URL for the CSV file
        s3_client = boto3.client('s3')
        bucket_name = 'earth-lb-logs'
        key = f'{query_execution_id}.csv'

        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600  # Link valid for 1 hour (adjust as needed)
        )

        # print(f"Your HOSP audit is available at: {presigned_url}")
        html_response = f'<html><body><h1>Your HOSP audit is here: <a href="{presigned_url}">Download CSV</a></h1></body></html>'
        # You can now include 'presigned_url' in your Lambda function response
        return {
            'statusCode': 200,
            'headers': {'content-type': 'text/html'},
            'body': html_response


            # 'body': f'Your HOSP audit is available at: {presigned_url}',
            # 'headers': {
            #     'Content-Disposition': 'attachment; filename=hosp_audit.csv'}
            # 'body': f'Your HOSP audit is available at: {presigned_url}'

        }
    else:
        # Handle the case where 'ResultConfiguration' is not present in the response
        print("Error: 'ResultConfiguration' not found in response")
        return {
            'statusCode': 500,
            'body': 'ResultConfiguration not found in response'
        }
# else:
#     # Handle query failure or cancellation
#     print(f"Query failed with status: {query_status}")
#     return {
#         'statusCode': 500,
#         'body': f'Query failed with status: {query_status}'
#     }
