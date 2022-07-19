# Set up an Elastic deployment
Set up an Elastic deployment that will serve as the final destination for telemetry data
 1. Our goal is to get telemetry data to end up in Elastic Observability for analysis. So let's set up an Elastic deployment for that purpose.
 2. Go to [https://cloud.elastic.co](https://cloud.elastic.co) and sign in if you have an account. If you don't have an account, using the "Sign up" button (on the top right) you can sign up for a free 14 day trial account (no credit card required).
 3. Once signed in, create a deployment with default settings. It will take a few minutes for the deployment to be ready.
 4. Once the deployment is ready, you can click "Continue" and that will sign you into Kibana using single sign on.
 5. In the welcome prompt, click "Add integrations" and in the resulting Integrations page click the "Elastic APM" card.
 6. Elastic APM Server is set up by default in default cloud deployments. We can confirm this by clicking on "Check APM Server status".
 7. Scroll down to the APM Agents section. We are actually not going to set up any integrations using these wizards. Current version of Elastic stack (v 8.3.2) does not have any integration wizards to set up OpenTelemetry. However, We can use this wizard to obtain the server url and the secret token values from under the "Configure the agent" section that will be used in the next task.
 8. We now have successfully set up the destination for our data pipeline. With this wizard open, we can now move on to the [next task](collect.md).

[Previous](Overview.md) \| [Next](collect.md)