import boto3

def main():
    
    # Boto3 Client
    client = boto3.client('s3')

    # Define results files
    results = open("files/backout/results.txt", "w")
    errors = open("files/backout/errors.txt", "w")

    # Read text file
    with open("files/buckets.txt", "r") as output:

        for line in output.readlines():

            bucket_name = line.strip()

            print(f"Processing bucket {bucket_name}")

            try:
                response = client.delete_bucket_encryption(
                    Bucket=bucket_name,
                )
                
                results.write(f"Results for {bucket_name}:\n\n")
                results.write("OK")
                results.write("====================================\n\n\n")
            except Exception as e:
                errors.write(f"Error for {bucket_name} err: {e}:\n\n")



if __name__ == "__main__":
    main()

