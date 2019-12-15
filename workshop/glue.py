from aws_cdk import (
    aws_glue as glue,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as _s3,
    aws_s3_assets as s3_assets,
    aws_sns_subscriptions as subs,
    core
)

class GlueJob (core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        script_as_asset = s3_assets.Asset(self, "scriptasset", path="./glue/transform.py")

        # Broad policy statement for training purposes
        policy_statement = iam.PolicyStatement(
                actions=['logs:*','s3:*','ec2:*','iam:*','glue:*']
            )
        
        policy_statement.add_all_resources()

        # Create an iam role for our glue job
        glue_job_role = iam.Role(
            self,
            'Glue-Job-Role',
            assumed_by=iam.ServicePrincipal('glue.amazonaws.com')
        )

        glue_job_role.add_to_policy(
            policy_statement
        )

        # Create the actual job
        job = glue.CfnJob(
            self,
            'glue-test-job',
            role=glue_job_role.role_arn,
            allocated_capacity=10,
            command=glue.CfnJob.JobCommandProperty(
                name='glueetl',
                script_location=f's3://{script_as_asset.s3_bucket_name}/{script_as_asset.s3_object_key}'
            ))

        script_as_asset.grant_read(glue_job_role)

        # # Create a queue to add tasks
        # queue = sqs.Queue(
        #     self, "WorkshopQueue",
        #     visibility_timeout=core.Duration.seconds(300),
        # )

        # # And a topic for a subscription
        # topic = sns.Topic(
        #     self, "WorkshopTopic",
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))

