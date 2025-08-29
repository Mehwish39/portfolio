# Portfolio Website

This is a simple portfolio website built with **Python** and the **Flask** web framework.  The site is designed to be easy to customise and extend.  It includes a landing page, an about page, a projects page and a contact page.  You can run it locally or deploy it to your preferred hosting service.

## Features

* **Python/Flask back‑end** – the application uses a small Flask server to serve HTML templates.  There is no database dependency by default.
* **Modular templates** – pages are built from a base template (`templates/base.html`) so you can adjust the navigation and layout in one place.
* **Responsive design** – the included CSS uses flexbox and CSS grid to adapt to different screen sizes.
* **Easily customisable** – all content lives in HTML templates and static assets.  Replace the placeholder text and images with your own content.

## Getting started

1. **Install dependencies.**  Navigate into the project folder and install the required Python packages.  It's recommended to create a virtual environment first:

   ```bash
   cd portfolio_site
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the development server.**  Launch the Flask application:

   ```bash
   python app.py
   ```

   By default the app runs on `http://127.0.0.1:5000/`.  Open that URL in a web browser to see your portfolio.

3. **Customise.**  Edit the HTML templates in the `templates/` directory to add your own projects, biography and contact details.  Update the CSS in `static/css/style.css` to tailor the look and feel.  You can replace the image used in the hero section (`static/images/hero.jpg`) with your own photo or artwork.

## Deployment

The app can be deployed to any platform that supports Python.  For example, you could deploy it on [Heroku](https://www.heroku.com/), [Render](https://render.com/) or a simple VPS.  Make sure to set the `FLASK_ENV` environment variable to `production` and configure a proper web server (e.g. Gunicorn) for production deployments.

## License

This project is provided under the MIT License.  Feel free to use it as a starting point for your own portfolio.