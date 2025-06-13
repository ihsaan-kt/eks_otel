## Thank you for your time and consideration. This project implements `telemetrygen` and `Amazon Distro for Opentelemetry` container to mock telemetry data onto working EKS cluster.


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
