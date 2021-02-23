# grafana-step-create-annotation

This step adds an annotation to a Grafana dashboard.

Annotate a dashboard with an event from a Relay workflow.
If the panelId and dashboardId are omitted, the annotation
will be global. Note this does not yet support region
(timespan) annotations; the timestamp will be the time
at which the workflow runs.

