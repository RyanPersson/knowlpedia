# Research Task: Commenting Systems for Math Blogs

## Objective
Find a commenting system that balances accessibility for general users with LaTeX support for mathematical discussions.

## Requirements (Prioritized)

### Must Have
- Works with static sites / GitHub Pages
- Reasonably user-friendly (not requiring obscure account types)
- Open source or privacy-respecting (avoid heavy tracking)

### Strong Preference
- LaTeX/math rendering in comments
- No required GitHub account (mathematicians often don't have one)
- Moderation capabilities

### Nice to Have
- Self-hostable
- Markdown support in comments
- Email notifications
- Spam filtering

## Candidates to Research

### GitHub-Based
1. **Giscus** (github.com/giscus/giscus)
   - Uses GitHub Discussions
   - Requires GitHub account to comment
   - Check: LaTeX support? Theming?

2. **Utterances** (utteranc.es)
   - Uses GitHub Issues
   - Same limitation: requires GitHub
   - Check: still maintained? LaTeX?

### Self-Hosted / Open Source
3. **Remark42**
   - Self-hosted, privacy-focused
   - Check: math support, ease of deployment

4. **Commento** (or Commento++)
   - Open source option
   - Check: current status, features

5. **Isso**
   - Python-based, self-hosted
   - Check: extensibility for math

### Third-Party Services
6. **Hyvor Talk**
   - Paid service, privacy-focused
   - Check: LaTeX support, pricing

7. **Disqus**
   - Most common, but privacy concerns
   - Check: LaTeX support (likely no)

### Unconventional Options
8. **Email-based**
   - Just provide contact email, curate responses manually
   - Low friction for readers, high friction for author

9. **Webmention + IndieWeb**
   - Decentralized commenting via links
   - Check: feasibility, math support

10. **Custom solution**
    - Build minimal system with math rendering
    - Evaluate effort vs. benefit

## Key Questions

1. Does ANY commenting system natively support LaTeX/MathJax?
2. If not, can we inject MathJax into comment rendering?
3. What % of target audience (mathematicians) likely has GitHub?
4. Is self-hosting viable for the author's situation?
5. What do other math blogs use? (research examples)

## Deliverable
- Comparison table with pros/cons
- Recommendation with rationale
- Note if "no good solution exists" and alternatives (e.g., email)
- Examples of math blogs and their commenting approach
