data "aws_iam_policy_document" "adot_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Federated"
      identifiers = [module.eks.oidc_provider_arn]
    }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test     = "StringEquals"
      variable = "${module.eks.oidc_provider}:sub"
      values   = ["system:serviceaccount:default:adot-collector"]
    }
  }
}

resource "aws_iam_role" "adot_irsa" {
  name               = "adot-collector-irsa"
  assume_role_policy = data.aws_iam_policy_document.adot_assume_role.json
}

resource "aws_iam_policy" "adot_policy" {
  name   = "adot-collector-policy"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = [
          "xray:PutTraceSegments",
          "xray:PutTelemetryRecords",
          "logs:PutLogEvents",
          "logs:CreateLogStream",
          "logs:CreateLogGroup",
          "cloudwatch:PutMetricData"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "adot_attach" {
  role       = aws_iam_role.adot_irsa.name
  policy_arn = aws_iam_policy.adot_policy.arn
}
