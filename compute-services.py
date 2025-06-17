services:
  api_gateway:
    service: AWS API Gateway
    features: [rate_limiting, auth, caching]
  
  containers:
    service: Amazon EKS
    nodes: [m5.xlarge, c5.2xlarge]
    auto_scaling: horizontal_pod_autoscaler
  
  serverless:
    service: AWS Lambda
    functions: [pricing_calculator, churn_predictor]
    triggers: [api_gateway, kinesis, scheduled]
  
  ml_platform:
    service: Amazon SageMaker
    instances: [ml.m5.xlarge, ml.p3.2xlarge]
    features: [model_endpoints, batch_transform, pipelines]

storage:
  data_lake:
    service: Amazon S3
    buckets: [raw-data, processed-data, ml-models]
    lifecycle_policies: enabled
  
  databases:
    relational: Amazon RDS PostgreSQL (Multi-AZ)
    time_series: Amazon Timestream
    graph: Amazon Neptune
    cache: Amazon ElastiCache Redis
  
streaming:
  service: Amazon Kinesis
  streams: [cdr-stream, pricing-events, analytics-stream]
  retention: 7_days

