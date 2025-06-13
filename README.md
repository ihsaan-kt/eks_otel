## tester EKS cluster with Opentelemetry collector


## implements `telemetrygen` or `Amazon Distro for Opentelemetry` container to mock telemetry data


## Deploying Terraform:
```
cd oteltrygen-eks
terraform init
terraform apply -auto-approve
```

## exporting AWS credentials and updating kubeconfig context:
```
export AWS_ACCESS_KEY_ID=<your_access_key_here>
export AWS_SECRET_ACCESS_KEY=<your_secret_key_here>
aws eks --region <region> update-kubeconfig --name <cluster-name>
```



##  Deploy ADOT Collector:
```
kubectl apply -f adot/collector-config.yaml
```

## Deploy Telemetry Generator:
```
kubectl apply -f adot/telemetrygen-deployment.yaml
```
