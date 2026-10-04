BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "bookingid": {
            "type": "integer"
        },
        "booking": {
            "type": "object",
            "properties": {
                "firstname": {
                    "type": "string"
                },
                "lastname": {
                    "type": "string"
                },
                "totalprice": {
                    "type": "integer"
                },
                "depositpaid": {
                    "type": "boolean"
                },
                "bookingdates": {
                    "type": "object",
                    "properties": {
                        "checkin": {
                            "type": "date",
                            "format": "YYYY-MM-DD"
                        },
                        "checkout": {
                            "type": "date",
                            "format": "YYYY-MM-DD"
                        }
                    }
                }
            },
                "additionalneeds": {
                    "type": "string"
                }
        }
    },
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"],
    "additionalProperties": False
}