from flask import Flask, render_template
from datetime import datetime

# Create the Flask application instance
app = Flask(__name__)


# Inject current year into templates for footer display
@app.context_processor
def inject_now() -> dict:
    """Adds the current year to the template context."""
    return {"current_year": datetime.now().year}


@app.route('/')
def index() -> str:
    """Render the home/landing page."""
    return render_template('index.html')


@app.route('/about')
def about() -> str:
    """Render the about page."""
    return render_template('about.html')


@app.route('/projects')
def projects() -> str:
    """Render the projects page."""
    return render_template('projects.html')


@app.route('/contact')
def contact() -> str:
    """Render the contact page."""
    return render_template('contact.html')


# if __name__ == '__main__':
#     # For local development enable debug mode for hot reloading.
#     app.run(debug=True)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)