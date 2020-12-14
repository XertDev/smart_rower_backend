SQLALCHEMY_TRACK_MODIFICATIONS = False
SWAGGER = {
	"title": "API",
	"uiversion": 3,
	"openapi": '3.0.5',
	"components": {
		"schemas": {
			"ScooterState": {
				"type": "string",
				"enum": [
					"AVAILABLE",
					"IN_RUN",
					"DISABLED"
				]
			},
			"ScooterWithStatus": {
				"type": "object",
				"properties": {
					"id": {
						"type": "integer"
					},
					"state": {
						"$ref": "#/components/schemas/ScooterState"
					},
					"last_status": {
						"type": "object",
						"properties": {
							"timestamp": {
								"type": "date"
							},
							"battery_level": {
								"type": "integer"
							}
						}
					}
				}
			},
			"Scooter": {
				"type": "object",
				"properties": {
					"id": {
						"type": "integer"
					},
					"state": {
						"$ref": "#/components/schemas/ScooterState"
					}
				}
			}
		}
	}
}
