'''
        API Documentation
'''
REGISTER_DOCS = {
    "tags": [
        "User"
    ],
    "description": "User registration",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "User details",
            "required": True,
            "schema": {
                "id": "User",
                "required": [
                    "username",
                    "email",
                    "password",
                    "confirm_password",
                ],
                "properties": {
                    "username": {
                        "type": "string",
                        "minimum": 6,
                        "example": "muhozie",
                    },
                    "email": {
                        "type": "email",
                        "example": "muhozie@gmail.com"
                    },
                    "password": {
                        "type": "string",
                        "example": "123456",
                    },
                    "confirm_password": {
                        "type": "string",
                        "example": "123456",
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and message",
            "schema": {
                "id": "registration_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "You have been successfully registered"
                    },
                }
            }
        }
    }
}

LOGIN_DOCS = {
    "tags": [
        "User"
    ],
    "description": "User login by providing valid credentials",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "User credentials",
            "required": True,
            "schema": {
                "id": "login",
                "required": [
                    "email",
                    "password"
                ],
                "properties": {
                    "email": {
                        "type": "email",
                        "example": "muhozie@gmail.com"
                    },
                    "password": {
                        "type": "string",
                        "example": "123456"
                    },
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Return response status and message",
            "schema": {
                "id": "login_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "You have been successfully logged in"
                    },
                    "access_token": {
                        "type": "string",
                        "example": "token....."
                    },
                }
            }
        }
    }
}

LOGOUT_DOCS = {
    "tags": [
        "User"
    ],
    "description": "User logout",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "Return response status and message",
            "schema": {
                "id": "logout_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "You have successfully logged out"
                    },
                }
            }
        }
    }
}

RESET_LINK_DOCS = {
    "tags": [
        "User"
    ],
    "description": "Send password reset link",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Email",
            "required": True,
            "schema": {
                "id": "reset_link_schema",
                "required": [
                    "email",
                ],
                "properties": {
                    "email": {
                        "type": "string",
                        "example": "muhozie@gmail.com"
                    }
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and message",
            "schema": {
                "id": "reset_password_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("Your password has been "
                                    "changed successfully")
                    },
                }
            }
        }
    }
}

CONFIRM_EMAIL_DOCS = {
    "tags": [
        "User"
    ],
    "description": "Confirm email",
    "parameters": [
        {
            "name": "token",
            "in": "path",
            "description": "Confirmation token",
            "schema": {
                "type": "string",
            },
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "Email",
            "required": True,
            "schema": {
                "id": "confirm_email_schema",
                "required": [
                    "email",
                ],
                "properties": {
                    "email": {
                        "type": "string",
                        "example": "muhozie@gmail.com"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Return response status and message",
            "schema": {
                "id": "reset_password_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "Your email was confirmed successfully"
                    },
                }
            }
        }
    }
}

CONFIRM_TOKEN_DOCS = {
    "tags": [
        "User"
    ],
    "description": "Confirm email confirmation token",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Token",
            "required": True,
            "schema": {
                "id": "confirm_token_schema",
                "required": [
                    "token",
                ],
                "properties": {
                    "token": {
                        "type": "string",
                        "example": "kjsdbfkjsdbfkjsdbfkjsdbfkjsdbkjfbs"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Return response status and message",
            "schema": {
                "id": "confirm_token_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "Token exists!"
                    },
                }
            }
        }
    }
}

RESET_PASSWORD_DOCS = {
    "tags": [
        "User"
    ],
    "description": "Change password by providing old and new passwords",
    "parameters": [
        {
            "name": "token",
            "in": "path",
            "description": "Reset token",
            "schema": {
                "type": "string",
            },
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "Old password & New password",
            "required": True,
            "schema": {
                "id": "reset_password_schema",
                "required": [
                    "email",
                    "old_password",
                    "confirm_password",
                ],
                "properties": {
                    "email": {
                        "type": "string",
                        "example": "muhozie@gmail.com"
                    },
                    "password": {
                        "type": "string",
                        "example": "123456"
                    },
                    "confirm_password": {
                        "type": "string",
                        "example": "12345678"
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and message",
            "schema": {
                "id": "reset_password_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("Your password has been "
                                    "changed successfully")
                    },
                }
            }
        }
    }
}

CHANGE_PASSWORD_DOCS = {
    "tags": [
        "User"
    ],
    "description": "Change password by providing old and new passwords",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "type": "string",
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "Old password & New password",
            "required": True,
            "schema": {
                "id": "change_password_schema",
                "required": [
                    "old_password",
                    "new_password"
                ],
                "properties": {
                    "old_password": {
                        "type": "string",
                        "example": "123456"
                    },
                    "new_password": {
                        "type": "string",
                        "example": "12345678"
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and message",
            "schema": {
                "id": "reset_password_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("You have successfully "
                                    "changed your password")
                    },
                }
            }
        }
    }
}

