
# DevSpace HTML

A Flask-based personal portfolio and blog website template with modern HTML/CSS design.

## Description

This is a Flask web application that serves a personal portfolio website featuring multiple pages including home, about, projects, resume, blog, and subscription functionality. The project uses Tailwind CSS for styling and includes automated deployment to AWS S3 with CloudFront invalidation through GitHub Actions. The template was originally designed by Cruip and has been enhanced with Flask templating using Jinja2 for dynamic content rendering.

## AWS S3 Static Site Hosting Workflow

This project demonstrates a cost-effective workflow for hosting static websites on AWS for approximately $1/month:

### Workflow Overview
1. **Development**: Create/edit HTML, CSS, and JavaScript files locally or in Replit
2. **Version Control**: Commit changes to GitHub repository 
3. **Automated Deployment**: GitHub Actions automatically deploys changed files to S3
4. **Content Distribution**: CloudFront CDN serves content globally with fast load times
5. **Cost Optimization**: Pay only for storage (~$0.50/month) and minimal data transfer costs

### GitHub Actions Pipeline
- **Trigger**: Automatically runs on commits to main/master branch
- **Changed Files Detection**: Only uploads modified files to reduce transfer costs
- **S3 Sync**: Copies changed files to S3 bucket with public-read permissions
- **CloudFront Invalidation**: Clears CDN cache to serve updated content immediately
- **Security**: Uses GitHub Secrets for AWS credentials (AWS_KEY, AWS_SECRET)

### Cost Breakdown (Approximate)
- **S3 Storage**: ~$0.50/month for typical website files
- **CloudFront**: ~$0.50/month for moderate traffic
- **Data Transfer**: Minimal costs for most personal/small business sites
- **Total**: ~$1-2/month for a fast, globally distributed website

This setup provides enterprise-level hosting capabilities at a fraction of traditional hosting costs.

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
