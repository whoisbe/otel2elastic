# Set up OpenTelemetry collector 
Set up [OpenTelemetry collector](https://opentelemetry.io/docs/concepts/components/#collector) and configure it to export telemetry data to Elastic APM server

  1. Ensure you have [docker installed](https://docs.docker.com/desktop/#download-and-install) correctly and is working. `docker --version` should produce an output that looks something like `Docker version 20.10.12, build 20.10.12-0ubuntu4`.
  2. Clone this repo and change into the `Config` directory, open up the `collector-config.yaml` file in a text editor and examine it. Notice line# 9 contains exporter oltp/elastic added for Elastic APM server.
```bash
git clone https://github.com/whoisbe/otel2elastic.git
cd otel2elastic/Config
vim collector-config.yaml
```
  3. Go back to the Elastic integration wizard that you left open in the last step of previous task and copy the value for `serverUrl` and paste it in as the value for `endpoint` in line# 10.
  4. Once again, go back to the wizard and copy the value for `secretToken` and paste it in replacing the existing token value found in line# 12 after the word `Bearer`. Here is an example:
```yaml
exporters:
  logging:
    loglevel: debug
  otlp/elastic:
    endpoint: https://1a8zfad07dda44f8935b5d2e7a9cd844.apm.us-central1.gcp.cloud.es.io:443
    headers:
      Authorization: "Bearer 5lNpu2GOflkPWbY9Bi"
```
  5. Save the file and copy it to `/tmp`

```bash
cp collector-config.yaml /tmp/
```
  6. Run the following docker command to pull the OpenTelemetry collector image and start a container that uses the saved configuration.

```bash
docker run -p 4317:4317 \
    -v /tmp/collector-config.yaml:/etc/collector-config.yaml \
    otel/opentelemetry-collector:latest \
    --config=/etc/collector-config.yaml
```
 7. You have now set up a collector instance that's listening on port 4317 for data. We can now move on to the [last task](instrument.md)

[Previous](deploy.md) \| [Next](instrument.md)