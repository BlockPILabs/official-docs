---
description: >-
  Provides a UI that you can use to explore the API. You can also retrieve the
  API directly at /spec.yaml and /spec.json.
---

# Show OpenAPI explorer

#### **Path Parameters:**

None

#### Query Parameters：

None

#### **Response Header:**

None

#### **Response Body:**

Text/html

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/spec

// Result
<!doctype html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta http-equiv="cache-control" content="no-cache">
	<title>Aptos REST API</title>
	<!-- Embed elements Elements via Web Component -->
	<script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
	<link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
</head>

<body>
	<elements-api apiDescriptionUrl="spec.yaml" router="hash" layout="sidebar" hideInternal="true" />
</body>

</html>
```
{% endcode %}
