# grafana-step-create-annotation

This step adds an [annotation](https://grafana.com/docs/grafana/latest/dashboards/annotations/) to a [Grafana dashboard](https://grafana.com/docs/grafana/latest/dashboards/) using the [Grafana Annotations API](https://grafana.com/docs/grafana/latest/http_api/annotations/#create-annotation).

* If both `dashboardId` and `panelId` are omitted, the annotation will be global.
* If a `dashboardId` is provided, but a `panelId` is omitted, the annotations will be applied to all panels for the given dashboard.
* The start time defaults to the current time if not provided.
* The end time defaults to the start time if not provided.
