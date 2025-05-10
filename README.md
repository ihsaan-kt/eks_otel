### tester EKS cluster with Opentelemetry collector

================================================

## `oteltrygen-eks/` 
### - implements `telemetrygen` container to mock telemetry data


### - Deployment Terraform:

`terraform init`
`terraform apply -auto-approve`

`aws eks --region <region> update-kubeconfig --name <cluster-name>`

### - Deploy Karpenter (if required):
`helm repo add karpenter https://charts.karpenter.sh`
`helm repo update`
`helm install karpenter karpenter/karpenter -f karpenter/values.yaml`

### - Deploy ADOT Collector:
`kubectl apply -f adot/collector-config.yaml`

### - Deploy Telemetry Generator:
`kubectl apply -f adot/telemetrygen-deployment.yaml`