REGISTER_BUSINESS_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Business registration",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "type": "string",
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "New business details",
            "required": True,
            "schema": {
                "id": "New_business_details",
                "required": [
                    "name",
                    "description",
                    "category",
                    "country",
                    "city",
                ],
                "properties": {
                    "name": {
                        "type": "string",
                        "minimum": 6,
                        "max": 30,
                        "example": "Inzora rooftop coffee"
                    },
                    "description": {
                        "type": "string",
                        "example": "We have best coffee"
                    },
                    "category": {
                        "type": "string",
                        "example": "Coffee-shop"
                    },
                    "country": {
                        "type": "string",
                        "example": "Kenya"
                    },
                    "city": {
                        "type": "string",
                        "example": "Nairobi"
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and response message",
            "schema": {
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("Your business has been"
                                    "successfully registered")
                    },
                }
            }
        }
    }
}

UPDATE_BUSINESS_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Update business details by the owner (authenticated user)",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "type": "string",
            "required": True,
        },
        {
            "name": "business_id",
            "in": "path",
            "description": "Business id",
            "type": "string",
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "New business details",
            "required": True,
            "schema": {
                "id": "update_business_data_model",
                "required": [
                    "name",
                    "description",
                    "category",
                    "country",
                    "city",
                ],
                "properties": {
                    "name": {
                        "type": "string",
                        "example": "Monaco Coffee"
                    },
                    "description": {
                        "type": "string",
                        "example": "We have best coffee"
                    },
                    "category": {
                        "type": "string",
                        "example": "Café-resto"
                    },
                    "country": {
                        "type": "string",
                        "example": "Rwanda"
                    },
                    "city": {
                        "type": "string",
                        "example": "Kigali"
                    },
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Return response status and response message",
            "schema": {
                "id": "update_business_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("Your business has been "
                                    "successfully updated")
                    },
                }
            }
        }
    }
}

GET_BUSINESSES_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Get a list of authenticated user businesses",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        },
        {
            "name": "name",
            "in": "query",
            "description": "Search business by name",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "category",
            "in": "query",
            "description": "Search by category",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "country",
            "in": "query",
            "description": "Search by country",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "city",
            "in": "query",
            "description": "Search by city",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "limit",
            "in": "query",
            "description": "Businesses limit per page",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "page",
            "in": "query",
            "description": "Page number",
            "schema": {
                "type": "string",
            },
            "required": False,
        }
    ],
    "responses": {
        "200": {
            "description": ("Get all authenticated user's businesses list "),
            "schema": {
                "id": "get_all_businesses_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("You have businesses "
                                    "1 registered businesses")
                    },
                    "businesses": {
                        "type": "array",
                        "items": {
                            "properties": [{
                                "id": {
                                    "type": "string",
                                    "example": "a69de3743ae249dc3dc2e54c91b3b"
                                },
                                "user_id": {
                                    "type": "string",
                                    "example": "a69de3743ae24ac89c2e54c9bdsf"
                                },
                                "name": {
                                    "type": "string",
                                    "example": "Inzora rooftop"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "We get best coffee"
                                },
                                "category": {
                                    "type": "string",
                                    "example": "Coffee-shop"
                                },
                                "country": {
                                    "type": "string",
                                    "example": "Rwanda"
                                },
                                "city": {
                                    "type": "string",
                                    "example": "Kigali"
                                },
                                "reviews_count": {
                                    "type": "string",
                                    "example": "1"
                                },
                                "created_at": {
                                    "type": "string",
                                    "example": "Thu, 24 May 2018 19:14:36 GMT"
                                },
                            }]
                        }
                    },
                }
            },
        }
    }
}

GET_ALL_BUSINESSES_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Get a list of all businesses",
    "parameters": [
        {
            "name": "searchAll",
            "in": "query",
            "description": "Search business by name",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "name",
            "in": "query",
            "description": "Search business by name",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "category",
            "in": "query",
            "description": "Search by category",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "country",
            "in": "query",
            "description": "Search by country",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "city",
            "in": "query",
            "description": "Search by city",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "limit",
            "in": "query",
            "description": "Businesses limit per page",
            "schema": {
                "type": "string",
            },
            "required": False,
        },
        {
            "name": "page",
            "in": "query",
            "description": "Page number",
            "schema": {
                "type": "string",
            },
            "required": False,
        }
    ],
    "responses": {
        "200": {
            "description": "Return all registered businesses ",
            "schema": {
                "id": "get_all_businesses_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("You have businesses 1 "
                                    "registered businesses")
                    },
                    "businesses": {
                        "type": "array",
                        "items": [{
                            "properties": {
                                "id": {
                                    "type": "string",
                                    "example": "a69de3743aec89dc3dc2e54c91b3b"
                                },
                                "user_id": {
                                    "type": "string",
                                    "example": "a69de3743ae89dc3dc2e54c9bdsf"
                                },
                                "name": {
                                    "type": "string",
                                    "example": "Inzora rooftop"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "We get best coffee"
                                },
                                "category": {
                                    "type": "string",
                                    "example": "Coffee-shop"
                                },
                                "country": {
                                    "type": "string",
                                    "example": "Rwanda"
                                },
                                "city": {
                                    "type": "string",
                                    "example": "Kigali"
                                },
                                "reviews_count": {
                                    "type": "string",
                                    "example": "1"
                                },
                                "created_at": {
                                    "type": "string",
                                    "example": "Thu, 24 May 2018 19:14:36 GMT"
                                },
                            }
                        }]
                    },
                }
            },
        }
    }
}

