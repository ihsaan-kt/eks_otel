output "cluster_name" {
  value = module.eks.cluster_name
}

output "adot_irsa_role_arn" {
  value = aws_iam_role.adot_irsa.arn
}
