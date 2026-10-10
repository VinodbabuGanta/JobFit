# CV Tailoring Assistant

A practical GitHub project that helps you tailor your CV to a specific job description.

This project reads your profile/CV and a target job description, highlights the best matches, identifies missing keywords, and generates a stronger, job-focused summary.

Key features:
- Paste a CV or profile
- Paste a job description
- Score the fit against the role
- Highlight matched and missing skills
- Generate a job-focused summary and recommendations
- Works without any external API or payment requirement

## Project idea
This project is designed for professionals like you who want to apply for roles in:
- Observability
- Infrastructure Operations
- SRE
- Platform Engineering
- Middleware and Cloud Operations

## Quick start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Open the local URL shown in the terminal.

## Files
- `app.py` - Streamlit application
- `resume_matcher.py` - matching and CV tailoring logic
- `sample_profile.txt` - example resume text
- `sample_job_description.txt` - sample job description
- `requirements.txt` - app dependencies

## Example workflow
- Paste your resume into the left panel
- Paste the job description into the right panel
- Click "Analyze & Tailor"
- Review:
  - Match score
  - Matched keywords
  - Missing skills
  - Tailored professional summary

## Future upgrades
- Add PDF upload support
- Add ATS scoring and keyword density checks
- Add export to DOCX/PDF
- Add multiple job description comparison
- Integrate with OpenAI to rewrite sections automatically

## License
MIT
