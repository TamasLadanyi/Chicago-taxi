![Chicago taxi](https://github.com/user-attachments/assets/bd58e32b-4dbf-41a3-9b4a-a4741db3f910)

This is my first project, which also serves as a learning experience.
The goal of the project is to provide an overview of Chicago taxi activity throughout the day using daily updated data. It utilizes open-source APIs, including one provided by data.cityofchicago.org. Additionally, data from the open-meteo.com API is also incorporated.
The project can be divided into two main parts:

First part: AWS cloud platform, automatically data extraction and transformation.

Extracting taxi trip and weather data from the APIs and transforming it. (The extracting of taxi trips data is performed at T-2 months whit this way I can simulate the daily updating since the Chicago API is updated monthly.) 
The transformation process involves creating master and dimension tables (for date, payment type and community areas of Chicago), as well as removing clearly inaccurate data. 
All steps are executed on a cloud platform, using AWS. Data storage is handled through S3, 	while data transformations are performed using AWS Lambda functions.
 
Second part:

This section involves utilizing the Boto3 client to get weather and taxi trip data. These  data is then integrated into a final DataFrame, which can be queried using pandasql. After that visualizations can be generated as required.
	
