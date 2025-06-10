
# DevSpace HTML

A Flask-based personal portfolio and blog website template with modern HTML/CSS design.

## Description

This is a Flask web application that serves a personal portfolio website featuring multiple pages including home, about, projects, resume, blog, and subscription functionality. The project uses Tailwind CSS for styling and includes automated deployment to AWS S3 with CloudFront invalidation through GitHub Actions. The template was originally designed by Cruip and has been enhanced with Flask templating using Jinja2 for dynamic content rendering.

## Getting Started

### Dependencies

* Python 3.6 or higher
* Node.js and npm (for Tailwind CSS compilation)
* Flask web framework
* Modern web browser
* AWS account (for deployment)

### Installing

* Clone or download this repository to your local machine
* Install Python dependencies:
```
pip install flask
```
* Install Node.js dependencies:
```
npm install
```
* No additional file modifications are needed for basic setup

### Executing program

* To run the development server:
```
python app.py
```
* To compile CSS during development (in separate terminal):
```
npm run dev
```
* To build CSS for production:
```
npm run build
```
* Access the application at `http://0.0.0.0:5000` in your web browser

## Help

Common issues and solutions:

* If CSS styles aren't loading, make sure to run `npm run build` first
* For development with live CSS reloading, use `npm run dev` in a separate terminal
* Ensure all static files are in the `static/` directory for proper Flask serving

```
python app.py --help
```

## Authors

Contributors names and contact info

Joe Webb - [joewebbphd.com](https://joewebbphd.com)

## Version History

* 0.2
    * Added Flask templating with Jinja2
    * Implemented GitHub Actions deployment
    * Added blog functionality and sidebar navigation
    * Various bug fixes and optimizations
* 0.1
    * Initial Release - HTML template conversion
