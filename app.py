#!/usr/bin/env python3

from aws_cdk import core

from workshop.glue import GlueJob


app = core.App()
GlueJob(app, "workshop", env={'region': 'eu-west-2'})

app.synth()
