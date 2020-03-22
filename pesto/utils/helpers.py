def register_view(app, routes, view_func, *args, **kwargs):
    for route in routes:
        app.add_url_rule(route, view_func=view_func, *args, **kwargs)
