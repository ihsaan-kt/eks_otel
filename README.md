### tester EKS cluster with Opentelemetry collector

================================================

### - implements `telemetrygen` or `Amazon Distro for Opentelemetry` container to mock telemetry data


### - Deployment Terraform:
```
cd oteltrygen-eks
terraform init
terraform apply -auto-approve

aws eks --region <region> update-kubeconfig --name <cluster-name>`\
```


### - Deploy ADOT Collector:
`kubectl apply -f adot/collector-config.yaml`

### - Deploy Telemetry Generator:
`kubectl apply -f adot/telemetrygen-deployment.yaml`
