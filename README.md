
# DevSpace HTML

A personal website with modern HTML/CSS design.

## Description

This serves a personal portfolio website featuring multiple pages including home, about, projects, resume, blog, and subscription functionality. The project uses Tailwind CSS for styling and includes automated deployment to AWS S3 with CloudFront invalidation through GitHub Actions. 

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

* HTML & CSS
* Modern web browser
* AWS account (for deployment)

### Installing

* Clone or download this repository to your local machine
* Nothing to install!

### Executing program

* To run the development server open index.html in your web browser


## Authors

Contributors names and contact info

Joe Webb - [joewebbphd.com](https://joewebbphd.com)

## Version History

* 0.1
    * Initial Release - HTML template conversion
