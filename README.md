## ETL using AWS CDK


This example uses the New York Air BnB Open Data set from kaggle, but you can pick any data set you would like to work on. The following links have loads of pubicly availble datasets to choose from:
* https://registry.opendata.aws/
* https://www.kaggle.com/

### Set up

You'll need to set up some things if you haven't already:
* Python - https://www.python.org/downloads/
* AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
* Node.js and NPM - https://nodejs.org/en/
* AWS CDK Toolkit - Once npm is installed run <code>npm install -g aws-cdk</code>

This example uses python, but feel free to use any of the languages available with CDK. We're going to use <code>cdk init</code> to create our project. More information can be found here: https://cdkworkshop.com/30-python/20-create-project/100-cdk-init.html

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

Useful commands:

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 
 
 


