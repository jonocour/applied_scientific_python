"""
01_lab_vs_actions.py
=======================

Reference Guide: GitLab CI vs GitHub Actions
---------------------------------------------

| Feature          | GitLab CI                                        | GitHub Actions                              |
|------------------|--------------------------------------------------|---------------------------------------------|
| CI/CD Definition | `.gitlab-ci.yml` at project root                 | `.github/workflows/*.yml` inside `.github/` |
| Trigger Events   | Push, Merge Request, Tag, Scheduled, Manual      | Push, Pull Request, Tag, Scheduled          |
| Integrated UI    | Pipelines, Jobs, Logs, Artifacts inside GitLab   | Actions Tab, Logs, Marketplace Integration  |
| Runners          | Shared (GitLab) or Self-hosted                   | GitHub-hosted or Self-hosted Runners        |
| Marketplace      | Built-in templates, fewer third-party options    | Huge community-driven Actions Marketplace   |
| Best For         | Internal teams, enterprise, private repositories | Open-source projects, GitHub-hosted repos   |

Topics Covered:
---------------
- How CI/CD pipelines are defined in both platforms
- Differences in triggers and events
- Overview of runners and execution environments
- Integration with project management tools
- Use cases where one may suit better than the other

"""

