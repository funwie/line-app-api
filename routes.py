

def register_routes(api, app, root="api"):
    from user import register_routes as user_routes

    # Add routes
    user_routes(api, app)