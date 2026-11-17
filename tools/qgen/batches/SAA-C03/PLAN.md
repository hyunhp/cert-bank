# SAA-C03 exam-level set (b11-b12) + expert tier (b13-b14), 2026-11-17

Why: same gap as DEA-C01 (owner: 78% on our mock vs 45% on AWS's official practice set). SAA-C03 has only 24
exam-tier questions (tier_of: stem >= 55 words and options >= 13 words, or Select THREE). Rules are the DEA-C01 ones
(`tools/qgen/batches/DEA-C01/PLAN.md`); this file only splits topics. Never reuse official wording/scenarios/options.

## b11-b12 (level `advanced`, 30 each): DEA-C01 "hard set" style
Stem 60-90 words, 2-3 binding constraints, deciding criterion named; options 15-30 words, each wrong one workable
but fails exactly one constraint; ~20% multi-answer, >= 2 "(Select THREE)" per batch; G/W/X/T + `# src:` lines.
- b11: D1 Design Secure Architectures (16) + D2 Design Resilient Architectures (14)
  IAM policy evaluation across accounts (SCPs, permission boundaries, resource policies), KMS key policies/grants,
  S3 Block Public Access / Object Ownership / access points, VPC endpoints + endpoint policies, WAF/Shield/CloudFront
  OAC, Cognito vs IAM Identity Center, Secrets Manager rotation; Multi-AZ vs read replicas vs Aurora Global Database,
  RPO/RTO with backup/pilot light/warm standby, Route 53 failover/latency routing, SQS/SNS/EventBridge decoupling,
  Auto Scaling health checks with ELB.
- b12: D3 Design High-Performing Architectures (16) + D4 Design Cost-Optimized Architectures (14)
  Storage choice (EBS gp3/io2, EFS throughput modes, FSx variants, S3 performance), ElastiCache vs DAX vs read
  replicas, CloudFront caching, Global Accelerator, Kinesis vs SQS vs MSK throughput, Lambda concurrency;
  Savings Plans vs Reserved vs Spot under a stated usage pattern, S3 storage-class/lifecycle cost with minimum
  durations and retrieval fees, NAT gateway / data transfer costs vs VPC endpoints, right-sizing with Compute Optimizer.

## b13-b14 (level `expert`, 20 each): DEA-C01 "expert tier" rules
90-140-word scenarios, 3-4 constraints (one hidden in the details), worked numbers from documented limits/prices,
two-service seams, evidence-based troubleshooting, options that differ in one configuration detail, ~30%
multi-answer (half Select THREE). Reviewer blind-solves every question before reading the key.
- b13: D1 (10) + D2 (10)   cross-account access chains, KMS + S3/EBS/RDS snapshot sharing, endpoint policy +
  bucket policy seams, DR math (RPO/RTO vs replication lag, backup windows), multi-Region failover evidence.
- b14: D3 (10) + D4 (10)   throughput/IOPS math (EBS, EFS, DynamoDB, Kinesis shards), caching hit-ratio
  tradeoffs, cost math across two designs (data transfer, NAT, storage classes with minimum durations, Savings Plans).
No overlap with each other or published SAA-C03 questions (check --siblings).
