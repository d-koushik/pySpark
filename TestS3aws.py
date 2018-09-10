import boto3
import pandas as pd
# Accessing all available buckets from s3
s3bucketResource = boto3.resource('s3')
for bckt in s3bucketResource.buckets.all():
        print(bckt.name)

"""There are two main tools we can use to access S3: clients and resources. 
Clients are low-level functional interfaces, while resources are high-level object-oriented interfaces.
We can typically use clients to load single files and bucket resources to iterate over all items in a bucket"""

client = boto3.client('s3')
obj1 = client.get_object(Bucket='csv-koushik', Key='Employees.csv')
obj2 = client.get_object(Bucket='csv-koushik', Key='Employees.csv')
df = pd.read_csv(obj1['Body'])
print("-----Printing Data-frame ------")
print(df)
print("------ Printing all employees with age less than 30 ------- ")
df = pd.read_csv(obj2['Body'], usecols=['Name', 'Age'])
print(df[df['Age'] < 30.0])
df = df[df['Age'] < 30.0]
df.to_csv(r'employeesAgeLess30.csv', header=None, index=None, sep=',', mode='a')
# f = open("demofile.txt", "w")
# f.write(df[df['Age'] < 30.0])


print("\nList down all Files inside a folder of the bucket: csv-koushik")
my_bucket = s3bucketResource.Bucket('csv-koushik')  # subsitute this for your s3 bucket name.
files = list(my_bucket.objects.filter(Prefix='TestFolder'))
x=len(files)
for i in range(0, x):
    print("Object ", str(i+1), ": ", files[i])