GET_BUSINESS_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Get a business details",
    "parameters": [
        {
            "name": "business_id",
            "in": "path",
            "description": "Business id",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": ("Return response status "
                            "and message and business details"),
            "schema": {
                "id": "get_business_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "Business found"
                    },
                    "business": {
                        "type": "object",
                        "schema": {
                            "properties": {
                                "id": {
                                    "type": "string",
                                    "example": "a69de3743aec89dc3dc2e54c91b3b"
                                },
                                "user_id": {
                                    "type": "string",
                                    "example": "a69de3743aec89dc3dc2e54c9bdsf"
                                },
                                "name": {
                                    "type": "string",
                                    "example": "Inzora rooftop"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "We get best coffee"
                                },
                                "category": {
                                    "type": "string",
                                    "example": "Coffee-shop"
                                },
                                "country": {
                                    "type": "string",
                                    "example": "Rwanda"
                                },
                                "city": {
                                    "type": "string",
                                    "example": "Kigali"
                                },
                                "reviews_count": {
                                    "type": "string",
                                    "example": "1"
                                },
                                "created_at": {
                                    "type": "string",
                                    "example": "Thu, 24 May 2018 19:14:36 GMT"
                                },
                            }
                        }
                    },
                }
            },
        }
    }
}

DELETE_BUSINESS_DOCS = {
    "tags": [
        "Business"
    ],
    "description": "Business deletion by the owner(authenticated user)",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "type": "string",
            "required": True,
        },
        {
            "name": "business_id",
            "in": "path",
            "description": "Business id",
            "type": "string",
            "required": True,
        },
    ],
    "responses": {
        "202": {
            "description": "Return response status and response message",
            "schema": {
                "id": "delete_business_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": ("Your business has"
                                    "been successfully deleted")
                    },
                }
            }
        }
    }
}

BUSINESS_REVIEWS_DOCS = {
    "tags": [
        "Reviews"
    ],
    "description": "Get a list business reviews",
    "parameters": [
        {
            "name": "business_id",
            "in": "path",
            "description": "Business id",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "Return business reviews ",
            "schema": {
                "id": "business_reviews_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "1 review found"
                    },
                    "business": {
                        "type": "object",
                        "schema": {
                            "properties": {
                                "id": {
                                    "type": "string",
                                    "example": "a69de3743ae24ac3dc2e54c91b3b"
                                },
                                "user_id": {
                                    "type": "string",
                                    "example": "a69de3743ae24acc3dc2e54c9bdsf"
                                },
                                "name": {
                                    "type": "string",
                                    "example": "Inzora rooftop"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "We get best coffee"
                                },
                                "category": {
                                    "type": "string",
                                    "example": "Coffee-shop"
                                },
                                "country": {
                                    "type": "string",
                                    "example": "Rwanda"
                                },
                                "city": {
                                    "type": "string",
                                    "example": "Kigali"
                                },
                                "reviews_count": {
                                    "type": "string",
                                    "example": "1"
                                },
                                "created_at": {
                                    "type": "string",
                                    "example": "Thu, 24 May 2018 19:14:36 GMT"
                                },
                            }
                        }
                    },
                    "reviews": {
                        "type": "array",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string",
                                    "example": "c9918c47a9a76af54ce44a6d60e2d"
                                },
                                "user": {
                                    "type": "string",
                                    "example": "emery"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "You have best coffee"
                                },
                                "created_at": {
                                    "type": "string",
                                    "example": "2018-03-18 11:04"
                                },
                            }
                        }
                    },
                }
            },
        }
    }
}

ADD_BUSINESS_REVIEW_DOCS = {
    "tags": [
        "Reviews"
    ],
    "description": "Add business review",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization token",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        },
        {
            "name": "business_id",
            "in": "path",
            "description": "Business id",
            "schema": {
                "type": "string",
                "format": "uuid",
            },
            "required": True,
        },
        {
            "name": "body",
            "in": "body",
            "description": "Review",
            "required": True,
            "schema": {
                "id": "review_request_scheme",
                "required": [
                    "review",
                ],
                "properties": {
                    "review": {
                        "type": "string",
                        "example": "You have a great services"
                    },
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Return response status and message",
            "schema": {
                "id": "add_business_review_response",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok"
                    },
                    "message": {
                        "type": "string",
                        "example": "Your review has been submitted"
                    },
                }
            }
        }
    }
}
