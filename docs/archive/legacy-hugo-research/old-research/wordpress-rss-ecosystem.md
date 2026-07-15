# Research Task: WordPress Ecosystem & RSS Integration

## Context
Many established math blogs run on WordPress. There's an existing community of math blog readers/commenters who likely have WordPress accounts. The user wants to understand if there's a way to tap into this ecosystem while still using a modern static site approach.

## Objective
Explore whether WordPress ecosystem integration (especially for commenting) is feasible for a GitHub Pages / static site blog, and understand the RSS landscape for math blogs.

## Questions to Answer

### WordPress Commenting Integration
1. Can WordPress.com accounts be used to comment on non-WordPress sites?
   - Is there an OAuth/authentication bridge?
   - Any commenting systems that support "Login with WordPress"?

2. What commenting systems do popular WordPress math blogs use?
   - Native WordPress comments?
   - Disqus?
   - Something else?

3. Is there a way to federate or bridge comments?
   - Could comments appear in both places?
   - Webmention or similar protocols?

### RSS & Syndication
1. How does RSS work in the math blog community?
   - Do people actually use RSS readers for math blogs?
   - Is there a "math blog aggregator" or planet?

2. Can a static site easily generate RSS feeds?
   - Most SSGs should support this natively
   - What metadata matters for math blog RSS?

3. Does RSS content render LaTeX?
   - Probably not - how do other math blogs handle this?
   - Is there a convention (e.g., include plain text fallback)?

### The WordPress Math Blog Landscape
1. Which are the most popular/active math blogs?
   - What platforms do they use?
   - How do they handle comments?
   - Examples: Terence Tao's blog, others?

2. Is there a math blogging community/network?
   - Aggregators, webrings, cross-posting norms?

3. Is WordPress actually dominant, or are there other hubs?

### Feasibility Assessment
1. Is WordPress integration worth pursuing, or is it a dead end?
2. What's the realistic overlap between "people with WordPress accounts" and "people who would comment on a math blog"?
3. Are there simpler ways to be part of the math blog community without WordPress?

## Wild Ideas to Evaluate
- Mirror posts to a WordPress.com blog just for comments?
- Use WordPress as a headless CMS?
- Jetpack comments (WordPress.com commenting for external sites)?
- Any WordPress <-> static site bridges?

## Deliverable
1. Honest assessment: Is WordPress integration viable or a rabbit hole?
2. How established math blogs handle commenting
3. RSS best practices for math content
4. Recommendation: pursue WordPress angle or abandon it?
5. Alternative strategies for community integration if WordPress is a dead end
