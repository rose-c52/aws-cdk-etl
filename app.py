#!/usr/bin/env python3

from aws_cdk import core

from workshop.workshop_stack import WorkshopStack


app = core.App()
WorkshopStack(app, "workshop", env={'region': 'us-west-2'})

app.synth()
