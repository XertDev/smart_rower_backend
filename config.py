SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO=True

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
			},
			"RideCheckpoint": {
				"type": "object",
				"properties": {
					"timestamp": {
						"type": "date"
					},
					"battery_level": {
						"type": "integer"
					},
					"location_x": {
						"type": "float"
					},
					"location_y": {
						"type": "float"
					}
				}
			},
			"Ride": {
				"type": "object",
				"properties": {
					"id": {
						"type": "integer"
					},
					"client_id": {
						"type": "integer"
					},
					"scooter_id": {
						"type": "integer"
					},
					"start_time": {
						"type": "date"
					},
					"end_time": {
						"type": "date"
					},
					"checkpoints": {
						"type": "array",
						"items": {
							"$ref": "#/components/schemas/RideCheckpoint"
						}
					}
				}
			}
		}
	}
}
